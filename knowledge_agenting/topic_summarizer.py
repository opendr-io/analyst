from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sqlite3
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

load_dotenv()

from knowledge_indexing import knowledge_index as ki
import llm_client
from config import llm_settings
from knowledge_indexing.knowledge_authors import split_authors
from knowledge_indexing.knowledge_db import open_db, utc_now_iso

from .common import MODEL_SUMMARIZE, SUMMARY_CHARS_PER_TOKEN, estimate_tokens


PROMPT_VERSION = "topic-summary-v1"
PROMPT_DIR = Path(__file__).resolve().parent / "prompts"
TOPIC_SUMMARY_USER_PROMPT = PROMPT_DIR / "topic_summary_user.txt"
TOPIC_SUMMARY_SYSTEM_PROMPT = PROMPT_DIR / "topic_summary_system.txt"
DEFAULT_SUMMARY_DIR = Path("summaries")
SUMMARY_CHECK_DIR_NAMES = {
    "summaries-artifact-check",
    "summaries-group-check",
    "summaries-prompt-check",
    "summaries-validation",
}
DEFAULT_INPUT_TOKEN_THRESHOLD = 750_000
DEFAULT_AUTHOR_MIN_RECORDS = 2
RECORD_ID_RE = re.compile(r"\[record_id:(\d+)\]")


@dataclass(frozen=True)
class TopicPaths:
    summary: Path
    audit: Path
    prompt_input: Path
    manifest: Path


@dataclass(frozen=True)
class SummaryGroup:
    group_by: str
    name: str
    label: str
    query: str
    description: str


@dataclass(frozen=True)
class SummaryListing:
    group_by: str
    name: str
    status: str
    records: int | None
    generated_at: str
    summary_path: Path
    manifest_path: Path
    audit_path: Path


def slugify_topic(topic: str) -> str:
    slug = topic.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "topic"


