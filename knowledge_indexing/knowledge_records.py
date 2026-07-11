import json
import sqlite3
from pathlib import Path
from typing import Any

from .knowledge_config import DB_PATH
from .knowledge_db import clean_text, open_db, utc_now_iso


def search_records(db_path: Path, query: str, limit: int, unread: bool = False) -> list[sqlite3.Row]:
    sql = """
        SELECT records.*, bm25(records_fts) AS rank
        FROM records_fts
        JOIN records ON records_fts.rowid = records.id
        WHERE records_fts MATCH ?
    """
    params: list[Any] = [query]
    if unread:
        sql += " AND records.agent_read = 0"
    sql += " ORDER BY rank LIMIT ?"
    params.append(limit)
    with open_db(db_path) as conn:
        return list(conn.execute(sql, params))


def list_unread_records(db_path: Path = DB_PATH, limit: int = 20, source: str = "", start_id: int = 0) -> list[sqlite3.Row]:
    sql = """
        SELECT *
        FROM records
        WHERE agent_read = 0
    """
    params: list[Any] = []
    if source:
        sql += " AND source = ?"
        params.append(source)
    if start_id and start_id > 0:
        sql += " AND id >= ?"
        params.append(start_id)
    sql += " ORDER BY id LIMIT ?"
    params.append(limit)
    with open_db(db_path) as conn:
        return list(conn.execute(sql, params))


def mark_records_read(
    db_path: Path,
    record_ids: list[int],
    read: bool = True,
    reader: str = "agent",
    notes: str = "",
) -> int:
    if not record_ids:
        return 0
    now = utc_now_iso() if read else ""
    placeholders = ", ".join("?" for _ in record_ids)
    params: list[Any] = [
        1 if read else 0,
        now,
        clean_text(reader) if read else "",
        clean_text(notes) if read else "",
        *record_ids,
    ]
    with open_db(db_path) as conn:
        cursor = conn.execute(
            f"""
            UPDATE records
            SET agent_read = ?, agent_read_at = ?, agent_reader = ?, agent_notes = ?
            WHERE id IN ({placeholders})
            """,
            params,
        )
        conn.commit()
        return cursor.rowcount


def encode_topics(topics: list[str]) -> str:
    cleaned = [t.strip() for t in topics if t.strip()]
    if not cleaned:
        return ""
    return "|" + "|".join(cleaned) + "|"


def decode_topics(value: str | None) -> list[str]:
    if not value:
        return []
    return [t for t in value.strip("|").split("|") if t.strip()]


def set_record_topics(
    db_path: Path,
    record_id: int,
    topics: list[str],
    reader: str = "agent",
    notes: str = "",
) -> bool:
    now = utc_now_iso()
    with open_db(db_path) as conn:
        cursor = conn.execute(
            """
            UPDATE records
            SET agent_read = 1, agent_read_at = ?, agent_reader = ?,
                agent_notes = ?, agent_topics = ?
            WHERE id = ?
            """,
            (now, clean_text(reader), clean_text(notes), encode_topics(topics), record_id),
        )
        conn.commit()
        return cursor.rowcount > 0


def store_record_classification(
    db_path: Path,
    record_id: int,
    primary_topic: str,
    secondary_topics: list[str] | None = None,
    confidence: str = "",
    rationale: str = "",
    new_topic_candidate: str = "",
    raw: dict[str, Any] | None = None,
    model: str = "",
    schema_version: int = 1,
) -> None:
    now = utc_now_iso()

    def json_list(values: list[str] | None) -> str:
        clean = [clean_text(v) for v in values or [] if clean_text(v)]
        return json.dumps(clean, ensure_ascii=False)

    with open_db(db_path) as conn:
        conn.execute(
            """
            INSERT INTO record_classifications (
                record_id, model, schema_version, primary_topic,
                secondary_topics_json, confidence, rationale,
                new_topic_candidate, raw_json, created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(record_id) DO UPDATE SET
                model = excluded.model,
                schema_version = excluded.schema_version,
                primary_topic = excluded.primary_topic,
                secondary_topics_json = excluded.secondary_topics_json,
                confidence = excluded.confidence,
                rationale = excluded.rationale,
                new_topic_candidate = excluded.new_topic_candidate,
                raw_json = excluded.raw_json,
                updated_at = excluded.updated_at
            """,
            (
                record_id,
                clean_text(model),
                schema_version,
                clean_text(primary_topic),
                json_list(secondary_topics),
                clean_text(confidence),
                clean_text(rationale),
                clean_text(new_topic_candidate),
                json.dumps(raw or {}, ensure_ascii=False),
                now,
                now,
            ),
        )
        conn.commit()


