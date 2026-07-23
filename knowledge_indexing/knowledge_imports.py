import json
import re
import sqlite3
from pathlib import Path
from typing import Any

from .knowledge_authors import rebuild_author_index, sync_record_authors
from .knowledge_config import APP_DIR, BSIDESSF_MD, DB_PATH, DEFCON33_LATEST, LINKEDIN_DB_PATH, PROMPTORGTFO_LATEST
from .knowledge_db import KnowledgeRecord, clean_text, json_dumps, log_warning, open_db, stable_hash, utc_now_iso


_TIME_BLOCK_RE = re.compile(r"^\d{1,2}:\d{2}\s*(?:AM|PM)\s*[-–]\s*\d{1,2}:\d{2}\s*(?:AM|PM)", re.IGNORECASE)
_TYPE_MARKER_RE = re.compile(r"^~\s*\w+(?:\s+\w+)?\s*~$")
_WORD = r"[A-Z][a-z]+(?:-[A-Z][a-z]+)?"
_SPEAKER_NAME_RE = re.compile(
    rf"^((?:{_WORD})\s+(?:{_WORD})(?:,\s+(?:{_WORD})\s+(?:{_WORD}))*)"
)


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
    if "linkedin" in name or "linkedin" in parent:
        return "linkedin"
    if "promptorgtfo" in name or "promptorgtfo" in parent:
        return "promptorgtfo"
    if isinstance(data, dict):
        manifest = ((data.get("source") or {}).get("manifest") or {})
        if clean_text(manifest.get("code", "")).lower().startswith("defcon"):
            return "defcon"
        config_source = clean_text((data.get("config") or {}).get("source", ""))
        if config_source in {"feed", "saved"}:
            return "linkedin"
        if "playlist" in data and "records" in data:
            records = data.get("records") or []
            if records and isinstance(records[0], dict) and "talk_title" in records[0]:
                return "youtube_playlist"
    elif isinstance(data, list):
        if data and isinstance(data[0], dict) and "summary" in data[0] and "transcript_available" in data[0]:
            return "promptorgtfo"
    return "unknown"


CONFERENCE_RECORD_SOURCES = {"blackhat", "camlis", "bsideslv", "rsac", "bsidessf"}


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
    if (source in CONFERENCE_RECORD_SOURCES or re.fullmatch(r"defcon\d+", source)) and title:
        event_key = _dedupe_component(year or event)
        material = "\n".join([source, event_key, title.lower(), author.lower()])
        return f"{source}:{event_key}:title-author:{stable_hash(material)}"
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


def records_from_linkedin(data: dict[str, Any], source_file: Path) -> list[KnowledgeRecord]:
    records = []
    source_name = f"linkedin_{clean_text((data.get('config') or {}).get('source', 'post'))}"
    ingested_at = clean_text(data.get("ingested_at", ""))
    year = ingested_at[:4] if ingested_at else ""
    for post in data.get("posts", []):
        text = clean_text(post.get("text", ""))
        title = text[:120]
        records.append(
            make_record(
                source=source_name,
                source_file=source_file,
                source_record_id=post.get("url", ""),
                title=title,
                author=post.get("author", ""),
                text=text,
                url=post.get("url", ""),
                event="LinkedIn",
                year=year,
                tags=post.get("source", ""),
                raw=post,
            )
        )
    return records


