#!/usr/bin/env python3
"""
Knowledge base classification, annotation, and open-topic agent.

    python -m knowledge_agenting.knowledge_agent classify
    python -m knowledge_agenting.knowledge_agent annotate
    python -m knowledge_agenting.knowledge_agent discover-record-topics
"""

import argparse
import sys
import types
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from knowledge_agenting import common as _common
from knowledge_agenting import classify as _classify
from knowledge_agenting.annotate import annotate_batch, build_annotation_request, format_provider_error, run_annotate
from knowledge_agenting.classify import (
    build_classification_request,
    build_classify_system,
    classify_record,
    get_classification_topics,
    run_classify,
)
from knowledge_agenting.open_topics import (
    DEFAULT_JSONL_PATH,
    DEFAULT_REPORT_PATH,
    OPEN_TOPIC_SYSTEM,
    build_open_topic_request,
    discover_record_topics,
    run_discover_record_topics,
    write_open_topic_report,
)
from knowledge_agenting.common import (
    ANNOTATE_SYSTEM,
    ANNOTATION_DEFAULT_BATCH_SIZE,
    ANNOTATION_MAX_INPUT_TOKENS,
    ANNOTATION_MAX_OUTPUT_TOKENS,
    ANNOTATION_RECORD_CHARS,
    ANNOTATION_SCHEMA_VERSION,
    CLASSIFICATION_DEFAULT_BATCH_SIZE,
    CLASSIFICATION_MAX_INPUT_TOKENS,
    CLASSIFICATION_SCHEMA_VERSION,
    CLASSIFY_SYSTEM,
    MODEL_ANNOTATE,
    MODEL_CLASSIFY,
    SUMMARY_CHARS_PER_TOKEN,
    as_string_list as _as_string_list,
    json_list_text as _json_list_text,
    strip_code_fence as _strip_code_fence,
)
from knowledge_agenting.common import estimate_tokens


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Classify, annotate, and discover topics using the shared LLM client."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    classify_p = sub.add_parser("classify", help="Classify unread records by topic.")
    classify_p.add_argument("--batch-size", type=int, default=CLASSIFICATION_DEFAULT_BATCH_SIZE, help=f"Records per API call (default {CLASSIFICATION_DEFAULT_BATCH_SIZE}).")
    classify_p.add_argument("--limit", type=int, default=0, help="Stop after N records total (0 = all).")
    classify_p.add_argument("--start-id", type=int, default=0, help="Start at this record id when classifying.")
    classify_p.add_argument("--dry-run", action="store_true", help="Print without writing to DB.")

    annotate_p = sub.add_parser("annotate", help="Generate compact per-record summaries and keywords.")
    annotate_p.add_argument("--batch-size", type=int, default=ANNOTATION_DEFAULT_BATCH_SIZE, help=f"Records per API call (default {ANNOTATION_DEFAULT_BATCH_SIZE}).")
    annotate_p.add_argument("--limit", type=int, default=0, help="Stop after N records total (0 = all missing annotations).")
    annotate_p.add_argument("--source", default="", help="Only annotate records from one source.")
    annotate_p.add_argument("--start-id", type=int, default=0, help="Start at this record id when annotating.")
    annotate_p.add_argument("--force", action="store_true", help="Regenerate annotations for records that already have them.")
    annotate_p.add_argument("--reannotate-all", action="store_true", help="Regenerate and upsert annotations for all matching records.")
    annotate_p.add_argument("--dry-run", action="store_true", help="Print without calling the API or writing to DB.")

    open_topic_p = sub.add_parser("discover-record-topics", help="Suggest natural open-ended topics without writing agent_topics.")
    open_topic_p.add_argument("--limit", type=int, default=0, help="Stop after N records total (0 = all annotated records).")
    open_topic_p.add_argument("--source", default="", help="Only process records from one source.")
    open_topic_p.add_argument("--output", type=Path, default=DEFAULT_JSONL_PATH, help=f"JSONL output path (default {DEFAULT_JSONL_PATH}).")
    open_topic_p.add_argument("--report", type=Path, default=DEFAULT_REPORT_PATH, help=f"Markdown report path (default {DEFAULT_REPORT_PATH}).")
    open_topic_p.add_argument("--force", action="store_true", help="Overwrite output instead of resuming/skipping existing record ids.")
    open_topic_p.add_argument("--dry-run", action="store_true", help="Print without calling the API or writing output files.")

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.command == "classify":
        return run_classify(args)
    if args.command == "annotate":
        return run_annotate(args)
    if args.command == "discover-record-topics":
        return run_discover_record_topics(args)
    return 0


class _CompatModule(types.ModuleType):
    _CLASSIFICATION_CONSTANTS = {
        "CLASSIFICATION_MAX_INPUT_TOKENS",
    }

    def __setattr__(self, name: str, value: object) -> None:
        super().__setattr__(name, value)
        if name in self._CLASSIFICATION_CONSTANTS:
            setattr(_common, name, value)
            setattr(_classify, name, value)


sys.modules[__name__].__class__ = _CompatModule


if __name__ == "__main__":
    raise SystemExit(main())
