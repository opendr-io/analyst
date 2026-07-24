import json
import re
import sqlite3
from pathlib import Path
from typing import Any

from .knowledge_authors import rebuild_author_index, sync_record_authors
from .knowledge_config import (
    APP_DIR,
    CONFERENCE_RECORD_SOURCES,
    DB_PATH,
    DEFCON33_LATEST,
    PROMPTORGTFO_LATEST,
)
from .knowledge_db import KnowledgeRecord, clean_text, json_dumps, log_warning, open_db, stable_hash, utc_now_iso


def detect_export_kind(data: Any, path: Path) -> str:
    name = path.name.lower()
    parent = str(path.parent).lower()
    if "blackhat" in name or "blackhat" in parent:
        return "blackhat"
    if "camlis" in name or "camlis" in parent:
        return "camlis"
    if "bsideslv" in name or "bsideslv" in parent:
        return "bsideslv"
    if "defcon" in name or "defcon" in parent:
        return "defcon"
    if "rsac" in name or "rsac" in parent:
        return "rsac"
    if "promptorgtfo" in name or "promptorgtfo" in parent:
        return "promptorgtfo"
    if isinstance(data, dict):
        manifest = ((data.get("source") or {}).get("manifest") or {})
        if clean_text(manifest.get("code", "")).lower().startswith("defcon"):
            return "defcon"
        if "playlist" in data and "records" in data:
            records = data.get("records") or []
            if records and isinstance(records[0], dict) and "talk_title" in records[0]:
                return "youtube_playlist"
    elif isinstance(data, list):
        if data and isinstance(data[0], dict) and "summary" in data[0] and "transcript_available" in data[0]:
            return "promptorgtfo"
    return "unknown"


def _dedupe_component(value: str) -> str:
    value = clean_text(value).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "unknown"


def record_dedupe_key(
    source: str,
    record_id: str,
    url: str,
    title: str,
    author: str,
    text: str,
    event: str = "",
    year: str = "",
) -> str:
    if source in CONFERENCE_RECORD_SOURCES and title:
        event_key = _dedupe_component(year or event)
        material = "\n".join([source, event_key, title.lower()])
        return f"{source}:{event_key}:title:{stable_hash(material)}"
    if record_id and ("youtube.com/watch" in url or "youtu.be/" in url):
        return f"{source}:id:{record_id}"
    if url:
        return f"{source}:url:{url.split('?', 1)[0].rstrip('/')}"
    if record_id:
        return f"{source}:id:{record_id}"
    material = "\n".join([source, year.lower() or event.lower(), title.lower(), author.lower(), text.lower()[:1000]])
    return f"{source}:text:{stable_hash(material)}"


def make_record(
    *,
    source: str,
    source_file: Path,
    source_record_id: Any = "",
    title: Any = "",
    author: Any = "",
    text: Any = "",
    url: Any = "",
    event: Any = "",
    year: Any = "",
    tags: Any = "",
    raw: dict[str, Any],
) -> KnowledgeRecord:
    source_record_id_text = clean_text(source_record_id)
    title_text = clean_text(title)
    author_text = clean_text(author)
    text_text = clean_text(text)
    url_text = clean_text(url)
    event_text = clean_text(event)
    year_text = clean_text(year)
    return KnowledgeRecord(
        source=source,
        source_file=str(source_file),
        source_record_id=source_record_id_text,
        dedupe_key=record_dedupe_key(
            source,
            source_record_id_text,
            url_text,
            title_text,
            author_text,
            text_text,
            event=event_text,
            year=year_text,
        ),
        title=title_text,
        author=author_text,
        text=text_text,
        url=url_text,
        event=event_text,
        year=year_text,
        tags=clean_text(tags),
        raw_json=json_dumps(raw),
    )


def records_from_blackhat(data: dict[str, Any], source_file: Path) -> list[KnowledgeRecord]:
    records = []
    for talk in data.get("talks", []):
        tags = "; ".join(
            part for part in [talk.get("track", ""), talk.get("listing_text", "")] if clean_text(part)
        )
        records.append(
            make_record(
                source="blackhat",
                source_file=source_file,
                source_record_id=talk.get("session_id", ""),
                title=talk.get("title", ""),
                author=normalize_blackhat_authors(talk.get("speakers", "")),
                text=talk.get("abstract", ""),
                url=talk.get("url", ""),
                event=talk.get("event", "Black Hat"),
                year=talk.get("year", ""),
                tags=tags,
                raw=talk,
            )
        )
    return records


