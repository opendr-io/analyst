import json
import re
import sqlite3
import sys
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .knowledge_config import DB_PATH, LOG_PATH


@dataclass(frozen=True)
class KnowledgeRecord:
    source: str
    source_file: str
    source_record_id: str
    dedupe_key: str
    title: str
    author: str
    text: str
    url: str
    event: str
    year: str
    tags: str
    raw_json: str


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


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


def clean_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def stable_hash(value: str) -> str:
    return __import__("hashlib").sha256(value.encode("utf-8")).hexdigest()


def json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


@contextmanager
def open_db(db_path: Path = DB_PATH):
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    init_db(conn)
    try:
        yield conn
    finally:
        conn.close()


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY,
            source TEXT NOT NULL,
            source_file TEXT NOT NULL,
            source_record_id TEXT NOT NULL,
            dedupe_key TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL DEFAULT '',
            author TEXT NOT NULL DEFAULT '',
            text TEXT NOT NULL DEFAULT '',
            url TEXT NOT NULL DEFAULT '',
            event TEXT NOT NULL DEFAULT '',
            year TEXT NOT NULL DEFAULT '',
            tags TEXT NOT NULL DEFAULT '',
            raw_json TEXT NOT NULL DEFAULT '{}',
            agent_read INTEGER NOT NULL DEFAULT 0,
            agent_read_at TEXT NOT NULL DEFAULT '',
            agent_reader TEXT NOT NULL DEFAULT '',
            agent_notes TEXT NOT NULL DEFAULT '',
            summarized_at TEXT NOT NULL DEFAULT '',
            summary TEXT NOT NULL DEFAULT '',
            imported_at TEXT NOT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_records_source ON records(source);
        CREATE INDEX IF NOT EXISTS idx_records_agent_read ON records(agent_read);
        CREATE INDEX IF NOT EXISTS idx_records_year ON records(year);

        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL COLLATE NOCASE UNIQUE
        );

        CREATE TABLE IF NOT EXISTS author_records (
            author_id INTEGER NOT NULL,
            record_id INTEGER NOT NULL,
            PRIMARY KEY (author_id, record_id),
            FOREIGN KEY(author_id) REFERENCES authors(id) ON DELETE CASCADE,
            FOREIGN KEY(record_id) REFERENCES records(id) ON DELETE CASCADE
        );

        CREATE INDEX IF NOT EXISTS idx_author_records_record_id
            ON author_records(record_id);

        CREATE TABLE IF NOT EXISTS topic_candidates (
            id INTEGER PRIMARY KEY,
            phrase TEXT NOT NULL UNIQUE,
            score REAL NOT NULL,
            record_count INTEGER NOT NULL,
            sources TEXT NOT NULL DEFAULT '',
            sample_record_ids TEXT NOT NULL DEFAULT '[]',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            query TEXT NOT NULL,
            description TEXT NOT NULL DEFAULT '',
            source TEXT NOT NULL DEFAULT 'seed',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS record_annotations (
            id INTEGER PRIMARY KEY,
            record_id INTEGER NOT NULL UNIQUE,
            model TEXT NOT NULL DEFAULT '',
            schema_version INTEGER NOT NULL DEFAULT 1,
            short_summary TEXT NOT NULL DEFAULT '',
            keywords_json TEXT NOT NULL DEFAULT '[]',
            tools_json TEXT NOT NULL DEFAULT '[]',
            people_json TEXT NOT NULL DEFAULT '[]',
            claims_json TEXT NOT NULL DEFAULT '[]',
            use_cases_json TEXT NOT NULL DEFAULT '[]',
            ai_relevance TEXT NOT NULL DEFAULT '',
            content_types_json TEXT NOT NULL DEFAULT '[]',
            security_domains_json TEXT NOT NULL DEFAULT '[]',
            source_quality TEXT NOT NULL DEFAULT '',
            contains_prompt_injection INTEGER NOT NULL DEFAULT 0,
            relevance_notes TEXT NOT NULL DEFAULT '',
            raw_json TEXT NOT NULL DEFAULT '{}',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY(record_id) REFERENCES records(id)
        );

        CREATE INDEX IF NOT EXISTS idx_record_annotations_record_id
            ON record_annotations(record_id);

        CREATE TABLE IF NOT EXISTS record_classifications (
            id INTEGER PRIMARY KEY,
            record_id INTEGER NOT NULL UNIQUE,
            model TEXT NOT NULL DEFAULT '',
            schema_version INTEGER NOT NULL DEFAULT 1,
            primary_topic TEXT NOT NULL DEFAULT '',
            secondary_topics_json TEXT NOT NULL DEFAULT '[]',
            confidence TEXT NOT NULL DEFAULT '',
            rationale TEXT NOT NULL DEFAULT '',
            new_topic_candidate TEXT NOT NULL DEFAULT '',
            raw_json TEXT NOT NULL DEFAULT '{}',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY(record_id) REFERENCES records(id)
        );

        CREATE INDEX IF NOT EXISTS idx_record_classifications_record_id
            ON record_classifications(record_id);
        CREATE INDEX IF NOT EXISTS idx_record_classifications_primary_topic
            ON record_classifications(primary_topic);

        CREATE TABLE IF NOT EXISTS record_annotation_errors (
            id INTEGER PRIMARY KEY,
            record_id INTEGER NOT NULL UNIQUE,
            model TEXT NOT NULL DEFAULT '',
            error_type TEXT NOT NULL DEFAULT '',
            error_message TEXT NOT NULL DEFAULT '',
            attempts INTEGER NOT NULL DEFAULT 0,
            first_seen_at TEXT NOT NULL,
            last_seen_at TEXT NOT NULL,
            FOREIGN KEY(record_id) REFERENCES records(id)
        );

        CREATE INDEX IF NOT EXISTS idx_record_annotation_errors_record_id
            ON record_annotation_errors(record_id);
        CREATE INDEX IF NOT EXISTS idx_record_annotation_errors_last_seen_at
            ON record_annotation_errors(last_seen_at);

        CREATE TABLE IF NOT EXISTS record_classification_errors (
            id INTEGER PRIMARY KEY,
            record_id INTEGER NOT NULL UNIQUE,
            model TEXT NOT NULL DEFAULT '',
            error_type TEXT NOT NULL DEFAULT '',
            error_message TEXT NOT NULL DEFAULT '',
            attempts INTEGER NOT NULL DEFAULT 0,
            first_seen_at TEXT NOT NULL,
            last_seen_at TEXT NOT NULL,
            FOREIGN KEY(record_id) REFERENCES records(id)
        );

        CREATE INDEX IF NOT EXISTS idx_record_classification_errors_record_id
            ON record_classification_errors(record_id);
        CREATE INDEX IF NOT EXISTS idx_record_classification_errors_last_seen_at
            ON record_classification_errors(last_seen_at);
        """
    )
    ensure_column(conn, "records", "agent_read_at", "TEXT NOT NULL DEFAULT ''")
    ensure_column(conn, "records", "agent_reader", "TEXT NOT NULL DEFAULT ''")
    ensure_column(conn, "records", "agent_notes", "TEXT NOT NULL DEFAULT ''")
    ensure_column(conn, "records", "agent_topics", "TEXT NOT NULL DEFAULT ''")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_records_agent_topics ON records(agent_topics)")
    ensure_column(conn, "record_annotations", "ai_relevance", "TEXT NOT NULL DEFAULT ''")
    ensure_column(conn, "record_annotations", "content_types_json", "TEXT NOT NULL DEFAULT '[]'")
    ensure_column(conn, "record_annotations", "security_domains_json", "TEXT NOT NULL DEFAULT '[]'")
    ensure_column(conn, "record_annotations", "source_quality", "TEXT NOT NULL DEFAULT ''")
    ensure_column(conn, "record_annotations", "contains_prompt_injection", "INTEGER NOT NULL DEFAULT 0")
    ensure_column(conn, "record_annotations", "relevance_notes", "TEXT NOT NULL DEFAULT ''")
    fts_schema = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'records_fts'"
    ).fetchone()
    if fts_schema and "content='records'" in (fts_schema["sql"] or ""):
        conn.execute("DROP TABLE records_fts")
    conn.execute(
        """
        CREATE VIRTUAL TABLE IF NOT EXISTS records_fts USING fts5(
            title,
            author,
            text,
            tags
        )
        """
    )


_IDENT_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _validate_ident(name: str) -> None:
    if not _IDENT_RE.match(name):
        raise ValueError(f"Invalid SQL identifier: {name!r}")


def ensure_column(conn: sqlite3.Connection, table: str, column: str, definition: str) -> None:
    _validate_ident(table)
    _validate_ident(column)
    columns = {row["name"] for row in conn.execute(f"PRAGMA table_info({table})")}
    if column not in columns:
        conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")
