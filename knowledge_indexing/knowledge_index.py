import argparse
import json
import sqlite3
import sys
from pathlib import Path
from typing import Any

from .knowledge_config import (
    APP_DIR,
    BAD_TOPIC_PHRASES,
    BAD_TOPIC_TOKENS,
    CONFIG_DIR,
    DB_PATH,
    DEFCON33_LATEST,
    LOG_PATH,
    PROMPTORGTFO_LATEST,
    SEED_TOPICS,
    STATE_DIR,
    STOPWORDS,
    SUMMARY_ARCHIVE_DIR,
)
from .knowledge_db import (
    KnowledgeRecord,
    _validate_ident,
    clean_text,
    ensure_column,
    json_dumps,
    log_info,
    log_warning,
    open_db,
    stable_hash,
    utc_now_iso,
)
from .knowledge_imports import (
    default_export_paths,
    detect_export_kind,
    import_exports,
    make_record,
    record_dedupe_key,
    records_from_blackhat,
    records_from_bsideslv,
    records_from_camlis,
    records_from_defcon,
    records_from_export,
    records_from_promptorgtfo,
    records_from_rsac,
    records_from_youtube_playlist,
    upsert_record,
)
from .knowledge_records import (
    clear_record_annotation_error,
    clear_record_classification_error,
    decode_topics,
    encode_topics,
    get_record_annotation_map,
    list_record_annotations,
    list_record_annotation_errors,
    list_record_classifications,
    list_record_classification_errors,
    list_records_for_topic,
    list_records_missing_annotations,
    list_records_missing_classifications,
    list_unread_records,
    mark_records_read,
    search_records,
    set_record_topics,
    store_record_classification,
    store_record_classification_error,
    store_record_annotation,
    store_record_annotation_error,
)
from .knowledge_topics import (
    discover_topic_candidates,
    export_topic_keyword_candidates,
    export_topic_list,
    list_classification_topics,
    phrase_candidates,
    refresh_topic_catalog,
    seed_topics,
    store_topic_candidates,
    tokens_for_topics,
)

def log_warning(msg: str) -> None:
    entry = f"{utc_now_iso()} [WARNING] {msg}\n"
    print(msg, file=sys.stderr)
    try:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with LOG_PATH.open("a", encoding="utf-8") as fh:
            fh.write(entry)
    except OSError:
        pass


def log_info(msg: str) -> None:
    entry = f"{utc_now_iso()} [INFO] {msg}\n"
    try:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with LOG_PATH.open("a", encoding="utf-8") as fh:
            fh.write(entry)
    except OSError:
        pass


def print_topic_candidates(candidates: list[dict[str, Any]]) -> None:
    for idx, candidate in enumerate(candidates, start=1):
        sources = ", ".join(candidate["sources"])
        samples = ", ".join(str(record_id) for record_id in candidate["sample_record_ids"])
        safe_print(
            f"{idx}. {candidate['phrase']} "
            f"(records={candidate['record_count']}, sources={sources}, samples={samples})"
        )


def print_search_results(rows: list[sqlite3.Row]) -> None:
    for row in rows:
        snippet = clean_text(row["text"])[:240]
        state = "read" if row["agent_read"] else "unread"
        safe_print(f"[{row['id']}] {row['source']} {row['year']} [{state}] {row['title']}")
        if row["author"]:
            safe_print(f"  author: {row['author']}")
        if row["url"]:
            safe_print(f"  url: {row['url']}")
        topics = decode_topics(row["agent_topics"])
        if topics:
            safe_print(f"  topics: {', '.join(topics)}")
        if snippet:
            safe_print(f"  {snippet}")


def _json_preview(value: str, limit: int = 8) -> str:
    if not value:
        return ""
    try:
        loaded = json.loads(value)
    except json.JSONDecodeError:
        return value[:240]
    if isinstance(loaded, list):
        return ", ".join(str(item) for item in loaded[:limit])
    return str(loaded)[:240]


def print_annotation_results(rows: list[sqlite3.Row]) -> None:
    for row in rows:
        safe_print(f"[{row['record_id']}] {row['source']} {row['year']} {row['title']}")
        if row["author"]:
            safe_print(f"  author: {row['author']}")
        if row["url"]:
            safe_print(f"  url: {row['url']}")
        topics = decode_topics(row["agent_topics"])
        if topics:
            safe_print(f"  topics: {', '.join(topics)}")
        if "updated_at" in row.keys():
            safe_print(f"  annotation updated: {row['updated_at']} ({row['model']}, schema {row['schema_version']})")
        safe_print(f"  annotation: {row['short_summary']}")
        for label, column in [
            ("keywords", "keywords_json"),
            ("tools", "tools_json"),
            ("people", "people_json"),
            ("claims", "claims_json"),
            ("use cases", "use_cases_json"),
            ("content types", "content_types_json"),
            ("security domains", "security_domains_json"),
        ]:
            preview = _json_preview(row[column])
            if preview:
                safe_print(f"  {label}: {preview}")
        if "ai_relevance" in row.keys() and row["ai_relevance"]:
            safe_print(f"  ai relevance: {row['ai_relevance']}")
        if "contains_prompt_injection" in row.keys() and row["contains_prompt_injection"]:
            safe_print("  contains prompt injection: yes")
        if "relevance_notes" in row.keys() and row["relevance_notes"]:
            safe_print(f"  relevance notes: {row['relevance_notes']}")
        raw = clean_text(row["text"])[:320]
        if raw:
            safe_print(f"  raw excerpt: {raw}")
        safe_print("")