def output_token_target(record_count: int) -> int:
    if record_count <= 10:
        return 3_000
    if record_count <= 50:
        return 8_000
    if record_count <= 100:
        return 15_000
    return 30_000


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_prompt_template(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def render_prompt_template(template: str, values: dict[str, str]) -> str:
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace("{" + key + "}", value)
    return rendered


def file_fingerprint(path: Path) -> dict[str, Any]:
    stat = path.stat()
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return {
        "path": str(path),
        "size_bytes": stat.st_size,
        "mtime_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).replace(microsecond=0).isoformat(),
        "sha256": h.hexdigest(),
    }


def json_list(value: str | None) -> list[str]:
    if not value:
        return []
    try:
        loaded = json.loads(value)
    except json.JSONDecodeError:
        return []
    if not isinstance(loaded, list):
        return []
    return [str(item).strip() for item in loaded if str(item).strip()]


def resolve_summary_dir(path: Path) -> Path:
    if path.parent == Path(".") and path.name in SUMMARY_CHECK_DIR_NAMES:
        return DEFAULT_SUMMARY_DIR / path.name
    return path


def group_summary_dir(summary_dir: Path, group_by: str) -> Path:
    if group_by == "topic":
        return summary_dir / "topics"
    if group_by == "source":
        return summary_dir / "sources"
    if group_by == "author":
        return summary_dir / "authors"
    raise ValueError(f"unknown group_by: {group_by!r}")


def group_artifact_dir(summary_dir: Path, group_by: str) -> Path:
    if group_by == "topic":
        return summary_dir / "artifacts" / "topics"
    if group_by == "source":
        return summary_dir / "artifacts" / "sources"
    if group_by == "author":
        return summary_dir / "artifacts" / "authors"
    raise ValueError(f"unknown group_by: {group_by!r}")


def grouped_paths(summary_dir: Path, group: SummaryGroup) -> TopicPaths:
    slug = slugify_topic(group.name)
    summary_base = group_summary_dir(summary_dir, group.group_by)
    artifact_base = group_artifact_dir(summary_dir, group.group_by)
    return TopicPaths(
        summary=summary_base / f"{slug}.md",
        audit=artifact_base / f"{slug}.audit.json",
        prompt_input=artifact_base / f"{slug}.prompt-input.md",
        manifest=artifact_base / f"{slug}.manifest.json",
    )


def _require_path_within(path: Path, base_dir: Path, label: str) -> Path:
    resolved_base = base_dir.resolve(strict=False)
    resolved_path = path.resolve(strict=False)
    try:
        resolved_path.relative_to(resolved_base)
    except ValueError as exc:
        raise ValueError(f"{label} must stay within summary_dir: {path}") from exc
    return resolved_path


def archive_existing(
    paths: TopicPaths,
    archive_root: Path,
    timestamp: str,
    include_summary: bool = True,
    summary_dir: Path | None = None,
) -> list[str]:
    archived: list[str] = []
    archive_dir = archive_root / timestamp
    containment_root = summary_dir or archive_root.parent.parent.parent
    _require_path_within(archive_dir, containment_root, "archive directory")
    files = [paths.audit, paths.prompt_input, paths.manifest]
    if include_summary:
        files.insert(0, paths.summary)
    for path in files:
        if not path.exists():
            continue
        _require_path_within(path, containment_root, "archive source")
        archive_dir.mkdir(parents=True, exist_ok=True)
        target = archive_dir / path.name
        suffix = 1
        while target.exists():
            target = archive_dir / f"{path.stem}-{suffix}{path.suffix}"
            suffix += 1
        _require_path_within(target, containment_root, "archive target")
        shutil.move(str(path), str(target))
        archived.append(str(target))
    return archived

def run_global_preflight(db_path: Path) -> dict[str, Any]:
    with open_db(db_path) as conn:
        classified = int(conn.execute("SELECT COUNT(*) FROM record_classifications").fetchone()[0])
        missing_agent_topics = [
            int(row["record_id"])
            for row in conn.execute(
                """
                SELECT record_classifications.record_id
                FROM record_classifications
                JOIN records ON records.id = record_classifications.record_id
                WHERE trim(COALESCE(records.agent_topics, '')) = ''
                ORDER BY record_classifications.record_id
                """
            )
        ]
        missing_primary = [
            int(row["record_id"])
            for row in conn.execute(
                """
                SELECT record_id
                FROM record_classifications
                WHERE trim(COALESCE(primary_topic, '')) = ''
                ORDER BY record_id
                """
            )
        ]
        primary_topics_not_in_topics = [
            row["primary_topic"]
            for row in conn.execute(
                """
                SELECT DISTINCT record_classifications.primary_topic
                FROM record_classifications
                LEFT JOIN topics ON topics.name = record_classifications.primary_topic
                WHERE record_classifications.primary_topic != ''
                  AND topics.name IS NULL
                ORDER BY record_classifications.primary_topic
                """
            )
        ]
    result = {
        "classified_records": classified,
        "records_with_empty_agent_topics": missing_agent_topics,
        "records_with_empty_primary_topic": missing_primary,
        "primary_topics_not_in_topics": primary_topics_not_in_topics,
        "ok": not missing_agent_topics and not missing_primary and not primary_topics_not_in_topics,
    }
    if not result["ok"]:
        raise ValueError(f"global preflight failed: {json.dumps(result, ensure_ascii=False)}")
    return result


def list_topics_for_summary(db_path: Path) -> list[str]:
    with open_db(db_path) as conn:
        return [
            row["name"]
            for row in conn.execute(
                """
                SELECT topics.name
                FROM topics
                WHERE EXISTS (
                    SELECT 1
                    FROM records
                    WHERE records.agent_topics LIKE '%|' || topics.name || '|%'
                )
                ORDER BY topics.name
                """
            )
        ]


def list_sources_for_summary(db_path: Path, min_records: int = 1) -> list[str]:
    with open_db(db_path) as conn:
        return [
            row["source"]
            for row in conn.execute(
                """
                SELECT source, COUNT(*) AS records
                FROM records
                GROUP BY source
                HAVING records >= ?
                ORDER BY source
                """,
                (max(1, min_records),),
            )
        ]


def list_authors_for_summary(db_path: Path, min_records: int = 1) -> list[str]:
    with open_db(db_path) as conn:
        return [
            row["name"]
            for row in conn.execute(
                """
                SELECT authors.name, COUNT(*) AS records
                FROM authors
                JOIN author_records ON author_records.author_id = authors.id
                GROUP BY authors.id, authors.name
                HAVING records >= ?
                ORDER BY authors.name COLLATE NOCASE
                """,
                (max(1, min_records),),
            )
        ]


def _record_select_sql() -> str:
    return """
        SELECT
            records.id,
            records.source,
            records.source_file,
            records.source_record_id,
            records.dedupe_key,
            records.title,
            records.author,
            records.text,
            records.url,
            records.event,
            records.year,
            records.tags,
            records.raw_json,
            records.agent_topics,
            records.imported_at,
            record_classifications.primary_topic,
            record_classifications.secondary_topics_json,
            record_classifications.confidence,
            record_classifications.updated_at AS classification_updated_at,
            record_annotations.updated_at AS annotation_updated_at
        FROM records
        LEFT JOIN record_classifications ON record_classifications.record_id = records.id
        LEFT JOIN record_annotations ON record_annotations.record_id = records.id
    """


def load_topic_rows(db_path: Path, topic: str) -> list[sqlite3.Row]:
    pattern = f"%|{topic}|%"
    with open_db(db_path) as conn:
        return list(
            conn.execute(
                _record_select_sql()
                + """
                WHERE records.agent_topics LIKE ?
                ORDER BY records.id
                """,
                (pattern,),
            )
        )


def load_source_rows(db_path: Path, source: str) -> list[sqlite3.Row]:
    with open_db(db_path) as conn:
        return list(
            conn.execute(
                _record_select_sql()
                + """
                WHERE records.source = ?
                ORDER BY records.id
                """,
                (source,),
            )
        )


def load_author_rows(db_path: Path, author: str) -> list[sqlite3.Row]:
    with open_db(db_path) as conn:
        return list(
            conn.execute(
                _record_select_sql()
                + """
                JOIN author_records ON author_records.record_id = records.id
                JOIN authors ON authors.id = author_records.author_id
                WHERE authors.name = ? COLLATE NOCASE
                ORDER BY records.id
                """,
                (author,),
            )
        )


def load_topic_definition(db_path: Path, topic: str) -> dict[str, Any]:
    with open_db(db_path) as conn:
        row = conn.execute(
            "SELECT name, query, description, source, updated_at FROM topics WHERE name = ?",
            (topic,),
        ).fetchone()
    if not row:
        raise ValueError(f"topic not found in topics table: {topic!r}")
    return dict(row)


def topic_table_hash(db_path: Path) -> str:
    with open_db(db_path) as conn:
        rows = [
            dict(row)
            for row in conn.execute(
                "SELECT name, query, description, source, updated_at FROM topics ORDER BY name"
            )
        ]
    return text_hash(json.dumps(rows, ensure_ascii=False, sort_keys=True))


def source_fingerprint(topic: str, records: list[sqlite3.Row], topic_def: dict[str, Any]) -> str:
    payload = {
        "prompt_version": PROMPT_VERSION,
        "topic": topic,
        "topic_definition": topic_def,
        "records": [
            {
                "id": int(row["id"]),
                "dedupe_key": row["dedupe_key"],
                "raw_text_hash": text_hash(row["text"] or ""),
                "agent_topics": row["agent_topics"],
                "primary_topic": row["primary_topic"] or "",
                "secondary_topics_json": row["secondary_topics_json"] or "[]",
                "imported_at": row["imported_at"],
                "annotation_updated_at": row["annotation_updated_at"] or "",
                "classification_updated_at": row["classification_updated_at"] or "",
            }
            for row in records
        ],
    }
    return text_hash(json.dumps(payload, ensure_ascii=False, sort_keys=True))


def format_record(row: sqlite3.Row, topic: str) -> str:
    primary_topic = row["primary_topic"] or ""
    secondary_topics = json_list(row["secondary_topics_json"] or "[]")
    role = "primary" if primary_topic == topic else "secondary"
    parts = [
        f"## [record_id:{int(row['id'])}]",
        f"Source: {row['source']}",
        f"Source record ID: {row['source_record_id']}",
        f"Title: {row['title']}",
        f"Author: {row['author']}",
        f"Event: {row['event']}",
        f"Year: {row['year']}",
        f"URL: {row['url']}",
        f"Tags: {row['tags']}",
        f"Topic membership: {role}",
        f"Primary topic: {primary_topic}",
        f"Secondary topics: {', '.join(secondary_topics)}",
        "",
        "Raw record text:",
        "```text",
        sanitize_raw_record_text(row["text"] or ""),
        "```",
    ]
    return "\n".join(parts).strip()


def sanitize_raw_record_text(text: str) -> str:
    # Keep untrusted source text from polluting deterministic record-ID parsing.
    return re.sub(r"\[record_id:(\d+)\]", r"[source_record_id:\1]", text)


def build_prompt(topic: str, records: list[sqlite3.Row], topic_def: dict[str, Any]) -> str:
    record_ids = [int(row["id"]) for row in records]
    records_text = "\n\n---\n\n".join(format_record(row, topic) for row in records)
    return render_prompt_template(
        load_prompt_template(TOPIC_SUMMARY_USER_PROMPT),
        {
            "topic": topic,
            "topic_query": str(topic_def.get("query", "")),
            "topic_description": str(topic_def.get("description", "")),
            "record_count": str(len(records)),
            "record_ids": ", ".join(str(record_id) for record_id in record_ids),
            "records_text": records_text,
        },
    )


def build_group_prompt(group: SummaryGroup, records: list[sqlite3.Row]) -> str:
    return build_prompt(
        group.label,
        records,
        {
            "query": group.query,
            "description": group.description,
        },
    )


def extract_record_ids(text: str) -> list[int]:
    return [int(match.group(1)) for match in RECORD_ID_RE.finditer(text)]


def compare_ids(expected: list[int], observed: list[int]) -> dict[str, Any]:
    expected_counter = Counter(expected)
    observed_counter = Counter(observed)
    return {
        "missing": sorted(expected_counter.keys() - observed_counter.keys()),
        "unexpected": sorted(observed_counter.keys() - expected_counter.keys()),
        "duplicates": sorted(record_id for record_id, count in observed_counter.items() if count > 1),
        "unique_observed": sorted(observed_counter.keys()),
        "exact": expected_counter == observed_counter,
        "all_expected_present": set(expected_counter) <= set(observed_counter),
    }


def make_summary_group(db_path: Path, group_by: str, name: str) -> SummaryGroup:
    if group_by == "topic":
        topic_def = load_topic_definition(db_path, name)
        return SummaryGroup(
            group_by="topic",
            name=name,
            label=name,
            query=str(topic_def.get("query", "")),
            description=str(topic_def.get("description", "")),
        )
    if group_by == "source":
        return SummaryGroup(
            group_by="source",
            name=name,
            label=f"Source: {name}",
            query=f"All records imported from source {name}.",
            description=(
                f"Research report over all records from source {name}, "
                "summarizing the talks, posts, presentations, and themes present in that source."
            ),
        )
    if group_by == "author":
        return SummaryGroup(
            group_by="author",
            name=name,
            label=f"Author: {name}",
            query=f"All records attributed to author or speaker {name}.",
            description=(
                f"Research report over all records attributed to {name}, "
                "summarizing their talks, posts, presentations, recurring themes, and unique contributions."
            ),
        )
    raise ValueError(f"unknown group_by: {group_by!r}")


def load_group_rows(db_path: Path, group: SummaryGroup) -> list[sqlite3.Row]:
    if group.group_by == "topic":
        return load_topic_rows(db_path, group.name)
    if group.group_by == "source":
        return load_source_rows(db_path, group.name)
    if group.group_by == "author":
        return load_author_rows(db_path, group.name)
    raise ValueError(f"unknown group_by: {group.group_by!r}")


def preflight_group(
    db_path: Path,
    group: SummaryGroup,
    max_input_tokens: int,
) -> tuple[list[sqlite3.Row], dict[str, Any], str, dict[str, Any]]:
    records = load_group_rows(db_path, group)
    if not records:
        raise ValueError(f"no records found for {group.group_by}: {group.name!r}")

    expected_ids = [int(row["id"]) for row in records]
    topic_def = {
        "name": group.label,
        "query": group.query,
        "description": group.description,
        "group_by": group.group_by,
    }
    prompt = build_group_prompt(group, records)
    prompt_ids = extract_record_ids(prompt)
    input_tokens = estimate_tokens(prompt)
    id_check = compare_ids(expected_ids, prompt_ids)
    if not id_check["exact"]:
        raise ValueError(
            "prompt record ID coverage failed "
            f"(missing={id_check['missing']}, unexpected={id_check['unexpected']}, "
            f"duplicates={id_check['duplicates']})"
        )
    if input_tokens >= max_input_tokens:
        largest = sorted(
            (
                {
                    "record_id": int(row["id"]),
                    "title": row["title"],
                    "estimated_tokens": estimate_tokens(format_record(row, group.label)),
                }
                for row in records
            ),
            key=lambda item: item["estimated_tokens"],
            reverse=True,
        )[:10]
        raise ValueError(
            json.dumps(
                {
                    "error": "group exceeds single-pass input threshold; chunking requires user approval",
                    "group_by": group.group_by,
                    "name": group.name,
                    "expected_record_count": len(records),
                    "estimated_input_tokens": input_tokens,
                    "configured_safety_threshold": max_input_tokens,
                    "largest_records_by_token_estimate": largest,
                    "recommended_options": [
                        "increase the threshold",
                        "reduce included fields",
                        "explicitly approve a chunked design",
                    ],
                },
                ensure_ascii=False,
                indent=2,
            )
        )

    primary_ids = [int(row["id"]) for row in records if (row["primary_topic"] or "") == group.name]
    secondary_ids = [int(row["id"]) for row in records if (row["primary_topic"] or "") != group.name]
    preflight = {
        "group_by": group.group_by,
        "group_name": group.name,
        "group_label": group.label,
        "expected_record_count": len(expected_ids),
        "loaded_record_count": len(records),
        "expected_record_ids": expected_ids,
        "prompt_record_ids": sorted(set(prompt_ids)),
        "prompt_record_id_occurrences": len(prompt_ids),
        "prompt_id_check": id_check,
        "primary_record_ids": primary_ids,
        "secondary_record_ids": secondary_ids,
        "estimated_input_tokens": input_tokens,
        "max_input_tokens": max_input_tokens,
        "output_max_tokens": output_token_target(len(records)),
    }
    return records, topic_def, prompt, preflight


def build_system_prompt() -> str:
    return load_prompt_template(TOPIC_SUMMARY_SYSTEM_PROMPT)


def model_for_group(group_by: str) -> str:
    if group_by == "author":
        return llm_settings.get_model("summarize_author")
    return MODEL_SUMMARIZE


def call_summary_model(client: Any, prompt: str, max_tokens: int, model: str = MODEL_SUMMARIZE) -> str:
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=build_system_prompt(),
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()


def repair_missing_ids(
    client: Any,
    topic: str,
    summary: str,
    source_prompt: str,
    missing_ids: list[int],
    max_tokens: int,
    model: str = MODEL_SUMMARIZE,
) -> str:
    missing = ", ".join(f"[record_id:{record_id}]" for record_id in missing_ids)
    prompt = f"""Write a Markdown coverage addendum for the topic summary below.

Topic: {topic}
Missing record IDs: {missing}

Use the source evidence supplied below to discuss every missing record at least once.
Use exact [record_id:1234] citations. Return only an addendum beginning with:

## Coverage Addendum

Do not rewrite, summarize, or repeat the existing report.

Existing report:

{summary}

Source evidence:

{source_prompt}
"""
    addendum = call_summary_model(client, prompt, max_tokens, model=model)
    return f"{summary.rstrip()}\n\n{addendum.lstrip()}"


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_json_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return loaded if isinstance(loaded, dict) else {}


def list_existing_summaries(summary_dir: Path, group_by: str = "topic") -> list[SummaryListing]:
    summary_base = group_summary_dir(summary_dir, group_by)
    artifact_base = group_artifact_dir(summary_dir, group_by)
    listings: list[SummaryListing] = []
    for summary_path in sorted(summary_base.glob("*.md")):
        stem = summary_path.stem
        manifest_path = artifact_base / f"{stem}.manifest.json"
        audit_path = artifact_base / f"{stem}.audit.json"
        manifest = read_json_file(manifest_path)
        audit = read_json_file(audit_path)
        name = str(manifest.get("group_name") or audit.get("group_name") or audit.get("topic") or stem)
        status = str(manifest.get("status") or audit.get("summary_status") or "file_only")
        generated_at = str(manifest.get("generated_at") or audit.get("generated_timestamp") or "")
        records_value = audit.get("expected_record_count")
        try:
            records = int(records_value) if records_value is not None else None
        except (TypeError, ValueError):
            records = None
        listings.append(
            SummaryListing(
                group_by=group_by,
                name=name,
                status=status,
                records=records,
                generated_at=generated_at,
                summary_path=summary_path,
                manifest_path=manifest_path,
                audit_path=audit_path,
            )
        )
    return listings


def print_summary_list(listings: list[SummaryListing]) -> None:
    for item in listings:
        records = "" if item.records is None else str(item.records)
        generated = item.generated_at or ""
        print(f"{item.name}\t{item.status}\t{records}\t{generated}\t{item.summary_path}")
    print(f"summaries: {len(listings)}")


def print_topic_list(topics: list[str]) -> None:
    for topic in topics:
        print(topic)
    print(f"topics: {len(topics)}")


def summarize_group(
    group: SummaryGroup,
    db_path: Path,
    summary_dir: Path,
    max_input_tokens: int = DEFAULT_INPUT_TOKEN_THRESHOLD,
    dry_run: bool = False,
    write_preflight_artifacts: bool = False,
    client: Any | None = None,
) -> dict[str, Any]:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    generated_at = utc_now_iso()
    paths = grouped_paths(summary_dir, group)
    output_dir = group_summary_dir(summary_dir, group.group_by)
    artifact_dir = group_artifact_dir(summary_dir, group.group_by)
    should_write_preflight = (not dry_run) or write_preflight_artifacts
    archived: list[str] = []
    if not dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)
        artifact_dir.mkdir(parents=True, exist_ok=True)
        archived = archive_existing(paths, artifact_dir / "archive", timestamp, include_summary=True, summary_dir=summary_dir)
    elif write_preflight_artifacts:
        artifact_dir.mkdir(parents=True, exist_ok=True)

    global_preflight = run_global_preflight(db_path)
    records, topic_def, prompt, preflight = preflight_group(db_path, group, max_input_tokens)
    expected_ids = preflight["expected_record_ids"]
    topic_hash = topic_table_hash(db_path)
    source_hash = source_fingerprint(group.label, records, topic_def)
    db_fp = file_fingerprint(db_path)
    prompt_hash = text_hash(prompt)
    model = model_for_group(group.group_by)

    manifest = {
        "topic": group.name if group.group_by == "topic" else "",
        "topic_slug": slugify_topic(group.name) if group.group_by == "topic" else "",
        "group_by": group.group_by,
        "group_name": group.name,
        "group_label": group.label,
        "group_slug": slugify_topic(group.name),
        "status": "preflight_complete" if dry_run else "running",
        "model": model,
        "generated_at": generated_at,
        "prompt_version": PROMPT_VERSION,
        "topic_table_snapshot_hash": topic_hash,
        "source_fingerprint": source_hash,
        "database_fingerprint": db_fp,
        "summary_file_path": str(paths.summary),
        "audit_file_path": str(paths.audit),
        "prompt_input_file_path": str(paths.prompt_input),
        "manifest_file_path": str(paths.manifest),
        "archived_paths": archived,
        "artifacts_written": should_write_preflight,
    }
    audit: dict[str, Any] = {
        "topic": group.name if group.group_by == "topic" else "",
        "group_by": group.group_by,
        "group_name": group.name,
        "group_label": group.label,
        "summary_status": "preflight_complete" if dry_run else "running",
        "model": model,
        "generated_timestamp": generated_at,
        "taxonomy_version_or_topic_table_snapshot_hash": topic_hash,
        "prompt_version": PROMPT_VERSION,
        "source_database_path": str(db_path),
        "database_fingerprint": db_fp,
        "source_fingerprint": source_hash,
        "summary_input_artifact_path": str(paths.prompt_input),
        "summary_file_path": str(paths.summary),
        "audit_file_path": str(paths.audit),
        "manifest_file_path": str(paths.manifest),
        "artifacts_written": should_write_preflight,
        "global_preflight": global_preflight,
        **preflight,
    }

    if should_write_preflight:
        paths.prompt_input.write_text(prompt, encoding="utf-8")

    if dry_run:
        if write_preflight_artifacts:
            write_json(paths.audit, audit)
            write_json(paths.manifest, manifest)
        return audit

    client = client or llm_client.create_client()
    max_output_tokens = preflight["output_max_tokens"]
    retry_used = False
    try:
        summary = call_summary_model(client, prompt, max_output_tokens, model=model)
        output_ids = extract_record_ids(summary)
        output_check = compare_ids(expected_ids, output_ids)

        if output_check["missing"]:
            retry_used = True
            summary = repair_missing_ids(
                client,
                group.label,
                summary,
                prompt,
                output_check["missing"],
                max_output_tokens,
                model=model,
            )
            output_ids = extract_record_ids(summary)
            output_check = compare_ids(expected_ids, output_ids)
    except Exception as exc:
        audit.update(
            {
                "summary_status": "failed",
                "error_type": type(exc).__name__,
                "error_message": str(exc),
                "retry_used": retry_used,
            }
        )
        manifest.update(
            {
                "status": "failed",
                "prompt_hash": prompt_hash,
                "summary_storage": "file",
            }
        )
        write_json(paths.audit, audit)
        write_json(paths.manifest, manifest)
        raise

    complete = not output_check["missing"] and not output_check["unexpected"]
    status = "complete" if complete else "incomplete"
    paths.summary.write_text(summary, encoding="utf-8")

    audit.update(
        {
            "summary_status": status,
            "record_ids_found_in_output": sorted(set(output_ids)),
            "output_record_id_occurrences": len(output_ids),
            "missing_output_record_ids": output_check["missing"],
            "duplicate_output_record_ids": output_check["duplicates"],
            "unexpected_output_record_ids": output_check["unexpected"],
            "output_token_estimate": estimate_tokens(summary),
            "output_character_count": len(summary),
            "retry_used": retry_used,
            "summary_hash": text_hash(summary),
        }
    )
    manifest.update(
        {
            "status": status,
            "summary_hash": text_hash(summary),
            "prompt_hash": prompt_hash,
            "summary_storage": "file",
        }
    )

    write_json(paths.audit, audit)
    write_json(paths.manifest, manifest)
    if not complete:
        raise ValueError(
            f"summary incomplete for {group.group_by} {group.name!r}; missing={output_check['missing']} "
            f"unexpected={output_check['unexpected']}; summary file requires review"
        )
    return audit


