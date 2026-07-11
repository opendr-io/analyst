import argparse
import json
import sys
from pathlib import Path
from typing import Any

from knowledge_indexing import knowledge_index as ki
import llm_client

from .annotate import format_provider_error
from .common import (
    CLASSIFICATION_MAX_INPUT_TOKENS,
    CLASSIFICATION_MAX_OUTPUT_TOKENS,
    CLASSIFICATION_SCHEMA_VERSION,
    CLASSIFY_SYSTEM_TEMPLATE,
    MODEL_CLASSIFY,
    as_string_list,
    estimate_tokens,
    json_list_text,
    strip_code_fence,
)

CLASSIFICATION_TEXT_FORMAT = {
    "format": {
        "type": "json_schema",
        "name": "record_classification",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "primary_topic": {"type": "string"},
                "secondary_topics": {"type": "array", "items": {"type": "string"}},
                "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
                "rationale": {"type": "string"},
                "new_topic_candidate": {"type": "string"},
            },
            "required": [
                "id",
                "primary_topic",
                "secondary_topics",
                "confidence",
                "rationale",
                "new_topic_candidate",
            ],
            "additionalProperties": False,
        },
    }
}


def get_classification_topics(db_path: Path = ki.DB_PATH) -> list[str]:
    return ki.list_classification_topics(db_path, include_candidates=False)


def build_classify_system(topics: list[str]) -> str:
    definitions = {name: definition for name, definition in ki.SEED_TOPICS}
    topics_numbered = "\n".join(
        f"{i + 1}. {name}"
        + (f"\n   Definition: {definitions[name]}" if name in definitions else "")
        for i, name in enumerate(topics)
    )
    return (
        CLASSIFY_SYSTEM_TEMPLATE
        .replace("{topic_count}", str(len(topics)))
        .replace("{topics_numbered}", topics_numbered)
    )


def _annotation_payload(annotation: object | None) -> dict[str, Any]:
    if not annotation:
        return {}
    return {
        "summary": annotation["short_summary"],
        "keywords": json_list_text(annotation["keywords_json"]),
        "tools": json_list_text(annotation["tools_json"]),
        "people": json_list_text(annotation["people_json"]),
        "claims": json_list_text(annotation["claims_json"]),
        "use_cases": json_list_text(annotation["use_cases_json"]),
        "ai_relevance": annotation["ai_relevance"] if "ai_relevance" in annotation.keys() else "",
        "content_types": json_list_text(annotation["content_types_json"]) if "content_types_json" in annotation.keys() else "",
        "security_domains": json_list_text(annotation["security_domains_json"]) if "security_domains_json" in annotation.keys() else "",
        "contains_prompt_injection": bool(annotation["contains_prompt_injection"]) if "contains_prompt_injection" in annotation.keys() else False,
        "relevance_notes": annotation["relevance_notes"] if "relevance_notes" in annotation.keys() else "",
    }


def build_classification_request(
    record: object,
    annotation: object | None = None,
    topics: list[str] | None = None,
) -> tuple[dict[str, Any], str, int]:
    topics = topics or get_classification_topics()
    payload = {
        "id": int(record["id"]),
        "source": record["source"],
        "title": record["title"],
        "author": record["author"],
        "event": record["event"] if "event" in record.keys() else "",
        "year": record["year"] if "year" in record.keys() else "",
        "tags": record["tags"],
        "url": record["url"] if "url" in record.keys() else "",
        "annotation": _annotation_payload(annotation),
        "text": record["text"],
    }
    system = build_classify_system(topics)
    content = "Classify this record:\n\n" + json.dumps(payload, ensure_ascii=False, indent=2)
    input_tokens = estimate_tokens(system) + estimate_tokens(content)
    return payload, content, input_tokens


def normalize_classification_result(item: dict[str, Any], record_id: int, topics: list[str]) -> dict[str, Any]:
    topic_set = set(topics)
    primary_topic = str(item.get("primary_topic", "")).strip()
    if primary_topic not in topic_set and primary_topic != "Unclassified":
        primary_topic = "Unclassified"
    secondary_topics = [
        topic
        for topic in as_string_list(item.get("secondary_topics"))
        if topic in topic_set and topic != primary_topic
    ][:2]
    confidence = str(item.get("confidence", "")).strip().lower()
    if confidence not in {"high", "medium", "low"}:
        confidence = "low"
    return {
        "id": int(item.get("id", record_id)),
        "primary_topic": primary_topic,
        "secondary_topics": secondary_topics,
        "confidence": confidence,
        "rationale": str(item.get("rationale", "")).strip(),
        "new_topic_candidate": str(item.get("new_topic_candidate", "")).strip(),
    }


