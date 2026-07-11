import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from knowledge_indexing import knowledge_index as ki
import llm_client

from .annotate import format_provider_error
from .common import (
    ANNOTATION_MAX_INPUT_TOKENS,
    MODEL_CLASSIFY,
    OPEN_TOPICS_MAX_OUTPUT_TOKENS,
    as_string_list,
    estimate_tokens,
    json_list_text,
    load_prompt,
    strip_code_fence,
)


OPEN_TOPIC_SYSTEM = load_prompt("open_topic_system.txt")
DEFAULT_JSONL_PATH = ki.STATE_DIR / "open-topic-candidates.jsonl"
DEFAULT_REPORT_PATH = ki.STATE_DIR / "open-topic-report.md"


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


def build_open_topic_request(record: object, annotation: object | None) -> tuple[str, int]:
    payload = {
        "id": int(record["id"]),
        "source": record["source"],
        "title": record["title"],
        "author": record["author"],
        "event": record["event"],
        "year": record["year"],
        "tags": record["tags"],
        "url": record["url"],
        "annotation": _annotation_payload(annotation),
        "text": record["text"],
    }
    content = "Suggest natural topics for this record:\n\n" + json.dumps(payload, ensure_ascii=False, indent=2)
    input_tokens = estimate_tokens(OPEN_TOPIC_SYSTEM) + estimate_tokens(content)
    return content, input_tokens


def discover_record_topics(client: Any, record: object, annotation: object | None, dry_run: bool = False) -> dict[str, Any]:
    content, input_tokens = build_open_topic_request(record, annotation)
    if input_tokens > ANNOTATION_MAX_INPUT_TOKENS:
        raise ValueError(
            "open-topic input exceeds max token budget "
            f"({input_tokens} estimated tokens > {ANNOTATION_MAX_INPUT_TOKENS}); "
            f"record_id={int(record['id'])}"
        )
    if dry_run:
        return {
            "id": int(record["id"]),
            "suggested_topics": [],
            "ai_relevance": "none",
            "content_types": [],
            "rationale": "",
            "estimated_input_tokens": input_tokens,
            "dry_run": True,
        }

    response = client.messages.create(
        model=MODEL_CLASSIFY,
        max_tokens=OPEN_TOPICS_MAX_OUTPUT_TOKENS,
        system=OPEN_TOPIC_SYSTEM,
        messages=[{"role": "user", "content": content}],
    )
    raw = strip_code_fence(response.content[0].text)
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"model returned invalid open-topic JSON: {exc} | raw: {raw[:200]}") from exc
    if not isinstance(parsed, dict):
        raise ValueError(f"model returned non-object open-topic JSON: {raw[:200]}")

    return {
        "id": int(parsed.get("id", record["id"])),
        "suggested_topics": as_string_list(parsed.get("suggested_topics"))[:3],
        "ai_relevance": str(parsed.get("ai_relevance", "none")).strip() or "none",
        "content_types": as_string_list(parsed.get("content_types")),
        "rationale": str(parsed.get("rationale", "")).strip(),
        "model": MODEL_CLASSIFY,
        "estimated_input_tokens": input_tokens,
    }


def _load_existing_ids(path: Path) -> set[int]:
    if not path.exists():
        return set()
    ids: set[int] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        try:
            ids.add(int(item["id"]))
        except (KeyError, TypeError, ValueError):
            continue
    return ids


def load_records_for_open_topic_discovery(
    db_path: Path,
    limit: int = 0,
    source: str = "",
    skip_ids: set[int] | None = None,
) -> list:
    skip_ids = skip_ids or set()
    sql = """
        SELECT records.*
        FROM records
        JOIN record_annotations ON record_annotations.record_id = records.id
        WHERE 1 = 1
    """
    params: list[Any] = []
    if source:
        sql += " AND records.source = ?"
        params.append(source)
    if skip_ids:
        placeholders = ", ".join("?" for _id in skip_ids)
        sql += f" AND records.id NOT IN ({placeholders})"
        params.extend(sorted(skip_ids))
    sql += " ORDER BY records.id"
    if limit and limit > 0:
        sql += " LIMIT ?"
        params.append(limit)
    with ki.open_db(db_path) as conn:
        return list(conn.execute(sql, params))


