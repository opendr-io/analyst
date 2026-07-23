#!/usr/bin/env python3
"""Audit imported record counts against local source artifacts."""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

APP_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP_DIR))

from knowledge_indexing.knowledge_config import DB_PATH  # noqa: E402
from knowledge_indexing.knowledge_imports import records_from_export  # noqa: E402


@dataclass(frozen=True)
class SourceSpec:
    source: str
    path_getter: Callable[[Path], Path | None]
    kind: str = "json"


@dataclass(frozen=True)
class AuditRow:
    source: str
    db_count: int
    expected_count: int | None
    raw_count: int | None
    status: str
    path: str
    note: str = ""


def latest(pattern: str) -> Callable[[Path], Path | None]:
    def _get(root: Path) -> Path | None:
        matches = sorted(root.glob(pattern))
        return matches[-1] if matches else None

    return _get


def fixed(relative_path: str) -> Callable[[Path], Path | None]:
    def _get(root: Path) -> Path | None:
        path = root / relative_path
        return path if path.exists() else None

    return _get


SOURCE_SPECS = [
    SourceSpec("blackhat", latest("data/blackhat/exports/blackhat-talks-*.json")),
    SourceSpec("camlis", latest("data/camlis/exports/camlis-talks-*.json")),
    SourceSpec("bsideslv", latest("ingesters/data/bsideslv/exports/bsideslv-talks-*.json")),
    SourceSpec("defcon33", fixed("youtube_summaries/defcon33/defcon33_latest.json")),
    SourceSpec("promptorgtfo", latest("youtube_summaries/promptorgtfo_*.json")),
    SourceSpec("unprompted2026", fixed("youtube_summaries/unprompted2026/unprompted2026_latest.json")),
]


def db_counts(db_path: Path) -> dict[str, int]:
    with sqlite3.connect(db_path) as conn:
        return {
            source: count
            for source, count in conn.execute(
                "SELECT source, COUNT(*) FROM records GROUP BY source ORDER BY source"
            )
        }


def raw_json_count(path: Path) -> int | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if isinstance(data, list):
        return len(data)
    if isinstance(data, dict):
        for key in ("talks", "records"):
            value = data.get(key)
            if isinstance(value, list):
                return len(value)
        count = data.get("count") or data.get("talk_count")
        return int(count) if isinstance(count, int) else None
    return None


def source_expected_count(spec: SourceSpec, path: Path) -> tuple[int | None, int | None, str]:
    records = records_from_export(path)
    if not records:
        return None, raw_json_count(path), "0 parser records"
    unique = len({record.dedupe_key for record in records if record.source == spec.source})
    if unique == 0:
        unique = len({record.dedupe_key for record in records})
    raw_count = raw_json_count(path)
    note = "parser unique dedupe count"
    if raw_count is not None and raw_count != unique:
        note += f"; raw artifact count {raw_count}"
    return unique, raw_count, note


def audit_sources(root: Path = APP_DIR, db_path: Path = DB_PATH) -> list[AuditRow]:
    counts = db_counts(db_path)
    rows: list[AuditRow] = []
    seen_sources: set[str] = set()

    for spec in SOURCE_SPECS:
        seen_sources.add(spec.source)
        path = spec.path_getter(root)
        db_count = counts.get(spec.source, 0)
        if not path:
            rows.append(AuditRow(spec.source, db_count, None, None, "missing-source", ""))
            continue
        expected, raw_count, note = source_expected_count(spec, path)
        if expected is None:
            status = "unreadable-source"
        elif db_count == expected:
            status = "ok"
        else:
            status = "mismatch"
        rows.append(
            AuditRow(
                source=spec.source,
                db_count=db_count,
                expected_count=expected,
                raw_count=raw_count,
                status=status,
                path=str(path.relative_to(root) if path.is_relative_to(root) else path),
                note=note,
            )
        )

    for source, count in sorted(counts.items()):
        if source not in seen_sources:
            rows.append(AuditRow(source, count, None, None, "db-only", "", "no configured source artifact"))
    return rows


def format_table(rows: list[AuditRow]) -> str:
    headers = ["source", "db", "expected", "raw", "status", "artifact", "note"]
    body = [
        [
            row.source,
            str(row.db_count),
            "" if row.expected_count is None else str(row.expected_count),
            "" if row.raw_count is None else str(row.raw_count),
            row.status,
            row.path,
            row.note,
        ]
        for row in rows
    ]
    widths = [len(header) for header in headers]
    for record in body:
        for idx, value in enumerate(record):
            widths[idx] = max(widths[idx], len(value))
    lines = ["  ".join(header.ljust(widths[idx]) for idx, header in enumerate(headers))]
    lines.append("  ".join("-" * width for width in widths))
    lines.extend("  ".join(value.ljust(widths[idx]) for idx, value in enumerate(record)) for record in body)
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit DB record counts against local source artifacts.")
    parser.add_argument("--db", type=Path, default=DB_PATH, help="SQLite knowledge DB path.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when any source mismatches or is missing.")
    args = parser.parse_args(argv)

    rows = audit_sources(db_path=args.db)
    if args.json:
        print(json.dumps([row.__dict__ for row in rows], indent=2))
    else:
        print(format_table(rows))

    bad = [row for row in rows if row.status not in {"ok"}]
    return 1 if args.strict and bad else 0


if __name__ == "__main__":
    raise SystemExit(main())