def classify_record(
    client: Any,
    record: object,
    annotation: object | None = None,
    dry_run: bool = False,
    topics: list[str] | None = None,
) -> dict[str, Any]:
    topics = topics or get_classification_topics()
    _payload, content, input_tokens = build_classification_request(record, annotation, topics)
    record_id = int(record["id"])
    if input_tokens > CLASSIFICATION_MAX_INPUT_TOKENS:
        raise ValueError(
            "classification input exceeds max token budget "
            f"({input_tokens} estimated tokens > {CLASSIFICATION_MAX_INPUT_TOKENS}); "
            f"record_id={record_id}"
        )
    if dry_run:
        print(f"  [dry-run] would classify record {record_id} with {MODEL_CLASSIFY} ({input_tokens} estimated input tokens)")
        return {
            "id": record_id,
            "primary_topic": "Unclassified",
            "secondary_topics": [],
            "confidence": "low",
            "rationale": "",
            "new_topic_candidate": "",
            "estimated_input_tokens": input_tokens,
            "dry_run": True,
        }

    response = client.messages.create(
        model=MODEL_CLASSIFY,
        max_tokens=CLASSIFICATION_MAX_OUTPUT_TOKENS,
        system=[
            {
                "type": "text",
                "text": build_classify_system(topics),
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        text=CLASSIFICATION_TEXT_FORMAT,
    )

    raw = strip_code_fence(response.content[0].text)
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"model returned invalid JSON: {exc} | raw: {raw[:200]}") from exc
    if not isinstance(parsed, dict):
        raise ValueError(f"model returned non-object classification JSON: {raw[:200]}")
    result = normalize_classification_result(parsed, record_id, topics)
    result["model"] = MODEL_CLASSIFY
    result["estimated_input_tokens"] = input_tokens
    return result


def run_classify(args: argparse.Namespace, client: Any | None = None) -> int:
    client = client or llm_client.create_client()
    db_path = ki.DB_PATH
    topics = get_classification_topics(db_path)

    total_processed = 0
    total_tagged = 0
    total_errors = 0
    dry_run_seen_ids: set[int] = set()
    skipped_record_ids: set[int] = set()

    print(f"model: {MODEL_CLASSIFY}")
    print(f"batch_size: {args.batch_size}")
    print(f"topics: {len(topics)}")
    print(f"max_input_tokens: {CLASSIFICATION_MAX_INPUT_TOKENS}")
    print("record_text: full")
    start_id = int(getattr(args, "start_id", 0) or 0)
    if start_id:
        print(f"start_id: {start_id}")

    while True:
        if args.limit and total_processed >= args.limit:
            print(f"reached --limit {args.limit}, stopping")
            break

        fetch_limit = args.batch_size
        if args.limit:
            fetch_limit = min(fetch_limit, args.limit - total_processed)

        excluded_ids = dry_run_seen_ids | skipped_record_ids
        lookup_limit = fetch_limit + len(excluded_ids)
        rows = [
            row
            for row in ki.list_records_missing_classifications(db_path, limit=lookup_limit, start_id=start_id)
            if int(row["id"]) not in excluded_ids
        ][:fetch_limit]
        if not rows:
            print("no more annotated records needing classification")
            break

        annotations = ki.get_record_annotation_map(db_path, [int(row["id"]) for row in rows])
        print(f"\nbatch {total_processed // args.batch_size + 1}: {len(rows)} records")

        for row in rows:
            record_id = int(row["id"])
            try:
                result = classify_record(
                    client,
                    row,
                    annotation=annotations.get(record_id),
                    dry_run=args.dry_run,
                    topics=topics,
                )
            except ValueError as exc:
                error_message = str(exc)
                print(f"  parse error: {error_message}", file=sys.stderr)
                total_errors += 1
                skipped_record_ids.add(record_id)
                if not args.dry_run:
                    ki.store_record_classification_error(
                        db_path,
                        record_id=record_id,
                        model=MODEL_CLASSIFY,
                        error_type=type(exc).__name__,
                        error_message=error_message,
                    )
                continue
            except Exception as exc:
                error_message = format_provider_error(exc)
                print(f"  error: {error_message}", file=sys.stderr)
                total_errors += 1
                skipped_record_ids.add(record_id)
                if not args.dry_run:
                    ki.store_record_classification_error(
                        db_path,
                        record_id=record_id,
                        model=MODEL_CLASSIFY,
                        error_type=type(exc).__name__,
                        error_message=error_message,
                    )
                continue

            primary_topic = result["primary_topic"]
            secondary_topics = result["secondary_topics"]
            record_topics = []
            if primary_topic != "Unclassified":
                record_topics.append(primary_topic)
            record_topics.extend(secondary_topics)

            if not args.dry_run:
                ki.store_record_classification(
                    db_path,
                    record_id=record_id,
                    primary_topic=primary_topic,
                    secondary_topics=secondary_topics,
                    confidence=result["confidence"],
                    rationale=result["rationale"],
                    new_topic_candidate=result["new_topic_candidate"],
                    raw=result,
                    model=MODEL_CLASSIFY,
                    schema_version=CLASSIFICATION_SCHEMA_VERSION,
                )
                ki.set_record_topics(db_path, record_id, record_topics, reader="knowledge_agent")
                ki.clear_record_classification_error(db_path, record_id)

            label = ", ".join(record_topics) if record_topics else "(none)"
            title_short = (row["title"] or "")[:60]
            confidence = result["confidence"]
            candidate = result["new_topic_candidate"]
            suffix = f" | new: {candidate}" if candidate else ""
            ki.safe_print(f"  [{record_id}] {title_short} -> {label} ({confidence}){suffix}")
            if args.dry_run:
                dry_run_seen_ids.add(record_id)

            total_processed += 1
            if record_topics:
                total_tagged += 1

    print(f"\nprocessed: {total_processed}")
    print(f"tagged: {total_tagged}")
    print(f"errors: {total_errors}")
    if skipped_record_ids:
        skipped = ", ".join(str(record_id) for record_id in sorted(skipped_record_ids))
        print(f"skipped_record_ids: {skipped}")
    return 0