def normalize_blackhat_authors(value: Any) -> str:
    authors = clean_text(value)
    authors = re.sub(
        r"(^|;\s*)(?:Sponsor Speaker|Speaker|Contributor|Panelist|Moderator):\s*",
        r"\1",
        authors,
        flags=re.IGNORECASE,
    )
    cleaned = []
    depth = 0
    for char in authors:
        if char == "(":
            depth += 1
        elif char == ")" and depth:
            depth -= 1
        elif depth == 0:
            cleaned.append(char)
    return re.sub(r"\s*;\s*", "; ", "".join(cleaned)).strip(" ;")


def records_from_camlis(data: dict[str, Any], source_file: Path) -> list[KnowledgeRecord]:
    records = []
    for talk in data.get("talks", []):
        author = clean_text(talk.get("speaker", "") or talk.get("authors", ""))
        if author.lower() in {"panel", "panel discussion", "community discussion"}:
            author = ""
        tags = "; ".join(
            part
            for part in [
                talk.get("section", ""),
                talk.get("role", ""),
                talk.get("organization", ""),
            ]
            if clean_text(part)
        )
        records.append(
            make_record(
                source="camlis",
                source_file=source_file,
                source_record_id="|".join(
                    [
                        clean_text(talk.get("year", "")),
                        clean_text(talk.get("title", "")),
                        clean_text(talk.get("url", "")),
                    ]
                ),
                title=talk.get("title", ""),
                author=author,
                text=talk.get("abstract", ""),
                url=talk.get("url", ""),
                event="CAMLIS",
                year=talk.get("year", ""),
                tags=tags,
                raw=talk,
            )
        )
    return records


def records_from_bsideslv(data: dict[str, Any], source_file: Path) -> list[KnowledgeRecord]:
    records = []
    for talk in data.get("talks", []):
        title = clean_text(talk.get("title", ""))
        if not title:
            continue
        records.append(
            make_record(
                source="bsideslv",
                source_file=source_file,
                source_record_id=talk.get("session_id", ""),
                title=title,
                author=talk.get("speakers", ""),
                text=talk.get("abstract", ""),
                url=talk.get("url", ""),
                event=talk.get("event", "BSidesLV 2025"),
                year=talk.get("year", "2025"),
                tags="; ".join(
                    part
                    for part in [talk.get("track", ""), talk.get("room", ""), talk.get("date", ""), talk.get("time", "")]
                    if clean_text(part)
                ),
                raw=talk,
            )
        )
    return records


def records_from_rsac(data: dict[str, Any], source_file: Path) -> list[KnowledgeRecord]:
    records = []
    source_label = clean_text((data.get("config") or {}).get("source", "")) or "rsac"
    year = data.get("year") or ""
    for talk in data.get("talks", []):
        title = clean_text(talk.get("title", ""))
        if not title:
            continue
        records.append(
            make_record(
                source=source_label,
                source_file=source_file,
                source_record_id=talk.get("session_id", ""),
                title=title,
                author=clean_text(talk.get("speaker", "") or talk.get("speakers", "")),
                text=clean_text(talk.get("abstract", "") or talk.get("description", "")),
                url=talk.get("url", ""),
                event="RSAC",
                year=talk.get("year") or year,
                tags=clean_text(talk.get("track", "")),
                raw=talk,
            )
        )
    return records


def records_from_defcon(data: dict[str, Any], source_file: Path) -> list[KnowledgeRecord]:
    records = []
    source_meta = data.get("source") or {}
    manifest = source_meta.get("manifest") or {}
    source_label = clean_text(manifest.get("code", "")).lower() or clean_text(source_meta.get("conference", "")).lower()
    source_label = source_label or "defcon"
    event = clean_text(manifest.get("name", "")) or clean_text(source_label.upper())
    year_match = re.search(r"(20\d{2})", event)
    default_year = year_match.group(1) if year_match else ""
    for talk in data.get("talks", []):
        title = clean_text(talk.get("title", ""))
        if not title:
            continue
        tags = "; ".join(
            part
            for part in [
                talk.get("tags", ""),
                talk.get("matched_tags", ""),
                talk.get("track", ""),
                talk.get("room", ""),
                talk.get("date", ""),
                talk.get("time", ""),
            ]
            if clean_text(part)
        )
        records.append(
            make_record(
                source=source_label,
                source_file=source_file,
                source_record_id=clean_text(talk.get("session_id", "") or talk.get("content_id", "")),
                title=title,
                author=clean_text(talk.get("speakers", "") or talk.get("speaker", "")),
                text=clean_text(talk.get("abstract", "") or talk.get("description", "")),
                url=talk.get("url", ""),
                event=clean_text(talk.get("event", "")) or event,
                year=talk.get("year", "") or default_year,
                tags=tags,
                raw=talk,
            )
        )
    return records