def summarize_topic(
    topic: str,
    db_path: Path,
    summary_dir: Path,
    max_input_tokens: int = DEFAULT_INPUT_TOKEN_THRESHOLD,
    dry_run: bool = False,
    client: Any | None = None,
) -> dict[str, Any]:
    return summarize_group(
        make_summary_group(db_path, "topic", topic),
        db_path=db_path,
        summary_dir=summary_dir,
        max_input_tokens=max_input_tokens,
        dry_run=dry_run,
        client=client,
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate spec-compliant summaries grouped by topic, source, or author."
    )
    parser.add_argument("--db", type=Path, default=ki.DB_PATH, help="SQLite database path.")
    parser.add_argument(
        "--summary-dir",
        type=Path,
        default=DEFAULT_SUMMARY_DIR,
        help=(
            "Output folder for summary reports and artifacts. Legacy check folders "
            "such as summaries-validation are placed under summaries/."
        ),
    )
    parser.add_argument("--group-by", choices=["topic", "source", "author"], default="topic", help="Record grouping to summarize.")
    parser.add_argument("--topic", action="append", default=[], help="Topic to summarize. Can be passed more than once.")
    parser.add_argument("--source", action="append", default=[], help="Source to summarize. Can be passed more than once.")
    parser.add_argument("--author", action="append", default=[], help="Author to summarize. Can be passed more than once.")
    parser.add_argument("--all", action="store_true", help="Summarize every group with records.")
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip groups whose summary Markdown file already exists.",
    )
    parser.add_argument(
        "--list-summaries",
        action="store_true",
        help="List existing summary Markdown files for the selected group without generating anything.",
    )
    parser.add_argument(
        "--list-missing",
        action="store_true",
        help="List selected groups whose summary Markdown file does not exist without generating anything.",
    )
    parser.add_argument(
        "--list-topics",
        action="store_true",
        help="List topics that have classified records and can be summarized by --all.",
    )
    parser.add_argument(
        "--min-records",
        type=int,
        default=None,
        help="Optional minimum records for --all (defaults: source=1, author=2).",
    )
    parser.add_argument("--dry-run", action="store_true", help="Run preflight without calling the LLM or writing artifacts.")
    parser.add_argument(
        "--write-preflight-artifacts",
        action="store_true",
        help="With --dry-run, write prompt/audit/manifest artifacts without archiving existing files.",
    )
    parser.add_argument("--max-input-tokens", type=int, default=DEFAULT_INPUT_TOKEN_THRESHOLD, help="Single-pass safety threshold.")
    parser.add_argument("--parallel", type=int, default=1, help="Number of summaries to generate concurrently.")
    args = parser.parse_args(argv)
    args.summary_dir = resolve_summary_dir(args.summary_dir)
    return args