def store_record_classification_error(
    db_path: Path,
    record_id: int,
    model: str,
    error_type: str,
    error_message: str,
) -> None:
    now = utc_now_iso()
    with open_db(db_path) as conn:
        conn.execute(
            """
            INSERT INTO record_classification_errors (
                record_id, model, error_type, error_message,
                attempts, first_seen_at, last_seen_at
            )
            VALUES (?, ?, ?, ?, 1, ?, ?)
            ON CONFLICT(record_id) DO UPDATE SET
                model = excluded.model,
                error_type = excluded.error_type,
                error_message = excluded.error_message,
                attempts = record_classification_errors.attempts + 1,
                last_seen_at = excluded.last_seen_at
            """,
            (
                record_id,
                clean_text(model),
                clean_text(error_type),
                clean_text(error_message)[:4000],
                now,
                now,
            ),
        )
        conn.commit()


def clear_record_classification_error(db_path: Path, record_id: int) -> None:
    with open_db(db_path) as conn:
        conn.execute("DELETE FROM record_classification_errors WHERE record_id = ?", (record_id,))
        conn.commit()


def list_record_classifications(
    db_path: Path = DB_PATH,
    limit: int = 20,
    low_confidence: bool = False,
    new_topic_candidates: bool = False,
) -> list[sqlite3.Row]:
    sql = """
        SELECT
            record_classifications.record_id,
            records.source,
            records.title,
            record_classifications.primary_topic,
            record_classifications.secondary_topics_json,
            record_classifications.confidence,
            record_classifications.rationale,
            record_classifications.new_topic_candidate,
            record_classifications.model,
            record_classifications.schema_version,
            record_classifications.updated_at
        FROM record_classifications
        JOIN records ON records.id = record_classifications.record_id
        WHERE 1 = 1
    """
    params: list[Any] = []
    if low_confidence:
        sql += " AND record_classifications.confidence = 'low'"
    if new_topic_candidates:
        sql += " AND record_classifications.new_topic_candidate != ''"
    sql += " ORDER BY record_classifications.updated_at DESC, record_classifications.record_id DESC LIMIT ?"
    params.append(limit)
    with open_db(db_path) as conn:
        return list(conn.execute(sql, params))


def list_record_classification_errors(db_path: Path = DB_PATH, limit: int = 20) -> list[sqlite3.Row]:
    with open_db(db_path) as conn:
        return list(conn.execute(
            """
            SELECT
                record_classification_errors.record_id,
                records.source,
                records.title,
                record_classification_errors.model,
                record_classification_errors.error_type,
                record_classification_errors.error_message,
                record_classification_errors.attempts,
                record_classification_errors.first_seen_at,
                record_classification_errors.last_seen_at
            FROM record_classification_errors
            JOIN records ON records.id = record_classification_errors.record_id
            ORDER BY record_classification_errors.last_seen_at DESC, record_classification_errors.record_id
            LIMIT ?
            """,
            (limit,),
        ))


def store_record_annotation_error(
    db_path: Path,
    record_id: int,
    model: str,
    error_type: str,
    error_message: str,
) -> None:
    now = utc_now_iso()
    with open_db(db_path) as conn:
        conn.execute(
            """
            INSERT INTO record_annotation_errors (
                record_id, model, error_type, error_message,
                attempts, first_seen_at, last_seen_at
            )
            VALUES (?, ?, ?, ?, 1, ?, ?)
            ON CONFLICT(record_id) DO UPDATE SET
                model = excluded.model,
                error_type = excluded.error_type,
                error_message = excluded.error_message,
                attempts = record_annotation_errors.attempts + 1,
                last_seen_at = excluded.last_seen_at
            """,
            (
                record_id,
                clean_text(model),
                clean_text(error_type),
                clean_text(error_message)[:4000],
                now,
                now,
            ),
        )
        conn.commit()