def print_annotation_error_results(rows: list[sqlite3.Row]) -> None:
    for row in rows:
        safe_print(f"[{row['record_id']}] {row['source']} {row['title']}")
        safe_print(
            f"  attempts: {row['attempts']} "
            f"first: {row['first_seen_at']} last: {row['last_seen_at']}"
        )
        safe_print(f"  model: {row['model']}")
        safe_print(f"  error: {row['error_type']}: {row['error_message']}")
        safe_print("")


def print_classification_results(rows: list[sqlite3.Row]) -> None:
    for row in rows:
        secondary = _json_preview(row["secondary_topics_json"])
        safe_print(f"[{row['record_id']}] {row['source']} {row['title']}")
        safe_print(f"  classification updated: {row['updated_at']} ({row['model']}, schema {row['schema_version']})")
        safe_print(f"  primary: {row['primary_topic']}")
        if secondary:
            safe_print(f"  secondary: {secondary}")
        safe_print(f"  confidence: {row['confidence']}")
        if row["new_topic_candidate"]:
            safe_print(f"  new topic candidate: {row['new_topic_candidate']}")
        if row["rationale"]:
            safe_print(f"  rationale: {row['rationale']}")
        safe_print("")


def print_classification_error_results(rows: list[sqlite3.Row]) -> None:
    for row in rows:
        safe_print(f"[{row['record_id']}] {row['source']} {row['title']}")
        safe_print(
            f"  attempts: {row['attempts']} "
            f"first: {row['first_seen_at']} last: {row['last_seen_at']}"
        )
        safe_print(f"  model: {row['model']}")
        safe_print(f"  error: {row['error_type']}: {row['error_message']}")
        safe_print("")


def safe_print(value: str) -> None:
    encoding = sys.stdout.encoding or "utf-8"
    sys.stdout.write(value.encode(encoding, errors="replace").decode(encoding, errors="replace") + "\n")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build and search the local knowledge SQLite index.")
    parser.add_argument("--db", type=Path, default=DB_PATH, help="SQLite database path.")
    parser.add_argument("--import-json", type=Path, nargs="*", help="JSON export files to import.")
    parser.add_argument("--import-dir", type=Path, action="append", help="Import every JSON export file in a directory.")
    parser.add_argument("--all-exports", action="store_true", help="Import every known JSON export instead of only latest per source.")
    parser.add_argument("--rebuild", action="store_true", help="Clear existing records before importing.")
    parser.add_argument("--query", help="Search query using SQLite FTS5 syntax.")
    parser.add_argument("--limit", type=int, default=10, help="Maximum search results.")
    parser.add_argument("--unread", action="store_true", help="Only search records where agent_read = 0.")
    parser.add_argument("--list-unread", action="store_true", help="List unread records for agent processing.")
    parser.add_argument("--record-source", default="", help="Filter unread record listing to one source.")
    parser.add_argument("--mark-read", type=int, nargs="*", help="Mark record ids as read.")
    parser.add_argument("--mark-unread", type=int, nargs="*", help="Mark record ids as unread.")
    parser.add_argument("--reader", default="agent", help="Reader name for --mark-read.")
    parser.add_argument("--notes", default="", help="Notes to store with --mark-read.")
    parser.add_argument("--discover-topics", action="store_true", help="Discover recurring candidate topics from indexed records.")
    parser.add_argument("--min-topic-records", type=int, default=3, help="Minimum records for a discovered topic candidate.")
    parser.add_argument("--topic-source", default="", help="Limit topic discovery to one source.")
    parser.add_argument("--store-topics", action="store_true", help="Store discovered candidates in topic_candidates.")
    parser.add_argument("--seed-topics", action="store_true", help="Store a small curated starter topic taxonomy.")
    parser.add_argument("--export-topic-list", type=Path, nargs="?", const=STATE_DIR / "topic-list.txt", help="Write topics and discovered candidates to a text file.")
    parser.add_argument("--export-topic-keywords", type=Path, nargs="?", const=STATE_DIR / "topic-keyword-candidates.md", help="Write annotation-derived keyword candidates for curated topics.")
    parser.add_argument("--set-record-topics", type=int, metavar="RECORD_ID", help="Set topic classifications for a record and mark it read.")
    parser.add_argument("--topics", default="", help="Comma-separated topic names for --set-record-topics.")
    parser.add_argument("--list-topic-records", metavar="TOPIC_NAME", help="List all records classified under a topic.")
    parser.add_argument("--list-annotations", action="store_true", help="List generated record annotations for quality review.")
    parser.add_argument("--latest-annotations", action="store_true", help="List the most recently updated record annotations for quality review.")
    parser.add_argument("--annotation-source", default="", help="Filter annotation listing to one source.")
    parser.add_argument("--annotation-query", default="", help="Filter annotation listing by text, keyword, tool, or claim.")
    parser.add_argument("--list-annotation-errors", action="store_true", help="List durable annotation errors.")
    parser.add_argument("--list-classifications", action="store_true", help="List generated record classifications for review.")
    parser.add_argument("--low-confidence-classifications", action="store_true", help="List low-confidence record classifications.")
    parser.add_argument("--new-topic-candidates", action="store_true", help="List classifier-proposed new topic candidates.")
    parser.add_argument("--list-classification-errors", action="store_true", help="List durable classification errors.")
    return parser.parse_args(argv)