def groups_from_args(args: argparse.Namespace) -> list[SummaryGroup]:
    if args.group_by == "topic":
        names = list_topics_for_summary(args.db) if args.all else args.topic
    elif args.group_by == "source":
        minimum = 1 if args.min_records is None else args.min_records
        names = list_sources_for_summary(args.db, min_records=minimum) if args.all else args.source
    elif args.group_by == "author":
        minimum = DEFAULT_AUTHOR_MIN_RECORDS if args.min_records is None else args.min_records
        names = list_authors_for_summary(args.db, min_records=minimum) if args.all else args.author
    else:
        raise ValueError(f"unknown group_by: {args.group_by!r}")
    return [make_summary_group(args.db, args.group_by, name) for name in names]


def filter_existing_groups(summary_dir: Path, groups: list[SummaryGroup]) -> tuple[list[SummaryGroup], list[SummaryGroup]]:
    pending: list[SummaryGroup] = []
    skipped: list[SummaryGroup] = []
    for group in groups:
        if grouped_paths(summary_dir, group).summary.exists():
            skipped.append(group)
        else:
            pending.append(group)
    return pending, skipped


def normalized_parallelism(value: int) -> int:
    return max(1, min(value, 8))


def print_summary_result(audit: dict[str, Any], dry_run: bool) -> None:
    print(f"  status: {audit['summary_status']}")
    print(f"  records: {audit['expected_record_count']}")
    print(f"  estimated_input_tokens: {audit['estimated_input_tokens']}")
    print(f"  output_max_tokens: {audit['output_max_tokens']}")
    print(f"  artifacts_written: {audit['artifacts_written']}")
    print(f"  prompt: {audit['summary_input_artifact_path']}")
    print(f"  audit: {audit['audit_file_path']}")
    if not dry_run:
        print(f"  summary: {audit['summary_file_path']}")