def clear_record_annotation_error(db_path: Path, record_id: int) -> None:
    with open_db(db_path) as conn:
        conn.execute("DELETE FROM record_annotation_errors WHERE record_id = ?", (record_id,))
        conn.commit()


def list_record_annotation_errors(db_path: Path = DB_PATH, limit: int = 20) -> list[sqlite3.Row]:
    with open_db(db_path) as conn:
        return list(conn.execute(
            """
            SELECT
                record_annotation_errors.record_id,
                records.source,
                records.title,
                record_annotation_errors.model,
                record_annotation_errors.error_type,
                record_annotation_errors.error_message,
                record_annotation_errors.attempts,
                record_annotation_errors.first_seen_at,
                record_annotation_errors.last_seen_at
            FROM record_annotation_errors
            JOIN records ON records.id = record_annotation_errors.record_id
            ORDER BY record_annotation_errors.last_seen_at DESC, record_annotation_errors.record_id
            LIMIT ?
            """,
            (limit,),
        ))


def list_records_for_topic(
    db_path: Path,
    topic_name: str,
    limit: int = 500,
) -> list[sqlite3.Row]:
    pattern = f"%|{topic_name}|%"
    with open_db(db_path) as conn:
        if limit and limit > 0:
            return list(conn.execute(
                "SELECT * FROM records WHERE agent_topics LIKE ? ORDER BY id LIMIT ?",
                (pattern, limit),
            ))
        return list(conn.execute(
            "SELECT * FROM records WHERE agent_topics LIKE ? ORDER BY id",
            (pattern,),
        ))


def list_records_missing_annotations(
    db_path: Path = DB_PATH,
    limit: int = 20,
    source: str = "",
    start_id: int = 0,
) -> list[sqlite3.Row]:
    sql = """
        SELECT records.*
        FROM records
        LEFT JOIN record_annotations ON record_annotations.record_id = records.id
        WHERE record_annotations.record_id IS NULL
    """
    params: list[Any] = []
    if source:
        sql += " AND records.source = ?"
        params.append(source)
    if start_id and start_id > 0:
        sql += " AND records.id >= ?"
        params.append(start_id)
    sql += " ORDER BY records.id LIMIT ?"
    params.append(limit)
    with open_db(db_path) as conn:
        return list(conn.execute(sql, params))


def list_records_missing_classifications(
    db_path: Path = DB_PATH,
    limit: int = 20,
    source: str = "",
    start_id: int = 0,
) -> list[sqlite3.Row]:
    sql = """
        SELECT records.*
        FROM records
        JOIN record_annotations ON record_annotations.record_id = records.id
        LEFT JOIN record_classifications ON record_classifications.record_id = records.id
        WHERE record_classifications.record_id IS NULL
    """
    params: list[Any] = []
    if source:
        sql += " AND records.source = ?"
        params.append(source)
    if start_id and start_id > 0:
        sql += " AND records.id >= ?"
        params.append(start_id)
    sql += " ORDER BY records.id LIMIT ?"
    params.append(limit)
    with open_db(db_path) as conn:
        return list(conn.execute(sql, params))


def get_record_annotation_map(
    db_path: Path,
    record_ids: list[int],
) -> dict[int, sqlite3.Row]:
    if not record_ids:
        return {}
    placeholders = ",".join("?" for _ in record_ids)
    with open_db(db_path) as conn:
        rows = conn.execute(
            f"""
            SELECT *
            FROM record_annotations
            WHERE record_id IN ({placeholders})
            """,
            record_ids,
        ).fetchall()
        return {int(row["record_id"]): row for row in rows}