def parse_unprompted_title(record: dict[str, Any]) -> tuple[str, str]:
    full_title = clean_text(record.get("title", ""))
    suffix = " | [un]prompted 2026"
    core = full_title.removesuffix(suffix).strip()
    if " - " not in core:
        return core or clean_text(record.get("talk_title", "")), ""
    author, title = core.split(" - ", 1)
    return title.strip(), author.strip()


def records_from_youtube_playlist(data: dict[str, Any], source_file: Path) -> list[KnowledgeRecord]:
    stem = source_file.stem
    source_slug = stem.split("_")[0] if "_" in stem else stem

    event_map = {
        "defcon33": "DEF CON 33",
    }
    event = event_map.get(source_slug, source_slug.upper())

    records = []
    for r in data.get("records", []):
        abstract = clean_text(r.get("abstract", ""))
        if len(abstract) < 30:
            continue
        title = clean_text(r.get("talk_title", ""))
        author = clean_text(r.get("speakers", ""))
        if source_slug == "unprompted2026":
            title, author = parse_unprompted_title(r)
        elif source_slug == "defcon33" and "video team" in title.lower():
            title = author or title
            author = ""
        elif source_slug == "defcon33":
            if author.lower() in {"panel", "panel discussion", "community discussion"}:
                author = ""
            author = re.sub(r"^20\d{2}\s+(?=[A-Z])", "", author)
        if source_slug == "defcon33" and is_defcon_low_value_schedule_record(title, abstract):
            continue
        year = "2025" if source_slug == "defcon33" else (clean_text(r.get("upload_date", "")) or "")[:4] or "2025"
        tags = clean_text(r.get("duration_string", ""))
        records.append(
            make_record(
                source=source_slug,
                source_file=source_file,
                source_record_id=clean_text(r.get("id", "")),
                title=title,
                author=author,
                text=abstract,
                url=r.get("url", ""),
                event=event,
                year=year,
                tags=tags,
                raw=r,
            )
        )
    return records


def is_defcon_low_value_schedule_record(title: str, abstract: str) -> bool:
    title_text = clean_text(title).lower()
    abstract_text = clean_text(abstract).lower()
    if title_text.startswith("live music -"):
        return True
    if re.match(r"^live set from .+ (?:thursday|friday|saturday|sunday) night at the lvcc!?$", abstract_text):
        return True
    return False


def records_from_promptorgtfo(data: list[dict[str, Any]], source_file: Path) -> list[KnowledgeRecord]:
    records = []
    for r in data:
        title_raw = clean_text(r.get("title", ""))
        speaker = ""
        talk_title = title_raw

        pipe_idx = title_raw.rfind(" | ")
        core = title_raw[:pipe_idx] if pipe_idx != -1 else title_raw
        if " - " in core:
            sp, tl = core.split(" - ", 1)
            if sp and not sp.isupper():
                speaker = sp.strip()
                talk_title = tl.strip()
        if speaker.lower() in {"panel", "panel discussion", "community discussion"}:
            speaker = ""

        tools = r.get("tools") or []
        tool_names = [t.get("name", "") for t in tools if t.get("name")]
        tags = "; ".join(tool_names[:10])

        body = clean_text(r.get("text", "") or r.get("summary", ""))
        if not body:
            continue

        records.append(
            make_record(
                source="promptorgtfo",
                source_file=source_file,
                source_record_id=clean_text(r.get("url", "")),
                title=talk_title,
                author=speaker,
                text=body,
                url=r.get("url", ""),
                event="Prompt||GTFO",
                year="2026",
                tags=tags,
                raw=r,
            )
        )
    return records


