from __future__ import annotations

import re
import sqlite3


def split_authors(value: str) -> list[str]:
    return [
        part.strip().strip("&,;").strip()
        for part in re.split(
            r"\s*;\s*|\s*,\s*|\s+&\s+|\s+and\s+",
            value or "",
            flags=re.IGNORECASE,
        )
        if part.strip().strip("&,;").strip()
    ]


def sync_record_authors(conn: sqlite3.Connection, record_id: int, value: str) -> None:
    conn.execute("DELETE FROM author_records WHERE record_id = ?", (record_id,))
    seen: set[str] = set()
    for name in split_authors(value):
        key = name.casefold()
        if key in seen:
            continue
        seen.add(key)
        conn.execute("INSERT OR IGNORE INTO authors (name) VALUES (?)", (name,))
        author_id = conn.execute(
            "SELECT id FROM authors WHERE name = ? COLLATE NOCASE",
            (name,),
        ).fetchone()[0]
        conn.execute(
            "INSERT OR IGNORE INTO author_records (author_id, record_id) VALUES (?, ?)",
            (author_id, record_id),
        )
    conn.execute(
        """
        DELETE FROM authors
        WHERE NOT EXISTS (
            SELECT 1 FROM author_records WHERE author_records.author_id = authors.id
        )
        """
    )


def rebuild_author_index(conn: sqlite3.Connection) -> None:
    conn.execute("DELETE FROM author_records")
    conn.execute("DELETE FROM authors")
    for row in conn.execute(
        "SELECT id, author FROM records WHERE trim(COALESCE(author, '')) != '' ORDER BY id"
    ):
        sync_record_authors(conn, row["id"], row["author"])