def print_dry_run_totals(audits: list[dict[str, Any]]) -> None:
    input_tokens = sum(int(audit["estimated_input_tokens"]) for audit in audits)
    output_tokens = sum(int(audit["output_max_tokens"]) for audit in audits)
    records = sum(int(audit["expected_record_count"]) for audit in audits)
    print("\ndry_run_totals:")
    print(f"  summaries: {len(audits)}")
    print(f"  records: {records}")
    print(f"  estimated_input_tokens: {input_tokens}")
    print(f"  output_max_tokens: {output_tokens}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.write_preflight_artifacts and not args.dry_run:
        print("--write-preflight-artifacts requires --dry-run", file=sys.stderr)
        return 2
    if args.list_summaries:
        print_summary_list(list_existing_summaries(args.summary_dir, args.group_by))
        return 0
    if args.list_topics:
        if args.group_by != "topic":
            print("--list-topics only applies to --group-by topic", file=sys.stderr)
            return 2
        print_topic_list(list_topics_for_summary(args.db))
        return 0

    groups = groups_from_args(args)
    if args.list_missing:
        missing, _existing = filter_existing_groups(args.summary_dir, groups)
        for group in missing:
            print(f"{group.group_by}\t{group.name}\t{grouped_paths(args.summary_dir, group).summary}")
        print(f"missing: {len(missing)}")
        return 0

    skipped_existing: list[SummaryGroup] = []
    if args.skip_existing:
        groups, skipped_existing = filter_existing_groups(args.summary_dir, groups)
    if not groups:
        if skipped_existing:
            print(f"skipped_existing: {len(skipped_existing)}")
            print("no summaries to generate")
            return 0
        flag = {"topic": "--topic", "source": "--source", "author": "--author"}[args.group_by]
        print(f"specify {flag} VALUE or --all", file=sys.stderr)
        return 2

    print(f"db: {args.db}")
    print(f"summary_dir: {args.summary_dir}")
    print(f"group_by: {args.group_by}")
    print(f"model: {model_for_group(args.group_by)}")
    print(f"dry_run: {args.dry_run}")
    if args.skip_existing:
        print(f"skipped_existing: {len(skipped_existing)}")
    parallel = normalized_parallelism(args.parallel)
    print(f"parallel: {parallel}")

    def run_group(group: SummaryGroup, client: Any | None = None) -> dict[str, Any]:
        return summarize_group(
            group=group,
            db_path=args.db,
            summary_dir=args.summary_dir,
            max_input_tokens=args.max_input_tokens,
            dry_run=args.dry_run,
            write_preflight_artifacts=args.write_preflight_artifacts,
            client=client,
        )

    if parallel == 1:
        client = None if args.dry_run else llm_client.create_client()
        audits: list[dict[str, Any]] = []
        for group in groups:
            print(f"\n{group.group_by}: {group.name}")
            audit = run_group(group, client=client)
            audits.append(audit)
            print_summary_result(audit, args.dry_run)
        if args.dry_run:
            print_dry_run_totals(audits)
        return 0

    failures: list[tuple[SummaryGroup, BaseException]] = []
    audits: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=parallel) as executor:
        futures = {executor.submit(run_group, group): group for group in groups}
        for future in as_completed(futures):
            group = futures[future]
            print(f"\n{group.group_by}: {group.name}")
            try:
                audit = future.result()
            except Exception as exc:
                failures.append((group, exc))
                print(f"  status: failed")
                print(f"  error: {type(exc).__name__}: {exc}")
                continue
            audits.append(audit)
            print_summary_result(audit, args.dry_run)

    if args.dry_run:
        print_dry_run_totals(audits)

    if failures:
        print(f"\nfailed summaries: {len(failures)}", file=sys.stderr)
        for group, exc in failures:
            print(f"  {group.group_by} {group.name}: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
