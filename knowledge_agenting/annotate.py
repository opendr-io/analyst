import argparse
import json
import sys
from collections.abc import Mapping
from typing import Any

from knowledge_indexing import knowledge_index as ki
import llm_client

from .common import (
    ANNOTATE_SYSTEM,
    ANNOTATION_MAX_INPUT_TOKENS,
    ANNOTATION_MAX_OUTPUT_TOKENS,
    ANNOTATION_RECORD_CHARS,
    ANNOTATION_SCHEMA_VERSION,
    MODEL_ANNOTATE,
    as_string_list,
    estimate_tokens,
    strip_code_fence,
)

ANNOTATION_TEXT_FORMAT = {
    "format": {
        "type": "json_schema",
        "name": "record_annotations",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "annotations": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "summary": {"type": "string"},
                            "keywords": {"type": "array", "items": {"type": "string"}},
                            "tools": {"type": "array", "items": {"type": "string"}},
                            "people": {"type": "array", "items": {"type": "string"}},
                            "claims": {"type": "array", "items": {"type": "string"}},
                            "use_cases": {"type": "array", "items": {"type": "string"}},
                            "ai_relevance": {
                                "type": "string",
                                "enum": [
                                    "none",
                                    "about_ai_security",
                                    "ai_assisted_security",
                                    "ai_tooling_for_security",
                                    "ai_model_research",
                                    "generic_ai_not_security",
                                ],
                            },
                            "content_types": {
                                "type": "array",
                                "items": {
                                    "type": "string",
                                    "enum": [
                                        "research",
                                        "tooling",
                                        "practitioner_report",
                                        "vendor_product",
                                        "training_resource",
                                        "news",
                                        "opinion",
                                        "funding",
                                        "other",
                                    ],
                                },
                            },
                            "security_domains": {"type": "array", "items": {"type": "string"}},
                            "contains_prompt_injection": {"type": "boolean"},
                            "relevance_notes": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "summary",
                            "keywords",
                            "tools",
                            "people",
                            "claims",
                            "use_cases",
                            "ai_relevance",
                            "content_types",
                            "security_domains",
                            "contains_prompt_injection",
                            "relevance_notes",
                        ],
                        "additionalProperties": False,
                    },
                }
            },
            "required": ["annotations"],
            "additionalProperties": False,
        },
    }
}


def _annotation_text(row: object) -> str:
    text = row["text"]
    if ANNOTATION_RECORD_CHARS and ANNOTATION_RECORD_CHARS > 0:
        return text[:ANNOTATION_RECORD_CHARS]
    return text


def build_annotation_request(records: list) -> tuple[list[dict], str, int]:
    payload = [
        {
            "id": r["id"],
            "source": r["source"],
            "title": r["title"],
            "author": r["author"],
            "event": r["event"],
            "year": r["year"],
            "tags": r["tags"],
            "topics": ki.decode_topics(r["agent_topics"]),
            "text": _annotation_text(r),
        }
        for r in records
    ]
    content = f"Annotate these {len(records)} records:\n\n{json.dumps(payload, ensure_ascii=False, indent=2)}"
    input_tokens = estimate_tokens(ANNOTATE_SYSTEM) + estimate_tokens(content)
    return payload, content, input_tokens