def list_record_annotations(
    db_path: Path = DB_PATH,
    limit: int = 20,
    source: str = "",
    query: str = "",
    latest: bool = False,
) -> list[sqlite3.Row]:
    sql = """
        SELECT
            records.id AS record_id,
            records.source,
            records.year,
            records.title,
            records.author,
            records.url,
            records.text,
            records.agent_topics,
            record_annotations.short_summary,
            record_annotations.keywords_json,
            record_annotations.tools_json,
            record_annotations.people_json,
            record_annotations.claims_json,
            record_annotations.use_cases_json,
            record_annotations.ai_relevance,
            record_annotations.content_types_json,
            record_annotations.security_domains_json,
            record_annotations.source_quality,
            record_annotations.contains_prompt_injection,
            record_annotations.relevance_notes,
            record_annotations.updated_at,
            record_annotations.model,
            record_annotations.schema_version
        FROM record_annotations
        JOIN records ON records.id = record_annotations.record_id
        WHERE 1 = 1
    """
    params: list[Any] = []
    if source:
        sql += " AND records.source = ?"
        params.append(source)
    if query:
        like = f"%{query}%"
        sql += """
            AND (
                records.title LIKE ?
                OR records.text LIKE ?
                OR record_annotations.short_summary LIKE ?
                OR record_annotations.keywords_json LIKE ?
                OR record_annotations.tools_json LIKE ?
                OR record_annotations.claims_json LIKE ?
                OR record_annotations.security_domains_json LIKE ?
                OR record_annotations.ai_relevance LIKE ?
                OR record_annotations.relevance_notes LIKE ?
            )
        """
        params.extend([like, like, like, like, like, like, like, like, like])
    if latest:
        sql += " ORDER BY record_annotations.updated_at DESC, record_annotations.record_id DESC LIMIT ?"
    else:
        sql += " ORDER BY records.id LIMIT ?"
    params.append(limit)
    with open_db(db_path) as conn:
        return list(conn.execute(sql, params))


def store_record_annotation(
    db_path: Path,
    record_id: int,
    short_summary: str,
    keywords: list[str] | None = None,
    tools: list[str] | None = None,
    people: list[str] | None = None,
    claims: list[str] | None = None,
    use_cases: list[str] | None = None,
    ai_relevance: str = "",
    content_types: list[str] | None = None,
    security_domains: list[str] | None = None,
    source_quality: str = "",
    contains_prompt_injection: bool = False,
    relevance_notes: str = "",
    raw: dict[str, Any] | None = None,
    model: str = "",
    schema_version: int = 1,
) -> None:
    now = utc_now_iso()

    def json_list(values: list[str] | None) -> str:
        clean = [clean_text(v) for v in values or [] if clean_text(v)]
        return json.dumps(clean, ensure_ascii=False)

    raw_json = json.dumps(raw or {}, ensure_ascii=False)
    with open_db(db_path) as conn:
        conn.execute(
            """
            INSERT INTO record_annotations (
                record_id, model, schema_version, short_summary,
                keywords_json, tools_json, people_json, claims_json,
                use_cases_json, ai_relevance, content_types_json,
                security_domains_json, source_quality, contains_prompt_injection, relevance_notes,
                raw_json, created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(record_id) DO UPDATE SET
                model = excluded.model,
                schema_version = excluded.schema_version,
                short_summary = excluded.short_summary,
                keywords_json = excluded.keywords_json,
                tools_json = excluded.tools_json,
                people_json = excluded.people_json,
                claims_json = excluded.claims_json,
                use_cases_json = excluded.use_cases_json,
                ai_relevance = excluded.ai_relevance,
                content_types_json = excluded.content_types_json,
                security_domains_json = excluded.security_domains_json,
                source_quality = excluded.source_quality,
                contains_prompt_injection = excluded.contains_prompt_injection,
                relevance_notes = excluded.relevance_notes,
                raw_json = excluded.raw_json,
                updated_at = excluded.updated_at
            """,
            (
                record_id,
                clean_text(model),
                schema_version,
                clean_text(short_summary),
                json_list(keywords),
                json_list(tools),
                json_list(people),
                json_list(claims),
                json_list(use_cases),
                clean_text(ai_relevance),
                json_list(content_types),
                json_list(security_domains),
                clean_text(source_quality),
                1 if contains_prompt_injection else 0,
                clean_text(relevance_notes),
                raw_json,
                now,
                now,
            ),
        )
        conn.commit()