def import_paths_from_args(args: argparse.Namespace) -> list[Path]:
    paths: list[Path] = []
    if args.import_json is not None:
        paths.extend(args.import_json)
    for folder in args.import_dir or []:
        if folder.exists() and folder.is_dir():
            paths.extend(sorted(folder.glob("*.json")))
        else:
            paths.append(folder)
    if paths:
        return paths
    return default_export_paths(latest_per_source=not args.all_exports)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.import_json is not None or args.import_dir or args.rebuild or args.all_exports:
        paths = import_paths_from_args(args)
        stats = import_exports(paths, db_path=args.db, rebuild=args.rebuild)
        print(f"db: {args.db}")
        print(f"files: {stats['files']}")
        print(f"records_seen: {stats['records']}")
        print(f"inserted: {stats['inserted']}")
        print(f"updated: {stats['updated']}")
        print(f"skipped_files: {stats['skipped_files']}")
        if stats["errors"]:
            print(f"errors: {stats['errors']} (see {LOG_PATH})")
    if args.query:
        rows = search_records(args.db, args.query, args.limit, unread=args.unread)
        print_search_results(rows)
        print(f"results: {len(rows)}")
    if args.list_unread:
        rows = list_unread_records(args.db, limit=args.limit, source=args.record_source)
        print_search_results(rows)
        print(f"unread_results: {len(rows)}")
    if args.mark_read is not None:
        count = mark_records_read(args.db, args.mark_read, read=True, reader=args.reader, notes=args.notes)
        print(f"marked_read: {count}")
    if args.mark_unread is not None:
        count = mark_records_read(args.db, args.mark_unread, read=False)
        print(f"marked_unread: {count}")
    if args.discover_topics:
        candidates = discover_topic_candidates(
            args.db,
            limit=args.limit,
            min_records=args.min_topic_records,
            source=args.topic_source,
        )
        if args.store_topics:
            store_topic_candidates(args.db, candidates)
        print_topic_candidates(candidates)
        print(f"topic_candidates: {len(candidates)}")
    if args.seed_topics:
        count = seed_topics(args.db)
        print(f"seed_topics: {count}")
    if args.export_topic_list:
        path = export_topic_list(args.db, args.export_topic_list)
        print(f"topic_list: {path}")
    if args.export_topic_keywords:
        path = export_topic_keyword_candidates(args.db, args.export_topic_keywords)
        print(f"topic_keywords: {path}")
    if args.set_record_topics is not None:
        topics_list = [t.strip() for t in args.topics.split(",") if t.strip()] if args.topics else []
        ok = set_record_topics(args.db, args.set_record_topics, topics_list, reader=args.reader, notes=args.notes)
        print(f"record_id: {args.set_record_topics}")
        print(f"topics_set: {', '.join(topics_list) or '(none)'}")
        print(f"updated: {ok}")
    if args.list_topic_records:
        rows = list_records_for_topic(args.db, args.list_topic_records, limit=args.limit)
        print_search_results(rows)
        print(f"results: {len(rows)}")
    if args.list_annotations or args.latest_annotations:
        rows = list_record_annotations(
            args.db,
            limit=args.limit,
            source=args.annotation_source,
            query=args.annotation_query,
            latest=args.latest_annotations,
        )
        print_annotation_results(rows)
        print(f"annotations: {len(rows)}")
    if args.list_annotation_errors:
        rows = list_record_annotation_errors(args.db, limit=args.limit)
        print_annotation_error_results(rows)
        print(f"annotation_errors: {len(rows)}")
    if args.list_classifications or args.low_confidence_classifications or args.new_topic_candidates:
        rows = list_record_classifications(
            args.db,
            limit=args.limit,
            low_confidence=args.low_confidence_classifications,
            new_topic_candidates=args.new_topic_candidates,
        )
        print_classification_results(rows)
        print(f"classifications: {len(rows)}")
    if args.list_classification_errors:
        rows = list_record_classification_errors(args.db, limit=args.limit)
        print_classification_error_results(rows)
        print(f"classification_errors: {len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