def annotate_batch(
    client: Any,
    records: list,
    dry_run: bool = False,
) -> list[dict]:
    if not records:
        return []
    _payload, content, input_tokens = build_annotation_request(records)
    if input_tokens > ANNOTATION_MAX_INPUT_TOKENS:
        record_ids = [int(r["id"]) for r in records]
        raise ValueError(
            "annotation input exceeds max token budget "
            f"({input_tokens} estimated tokens > {ANNOTATION_MAX_INPUT_TOKENS}); "
            f"record_ids={record_ids}"
        )
    if dry_run:
        print(
            f"  [dry-run] would annotate {len(records)} records with {MODEL_ANNOTATE} "
            f"({input_tokens} estimated input tokens)"
        )
        return [
            {
                "id": r["id"],
                "summary": "",
                "keywords": [],
                "tools": [],
                "people": [],
                "claims": [],
                "use_cases": [],
                "contains_prompt_injection": False,
            }
            for r in records
        ]

    response = client.messages.create(
        model=MODEL_ANNOTATE,
        max_tokens=ANNOTATION_MAX_OUTPUT_TOKENS,
        system=[
            {
                "type": "text",
                "text": ANNOTATE_SYSTEM,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        text=ANNOTATION_TEXT_FORMAT,
    )
    raw = strip_code_fence(response.content[0].text)
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"model returned invalid annotation JSON: {exc} | raw: {raw[:200]}") from exc
    if isinstance(parsed, dict) and isinstance(parsed.get("annotations"), list):
        return parsed["annotations"]
    if isinstance(parsed, list):
        return parsed
    raise ValueError(f"model returned unexpected annotation JSON shape: {raw[:200]}")


def format_provider_error(exc: Exception) -> str:
    parts = [f"{type(exc).__name__}: {exc}"]
    for attr in ("status_code", "code", "type", "request_id"):
        value = getattr(exc, attr, None)
        if value:
            parts.append(f"{attr}={value}")
    response = getattr(exc, "response", None)
    if response is not None:
        status_code = getattr(response, "status_code", None)
        if status_code:
            parts.append(f"response_status={status_code}")
        request_id = getattr(response, "headers", {}).get("x-request-id") if hasattr(response, "headers") else None
        if request_id:
            parts.append(f"response_request_id={request_id}")
        response_body = ""
        try:
            response_json = response.json()
        except Exception:
            response_json = None
        if response_json:
            response_body = json.dumps(response_json, ensure_ascii=False)
        else:
            response_body = str(getattr(response, "text", "") or "")
        if response_body:
            parts.append(f"response_body={response_body[:2000]}")
    body = getattr(exc, "body", None)
    if body:
        if isinstance(body, Mapping):
            body_text = json.dumps(dict(body), ensure_ascii=False)
        else:
            body_text = str(body)
        parts.append(f"body={body_text[:2000]}")
    return " | ".join(parts)


def run_annotate(args: argparse.Namespace, client: Any | None = None) -> int:
    client = client or llm_client.create_client()
    db_path = ki.DB_PATH

    total_attempted = 0
    total_annotated = 0
    total_errors = 0
    skipped_record_ids: set[int] = set()

    print(f"model: {MODEL_ANNOTATE}")
    print(f"batch_size: {args.batch_size}")
    print(f"max_input_tokens: {ANNOTATION_MAX_INPUT_TOKENS}")
    print("record_text: full" if not ANNOTATION_RECORD_CHARS else f"record_text_chars: {ANNOTATION_RECORD_CHARS}")
    reannotate_all = bool(getattr(args, "reannotate_all", False) or getattr(args, "force", False))
    start_id = int(getattr(args, "start_id", 0) or 0)
    if start_id:
        print(f"start_id: {start_id}")
    print("mode: reannotate all matching records" if reannotate_all else "mode: annotate missing records")

    while True:
        if args.limit and total_attempted >= args.limit:
            print(f"reached --limit {args.limit}, stopping")
            break

        fetch_limit = args.batch_size
        if args.limit:
            fetch_limit = min(fetch_limit, args.limit - total_attempted)

        if reannotate_all:
            with ki.open_db(db_path) as conn:
                sql = "SELECT * FROM records"
                params: list[str | int] = []
                where: list[str] = []
                if args.source:
                    where.append("source = ?")
                    params.append(args.source)
                if start_id:
                    where.append("id >= ?")
                    params.append(start_id)
                if where:
                    sql += " WHERE " + " AND ".join(where)
                sql += " ORDER BY id LIMIT ? OFFSET ?"
                params.extend([fetch_limit, total_attempted])
                rows = list(conn.execute(sql, params))
        else:
            lookup_limit = fetch_limit + len(skipped_record_ids)
            rows = [
                row
                for row in ki.list_records_missing_annotations(
                    db_path,
                    limit=lookup_limit,
                    source=args.source,
                    start_id=start_id,
                )
                if int(row["id"]) not in skipped_record_ids
            ][:fetch_limit]

        if not rows:
            print("no more records needing annotation")
            break

        print(f"\nbatch {total_attempted // args.batch_size + 1}: {len(rows)} records")
        try:
            annotations = annotate_batch(client, rows, dry_run=args.dry_run)
        except ValueError as exc:
            error_message = str(exc)
            print(f"  parse error: {error_message}", file=sys.stderr)
            total_errors += len(rows)
            skipped_record_ids.update(int(row["id"]) for row in rows)
            if not args.dry_run:
                for row in rows:
                    ki.store_record_annotation_error(
                        db_path,
                        record_id=int(row["id"]),
                        model=MODEL_ANNOTATE,
                        error_type=type(exc).__name__,
                        error_message=error_message,
                    )
            total_attempted += len(rows)
            continue
        except Exception as exc:
            error_message = format_provider_error(exc)
            print(f"  error: {error_message}", file=sys.stderr)
            total_errors += len(rows)
            skipped_record_ids.update(int(row["id"]) for row in rows)
            if not args.dry_run:
                for row in rows:
                    ki.store_record_annotation_error(
                        db_path,
                        record_id=int(row["id"]),
                        model=MODEL_ANNOTATE,
                        error_type=type(exc).__name__,
                        error_message=error_message,
                    )
            total_attempted += len(rows)
            continue

        by_id = {}
        for item in annotations:
            try:
                by_id[int(item["id"])] = item
            except (KeyError, TypeError, ValueError):
                total_errors += 1

        for row in rows:
            record_id = int(row["id"])
            item = by_id.get(record_id)
            if not item:
                total_errors += 1
                continue
            summary = str(item.get("summary", "")).strip()
            keywords = as_string_list(item.get("keywords"))
            if not args.dry_run:
                ki.store_record_annotation(
                    db_path,
                    record_id=record_id,
                    short_summary=summary,
                    keywords=keywords,
                    tools=as_string_list(item.get("tools")),
                    people=as_string_list(item.get("people")),
                    claims=as_string_list(item.get("claims")),
                    use_cases=as_string_list(item.get("use_cases")),
                    ai_relevance=str(item.get("ai_relevance", "")).strip(),
                    content_types=as_string_list(item.get("content_types")),
                    security_domains=as_string_list(item.get("security_domains")),
                    contains_prompt_injection=bool(item.get("contains_prompt_injection", False)),
                    relevance_notes=str(item.get("relevance_notes", "")).strip(),
                    raw=item,
                    model=MODEL_ANNOTATE,
                    schema_version=ANNOTATION_SCHEMA_VERSION,
                )
                ki.clear_record_annotation_error(db_path, record_id)
            title_short = (row["title"] or "")[:60]
            label = ", ".join(keywords[:5]) if keywords else "(no keywords)"
            ki.safe_print(f"  [{record_id}] {title_short} -> {label}")
            total_attempted += 1
            total_annotated += 1

    print(f"\nannotated: {total_annotated}")
    print(f"attempted: {total_attempted}")
    print(f"errors: {total_errors}")
    if skipped_record_ids:
        skipped = ", ".join(str(record_id) for record_id in sorted(skipped_record_ids))
        print(f"skipped_record_ids: {skipped}")
    return 0 if total_errors == 0 else 1
