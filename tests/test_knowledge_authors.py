from pathlib import Path

from knowledge_indexing.knowledge_authors import rebuild_author_index, sync_record_authors
from knowledge_indexing.knowledge_db import open_db, utc_now_iso


def _insert_record(conn, author: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO records (
            source, source_file, source_record_id, dedupe_key, title, author,
            text, url, event, year, tags, raw_json, imported_at
        )
        VALUES ('test', 'test.json', '1', 'test:1', 'Shared Talk', ?,
                'Evidence', '', 'Test Event', '2026', '', '{}', ?)
        """,
        (author, utc_now_iso()),
    )
    return cursor.lastrowid


def test_sync_record_authors_creates_unique_names_and_record_links(tmp_path: Path):
    db_path = tmp_path / "knowledge.sqlite3"
    with open_db(db_path) as conn:
        record_id = _insert_record(conn, "Alice Example; Bob Example, Alice Example")
        sync_record_authors(conn, record_id, "Alice Example; Bob Example, Alice Example")

        assert [
            row["name"] for row in conn.execute("SELECT name FROM authors ORDER BY name")
        ] == ["Alice Example", "Bob Example"]
        assert conn.execute("SELECT COUNT(*) FROM author_records").fetchone()[0] == 2


def test_sync_record_authors_replaces_old_links_and_removes_orphans(tmp_path: Path):
    db_path = tmp_path / "knowledge.sqlite3"
    with open_db(db_path) as conn:
        record_id = _insert_record(conn, "Alice Example; Bob Example")
        sync_record_authors(conn, record_id, "Alice Example; Bob Example")
        sync_record_authors(conn, record_id, "Carol Example")

        assert [
            row["name"] for row in conn.execute("SELECT name FROM authors ORDER BY name")
        ] == ["Carol Example"]


def test_rebuild_author_index_backfills_existing_records(tmp_path: Path):
    db_path = tmp_path / "knowledge.sqlite3"
    with open_db(db_path) as conn:
        _insert_record(conn, "Alice Example & Bob Example")
        rebuild_author_index(conn)

        rows = conn.execute(
            """
            SELECT authors.name, author_records.record_id
            FROM authors
            JOIN author_records ON author_records.author_id = authors.id
            ORDER BY authors.name
            """
        ).fetchall()
        assert [(row["name"], row["record_id"]) for row in rows] == [
            ("Alice Example", 1),
            ("Bob Example", 1),
        ]