def write_open_topic_report(jsonl_path: Path, report_path: Path = DEFAULT_REPORT_PATH) -> Path:
    topic_counts: Counter[str] = Counter()
    topic_samples: dict[str, list[int]] = defaultdict(list)
    ai_counts: Counter[str] = Counter()
    content_counts: Counter[str] = Counter()
    total = 0

    if jsonl_path.exists():
        for line in jsonl_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            total += 1
            record_id = int(item.get("id", 0) or 0)
            ai_counts[str(item.get("ai_relevance", "none") or "none")] += 1
            for content_type in as_string_list(item.get("content_types")):
                content_counts[content_type] += 1
            for topic in as_string_list(item.get("suggested_topics")):
                topic_counts[topic] += 1
                if record_id and len(topic_samples[topic]) < 8:
                    topic_samples[topic].append(record_id)

    lines = [
        "# Open Topic Discovery Report",
        "",
        f"Records processed: {total}",
        "",
        "## Suggested Topics",
        "",
    ]
    if topic_counts:
        for topic, count in topic_counts.most_common():
            samples = ", ".join(str(record_id) for record_id in topic_samples[topic])
            lines.append(f"- {topic} ({count}) - samples: {samples}")
    else:
        lines.append("- (none)")

    lines.extend(["", "## AI Relevance", ""])
    lines.extend([f"- {label}: {count}" for label, count in ai_counts.most_common()] or ["- (none)"])
    lines.extend(["", "## Content Types", ""])
    lines.extend([f"- {label}: {count}" for label, count in content_counts.most_common()] or ["- (none)"])
    lines.append("")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def run_discover_record_topics(args: argparse.Namespace, client: Any | None = None) -> int:
    client = client or llm_client.create_client()
    db_path = ki.DB_PATH
    output_path = args.output
    report_path = args.report
    output_path.parent.mkdir(parents=True, exist_ok=True)

    existing_ids = set() if args.force else _load_existing_ids(output_path)
    rows = load_records_for_open_topic_discovery(
        db_path,
        limit=args.limit,
        source=args.source,
        skip_ids=existing_ids,
    )
    annotations = ki.get_record_annotation_map(db_path, [int(row["id"]) for row in rows])

    print(f"model: {MODEL_CLASSIFY}")
    print(f"records: {len(rows)}")
    print(f"output: {output_path}")
    print(f"report: {report_path}")
    if existing_ids and not args.force:
        print(f"skipping existing output ids: {len(existing_ids)}")

    mode = "w" if args.force else "a"
    processed = 0
    errors = 0
    with output_path.open(mode, encoding="utf-8") as handle:
        for row in rows:
            record_id = int(row["id"])
            try:
                result = discover_record_topics(
                    client,
                    row,
                    annotations.get(record_id),
                    dry_run=args.dry_run,
                )
            except ValueError as exc:
                print(f"  parse error: {exc}", file=sys.stderr)
                errors += 1
                break
            except Exception as exc:
                print(f"  error: {format_provider_error(exc)}", file=sys.stderr)
                errors += 1
                break

            if not args.dry_run:
                handle.write(json.dumps(result, ensure_ascii=False, sort_keys=True) + "\n")
                handle.flush()
            topics = ", ".join(result.get("suggested_topics", [])) or "(none)"
            print(f"  [{record_id}] {row['title'][:60]} -> {topics}")
            processed += 1

    if not args.dry_run:
        report = write_open_topic_report(output_path, report_path)
        print(f"report_written: {report}")
    print(f"processed: {processed}")
    print(f"errors: {errors}")
    return 0 if errors == 0 else 1