def records_from_export(path: Path) -> list[KnowledgeRecord]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        log_warning(f"skipping {path}: {exc}")
        return []
    kind = detect_export_kind(data, path)
    try:
        if kind == "blackhat":
            return records_from_blackhat(data, path)
        if kind == "camlis":
            return records_from_camlis(data, path)
        if kind == "bsideslv":
            return records_from_bsideslv(data, path)
        if kind == "defcon":
            return records_from_defcon(data, path)
        if kind == "rsac":
            return records_from_rsac(data, path)
        if kind == "youtube_playlist":
            return records_from_youtube_playlist(data, path)
        if kind == "promptorgtfo":
            return records_from_promptorgtfo(data, path)
    except Exception as exc:
        log_warning(f"parser error {path} (kind={kind}): {exc}")
    return []


def upsert_record(conn: sqlite3.Connection, record: KnowledgeRecord) -> bool:
    now = utc_now_iso()
    existing = conn.execute(
        "SELECT id, agent_read, summarized_at, summary FROM records WHERE dedupe_key = ?",
        (record.dedupe_key,),
    ).fetchone()
    if existing:
        row_id = existing["id"]
        conn.execute(
            """
            UPDATE records
            SET source = ?, source_file = ?, source_record_id = ?, title = ?, author = ?,
                text = ?, url = ?, event = ?, year = ?, tags = ?, raw_json = ?, imported_at = ?
            WHERE id = ?
            """,
            (
                record.source,
                record.source_file,
                record.source_record_id,
                record.title,
                record.author,
                record.text,
                record.url,
                record.event,
                record.year,
                record.tags,
                record.raw_json,
                now,
                row_id,
            ),
        )
        inserted = False
    else:
        cursor = conn.execute(
            """
            INSERT INTO records (
                source, source_file, source_record_id, dedupe_key, title, author, text,
                url, event, year, tags, raw_json, imported_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record.source,
                record.source_file,
                record.source_record_id,
                record.dedupe_key,
                record.title,
                record.author,
                record.text,
                record.url,
                record.event,
                record.year,
                record.tags,
                record.raw_json,
                now,
            ),
        )
        row_id = cursor.lastrowid
        inserted = True

    conn.execute("DELETE FROM records_fts WHERE rowid = ?", (row_id,))
    conn.execute(
        "INSERT INTO records_fts(rowid, title, author, text, tags) VALUES (?, ?, ?, ?, ?)",
        (row_id, record.title, record.author, record.text, record.tags),
    )
    sync_record_authors(conn, row_id, record.author)
    return inserted


def import_exports(paths: list[Path], db_path: Path = DB_PATH, rebuild: bool = False) -> dict[str, int]:
    stats = {"files": 0, "records": 0, "inserted": 0, "updated": 0, "skipped_files": 0, "errors": 0}
    with open_db(db_path) as conn:
        if rebuild:
            conn.execute("DELETE FROM records_fts")
            conn.execute("DELETE FROM records")
        for path in paths:
            if not path.exists() or not path.is_file():
                log_warning(f"skip (not found): {path}")
                stats["skipped_files"] += 1
                continue
            records = records_from_export(path)
            if not records:
                log_warning(f"skip (0 records): {path}")
                stats["skipped_files"] += 1
                continue
            file_inserted = file_updated = file_errors = 0
            for record in records:
                stats["records"] += 1
                try:
                    if upsert_record(conn, record):
                        stats["inserted"] += 1
                        file_inserted += 1
                    else:
                        stats["updated"] += 1
                        file_updated += 1
                except Exception as exc:
                    log_warning(f"upsert error [{record.source}] {record.title[:60]!r}: {exc}")
                    stats["errors"] += 1
                    file_errors += 1
            summary = f"  {path.name}: {len(records)} parsed, {file_inserted} inserted, {file_updated} updated"
            if file_errors:
                summary += f", {file_errors} errors"
            print(summary)
            stats["files"] += 1
        conn.commit()
    return stats


def default_export_paths(latest_per_source: bool = True) -> list[Path]:
    groups = [
        sorted((APP_DIR / "data" / "blackhat" / "exports").glob("*.json")),
        sorted((APP_DIR / "data" / "camlis" / "exports").glob("*.json")),
    ]
    if latest_per_source:
        paths = [group[-1] for group in groups if group]
    else:
        paths = [path for group in groups for path in group]
    for fixed in (DEFCON33_LATEST, PROMPTORGTFO_LATEST):
        if fixed is not None and fixed.exists() and fixed not in paths:
            paths.append(fixed)
    return paths
