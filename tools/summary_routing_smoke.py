#!/usr/bin/env python3
"""Deterministically smoke-test Oracle summary routing without LLM calls."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP_DIR))

import the_analyst  # noqa: E402
from knowledge_indexing import knowledge_index as ki  # noqa: E402


@dataclass(frozen=True)
class Result:
    status: str
    check: str
    group: str
    slug: str
    question: str
    expected: str = ""
    selected: str = ""
    detail: str = ""


def summary_files(summary_dir: Path, group: str) -> list[Path]:
    folder = summary_dir / f"{group}s"
    return sorted(folder.glob("*.md")) if folder.exists() else []


def selected_path(evidence: str) -> str:
    prefixes = ("Selected summary file: ", "Source file: ")
    for line in evidence.splitlines():
        for prefix in prefixes:
            if line.startswith(prefix):
                return line.removeprefix(prefix).strip()
    return ""


def smoke_grouped_summary(
    path: Path,
    group: str,
    state_dir: Path,
    summary_dir: Path,
) -> Result:
    label = path.stem.replace("-", " ")
    question = f"report on {label}"
    evidence = the_analyst.load_summary_files(
        state_dir,
        topic=label,
        summary_dir=summary_dir,
        include_auxiliary=False,
    )
    actual = selected_path(evidence)
    expected = str(path.resolve())
    if actual == expected:
        return Result("pass", "generated", group, path.stem, question, expected, actual)
    return Result(
        "fail",
        "generated",
        group,
        path.stem,
        question,
        expected,
        actual,
        "expected summary was not selected",
    )


def author_index(db_path: Path) -> dict[str, tuple[str, int]]:
    with ki.open_db(db_path) as conn:
        rows = conn.execute(
            """
            SELECT authors.name, COUNT(*) AS records
            FROM authors
            JOIN author_records ON author_records.author_id = authors.id
            GROUP BY authors.id, authors.name
            """
        ).fetchall()
    return {
        the_analyst._topic_slug(row["name"]): (row["name"], int(row["records"]))
        for row in rows
    }


def smoke_author_summary(
    path: Path,
    authors: dict[str, tuple[str, int]],
    db_path: Path,
    summary_dir: Path,
) -> Result:
    match = authors.get(path.stem)
    if not match:
        return Result(
            "fail",
            "generated",
            "author",
            path.stem,
            "",
            str(path.resolve()),
            "",
            "no matching normalized author",
        )
    name, record_count = match
    question = f"what has {name} discussed"
    if record_count < 2:
        return Result(
            "fail",
            "generated",
            "author",
            path.stem,
            question,
            "complete underlying record",
            str(path.resolve()),
            "summary exists for a single-record author and is not used by policy",
        )
    evidence = the_analyst.tool_answer_about_author(
        name,
        db_path=db_path,
        summary_dir=summary_dir,
    )
    expected = f"Source file: {path}"
    if expected in evidence or f"Source file: {path.resolve()}" in evidence:
        return Result(
            "pass",
            "generated",
            "author",
            path.stem,
            question,
            str(path.resolve()),
            str(path.resolve()),
        )
    return Result(
        "fail",
        "generated",
        "author",
        path.stem,
        question,
        str(path.resolve()),
        "",
        "author summary was not selected",
    )


def smoke_curated_case(
    case: dict[str, str],
    state_dir: Path,
    summary_dir: Path,
) -> Result:
    question = case["question"]
    group = case["group"]
    slug = case["slug"]
    expected = (summary_dir / f"{group}s" / f"{slug}.md").resolve()
    evidence = the_analyst.load_summary_files(
        state_dir,
        question=question,
        max_topics=1,
        summary_dir=summary_dir,
        include_auxiliary=False,
    )
    actual = selected_path(evidence)
    if actual == str(expected):
        return Result("pass", "curated", group, slug, question, str(expected), actual)
    return Result(
        "fail",
        "curated",
        group,
        slug,
        question,
        str(expected),
        actual,
        "expected summary was not selected",
    )


def run_smoke(
    db_path: Path,
    summary_dir: Path,
    cases_path: Path,
) -> list[Result]:
    results: list[Result] = []
    for group in ("topic", "source"):
        for path in summary_files(summary_dir, group):
            results.append(smoke_grouped_summary(path, group, ki.STATE_DIR, summary_dir))

    authors = author_index(db_path)
    for path in summary_files(summary_dir, "author"):
        results.append(smoke_author_summary(path, authors, db_path, summary_dir))

    if cases_path.exists():
        cases = json.loads(cases_path.read_text(encoding="utf-8"))
        for case in cases:
            results.append(smoke_curated_case(case, ki.STATE_DIR, summary_dir))
    return results


def archive_stale_author_summaries(
    results: list[Result],
    summary_dir: Path,
) -> tuple[Path | None, int]:
    stale_slugs = {
        result.slug
        for result in results
        if result.group == "author"
        and result.detail == "summary exists for a single-record author and is not used by policy"
    }
    if not stale_slugs:
        return None, 0

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    archive_root = (
        summary_dir / "artifacts" / "authors" / "archive"
        / f"stale-single-record-{timestamp}"
    )
    summary_archive = archive_root / "summaries"
    artifact_archive = archive_root / "artifacts"
    summary_archive.mkdir(parents=True, exist_ok=True)
    artifact_archive.mkdir(parents=True, exist_ok=True)

    moved = 0
    for slug in sorted(stale_slugs):
        summary_path = summary_dir / "authors" / f"{slug}.md"
        if summary_path.exists():
            shutil.move(str(summary_path), str(summary_archive / summary_path.name))
            moved += 1
        for suffix in (".audit.json", ".manifest.json", ".prompt-input.md"):
            artifact_path = summary_dir / "artifacts" / "authors" / f"{slug}{suffix}"
            if artifact_path.exists():
                shutil.move(str(artifact_path), str(artifact_archive / artifact_path.name))
                moved += 1
    return archive_root, moved


def default_log_path() -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    return APP_DIR / "tests" / "logs" / f"summary-routing-smoke-{timestamp}.log"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Smoke-test that Oracle selects every summary for relevant questions."
    )
    parser.add_argument("--db", type=Path, default=ki.DB_PATH)
    parser.add_argument("--summary-dir", type=Path, default=APP_DIR / "summaries")
    parser.add_argument(
        "--cases",
        type=Path,
        default=APP_DIR / "config" / "summary_routing_smoke.json",
    )
    parser.add_argument(
        "--archive-stale-authors",
        action="store_true",
        help="Archive current single-record author summaries that Oracle does not use.",
    )
    parser.add_argument(
        "--log",
        type=Path,
        default=None,
        help="Write complete run output to this log file (default: timestamped file under tests/logs).",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Print only totals and failures; the log still contains every check.",
    )
    args = parser.parse_args(argv)
    args.log = args.log or default_log_path()
    return args


def result_lines(result: Result) -> list[str]:
    lines = [
        f"{result.status.upper()} [{result.check}] {result.group}/{result.slug}",
        f"  question: {result.question or '(none)'}",
        f"  expected: {result.expected or '(none)'}",
        f"  selected: {result.selected or '(none)'}",
    ]
    if result.detail:
        lines.append(f"  detail: {result.detail}")
    return lines


def write_log(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"=== summary routing smoke {timestamp} ===\n")
        handle.write("\n".join(lines))
        handle.write("\n\n")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    results = run_smoke(args.db, args.summary_dir, args.cases)
    archive_lines: list[str] = []
    if args.archive_stale_authors:
        archive_path, moved = archive_stale_author_summaries(results, args.summary_dir)
        archive_lines = [
            f"stale_author_archive: {archive_path or 'none'}",
            f"stale_author_files_moved: {moved}",
        ]
        results = run_smoke(args.db, args.summary_dir, args.cases)
    failures = [result for result in results if result.status == "fail"]

    totals = [
        "summary_routing_smoke:",
        f"  checks: {len(results)}",
        f"  passed: {len(results) - len(failures)}",
        f"  failed: {len(failures)}",
        f"  log: {args.log}",
    ]
    detailed_lines = [
        line
        for result in results
        for line in [*result_lines(result), ""]
    ]
    output_lines = [*archive_lines, *totals, "", *detailed_lines]
    write_log(args.log, output_lines)

    for line in archive_lines:
        print(line)
    for line in totals:
        print(line)
    displayed = failures if args.quiet else results
    if displayed:
        print()
    for result in displayed:
        print("\n".join(result_lines(result)))
        print()
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