def records_from_linkedin_db(linkedin_db_path: Path = LINKEDIN_DB_PATH) -> list[KnowledgeRecord]:
    if not linkedin_db_path.exists():
        return []
    conn = sqlite3.connect(linkedin_db_path)
    conn.row_factory = sqlite3.Row
    try:
        rows = list(
            conn.execute(
                """
                SELECT
                    p.*,
                    COALESCE(
                        (
                            SELECT o.source
                            FROM post_observations o
                            WHERE o.post_id = p.id
                            ORDER BY o.seen_at DESC, o.id DESC
                            LIMIT 1
                        ),
                        p.source_first_seen
                    ) AS latest_source
                FROM linkedin_posts p
                ORDER BY p.id
                """
            )
        )
    finally:
        conn.close()

    records = []
    for row in rows:
        raw = {}
        try:
            raw = json.loads(row["raw_json"] or "{}")
        except json.JSONDecodeError:
            raw = {key: row[key] for key in row.keys()}
        source = clean_text(row["latest_source"] or row["source_first_seen"] or raw.get("source") or "post")
        if source == "feed":
            continue
        text = clean_text(row["text"])
        records.append(
            make_record(
                source=f"linkedin_{source}",
                source_file=linkedin_db_path,
                source_record_id=row["dedupe_key"],
                title=text[:120],
                author=row["author"],
                text=text,
                url=row["url"],
                event="LinkedIn",
                year=clean_text(row["first_seen_at"])[:4],
                tags=source,
                raw={**raw, "linkedin_db_id": row["id"], "dedupe_key": row["dedupe_key"]},
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


def records_from_bsidessf_md(path: Path) -> list[KnowledgeRecord]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    in_schedule = False
    schedule_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^#\s+(?:Saturday|Sunday),\s+April", stripped, re.IGNORECASE):
            in_schedule = True
        elif in_schedule and re.match(
            r"^#\s+(?:Many\s+Thanks|Ctf\s+Cross|Customers\s+Rate|Navigate\s+The)", stripped, re.IGNORECASE
        ):
            break
        if in_schedule:
            schedule_lines.append(stripped)

    blocks: list[list[str]] = []
    current: list[str] = []
    for line in schedule_lines:
        if _TIME_BLOCK_RE.match(line):
            if current:
                blocks.append(current)
            current = [line]
        elif line:
            current.append(line)
    if current:
        blocks.append(current)

    records = []
    for block in blocks:
        if len(block) < 3:
            continue

        time_str = block[0]
        rest = block[1:]

        venue = ""
        if rest and re.search(r"(?:METREON|THEATER|IMAX)", rest[0], re.IGNORECASE):
            venue = rest[0]
            rest = rest[1:]

        while rest and _TYPE_MARKER_RE.match(rest[0]):
            rest = rest[1:]

        if not rest:
            continue

        title = rest[0]
        body_lines = rest[1:]

        speaker = ""
        if body_lines:
            m = _SPEAKER_NAME_RE.match(body_lines[0])
            if m:
                speaker = m.group(1)

        full_text = " ".join(body_lines)
        if not full_text and not title:
            continue

        combined_text = (title + " " + full_text).strip() if full_text else title

        records.append(
            make_record(
                source="bsidessf",
                source_file=path,
                source_record_id=f"{time_str}|{venue}|{title[:80]}",
                title=title,
                author=speaker,
                text=combined_text,
                url="",
                event="BSidesSF 2025",
                year="2025",
                tags=venue,
                raw={"time": time_str, "venue": venue, "title": title, "speaker": speaker, "text": full_text},
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
        if kind == "linkedin":
            return records_from_linkedin(data, path)
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


def sync_linkedin_db(
    db_path: Path = DB_PATH,
    linkedin_db_path: Path = LINKEDIN_DB_PATH,
    rebuild_linkedin: bool = True,
) -> dict[str, int]:
    stats = {"records": 0, "inserted": 0, "updated": 0, "errors": 0}
    try:
        records = records_from_linkedin_db(linkedin_db_path)
    except Exception as exc:
        log_warning(f"error reading linkedin db {linkedin_db_path}: {exc}")
        return stats
    if not records:
        log_warning(f"0 records from {linkedin_db_path}")
    with open_db(db_path) as conn:
        if rebuild_linkedin:
            linkedin_ids = [
                row["id"]
                for row in conn.execute(
                    "SELECT id FROM records WHERE source IN ('linkedin_feed', 'linkedin_saved', 'linkedin_post')"
                )
            ]
            if linkedin_ids:
                placeholders = ", ".join("?" for _ in linkedin_ids)
                conn.execute(f"DELETE FROM records_fts WHERE rowid IN ({placeholders})", linkedin_ids)
                conn.execute(f"DELETE FROM records WHERE id IN ({placeholders})", linkedin_ids)
        for record in records:
            stats["records"] += 1
            try:
                if upsert_record(conn, record):
                    stats["inserted"] += 1
                else:
                    stats["updated"] += 1
            except Exception as exc:
                log_warning(f"upsert error [{record.source}] {record.title[:60]!r}: {exc}")
                stats["errors"] += 1
        conn.commit()
    return stats


def default_export_paths(latest_per_source: bool = True) -> list[Path]:
    groups = [
        sorted((APP_DIR / "data" / "blackhat" / "exports").glob("*.json")),
        sorted((APP_DIR / "data" / "camlis" / "exports").glob("*.json")),
        sorted((APP_DIR / "data" / "linkedin" / "exports").glob("*.json")),
    ]
    if latest_per_source:
        paths = [group[-1] for group in groups if group]
    else:
        paths = [path for group in groups for path in group]
    for fixed in (DEFCON33_LATEST, PROMPTORGTFO_LATEST):
        if fixed is not None and fixed.exists() and fixed not in paths:
            paths.append(fixed)
    return paths


def import_markdown_sources(db_path: Path = DB_PATH) -> dict[str, int]:
    stats = {"records": 0, "inserted": 0, "updated": 0, "errors": 0}
    sources = [BSIDESSF_MD]
    with open_db(db_path) as conn:
        for path in sources:
            if not path.exists():
                log_warning(f"skip (not found): {path}")
                continue
            try:
                records = records_from_bsidessf_md(path)
            except Exception as exc:
                log_warning(f"parser error {path}: {exc}")
                continue
            if not records:
                log_warning(f"skip (0 records): {path}")
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
        conn.commit()
    return stats
