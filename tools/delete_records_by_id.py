#!/usr/bin/env python3
"""
Delete records and dependent rows from knowledge.sqlite3 by record id.

Default behavior is a dry run. Pass --apply to commit.

Examples:
    python delete_records_by_id.py --ids-file linkedin_saved_record_ids.txt
    python delete_records_by_id.py --ids-file linkedin_saved_record_ids.txt --apply
"""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


DEFAULT_DB = Path("knowledge") / "knowledge.sqlite3"

CHILD_TABLES = [
    "record_annotation_errors",
    "record_annotations",
    "record_classification_errors",
    "record_classifications",
]


def parse_ids(path: Path) -> list[int]:
    ids: list[int] = []
    seen: set[int] = set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        value = line.strip()
        if not value:
            continue
        try:
            record_id = int(value)
        except ValueError as exc:
            raise ValueError(f"{path}:{line_number}: invalid record id {value!r}") from exc
        if record_id not in seen:
            ids.append(record_id)
            seen.add(record_id)
    return ids


def placeholders(ids: list[int]) -> str:
    return ", ".join("?" for _ in ids)


def count_rows(conn: sqlite3.Connection, table: str, column: str, ids: list[int]) -> int:
    if not ids:
        return 0
    sql = f"SELECT COUNT(*) FROM {table} WHERE {column} IN ({placeholders(ids)})"
    return int(conn.execute(sql, ids).fetchone()[0])


def delete_rows(conn: sqlite3.Connection, table: str, column: str, ids: list[int]) -> int:
    if not ids:
        return 0
    sql = f"DELETE FROM {table} WHERE {column} IN ({placeholders(ids)})"
    cursor = conn.execute(sql, ids)
    return int(cursor.rowcount)


def main() -> int:
    parser = argparse.ArgumentParser(description="Delete knowledge records by id across dependent tables.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help=f"SQLite DB path (default: {DEFAULT_DB})")
    parser.add_argument("--ids-file", type=Path, required=True, help="Text file with one record id per line.")
    parser.add_argument("--apply", action="store_true", help="Commit deletes. Without this, only print counts.")
    args = parser.parse_args()

    ids = parse_ids(args.ids_file)
    if not ids:
        print("no record ids loaded")
        return 0

    conn = sqlite3.connect(args.db)
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        before_integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
        if before_integrity != "ok":
            raise RuntimeError(f"database integrity_check failed before delete: {before_integrity}")

        existing_count = count_rows(conn, "records", "id", ids)
        print(f"db: {args.db}")
        print(f"ids_loaded: {len(ids)}")
        print(f"matching_records: {existing_count}")
        print("planned_deletes:")
        for table in CHILD_TABLES:
            print(f"  {table}: {count_rows(conn, table, 'record_id', ids)}")
        print(f"  records_fts: {count_rows(conn, 'records_fts', 'rowid', ids)}")
        print(f"  records: {existing_count}")

        if not args.apply:
            print("dry_run: true")
            print("pass --apply to commit these deletes")
            return 0

        with conn:
            deleted: dict[str, int] = {}
            for table in CHILD_TABLES:
                deleted[table] = delete_rows(conn, table, "record_id", ids)
            deleted["records_fts"] = delete_rows(conn, "records_fts", "rowid", ids)
            deleted["records"] = delete_rows(conn, "records", "id", ids)

        after_integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
        if after_integrity != "ok":
            raise RuntimeError(f"database integrity_check failed after delete: {after_integrity}")

        print("deleted:")
        for table in [*CHILD_TABLES, "records_fts", "records"]:
            print(f"  {table}: {deleted[table]}")
        print("integrity_check: ok")
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
