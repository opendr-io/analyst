import json
import math
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from .knowledge_config import BAD_TOPIC_PHRASES, BAD_TOPIC_TOKENS, DB_PATH, SEED_TOPICS, STATE_DIR, STOPWORDS
from .knowledge_db import log_info, open_db, utc_now_iso
from .knowledge_records import decode_topics


def tokens_for_topics(value: str) -> list[str]:
    tokens = re.findall(r"[a-zA-Z][a-zA-Z0-9+\-]{1,}", value.lower())
    return [token for token in tokens if token not in STOPWORDS and not token.isdigit()]


def phrase_candidates(text: str, max_ngram: int = 3) -> set[str]:
    tokens = tokens_for_topics(text)
    phrases: set[str] = set()
    for size in range(2, max_ngram + 1):
        for idx in range(0, max(len(tokens) - size + 1, 0)):
            phrase_tokens = tokens[idx : idx + size]
            if len(phrase_tokens) != size:
                continue
            if any(token in STOPWORDS for token in phrase_tokens):
                continue
            if any(token in BAD_TOPIC_TOKENS for token in phrase_tokens):
                continue
            if len(set(phrase_tokens)) != len(phrase_tokens):
                continue
            phrase = " ".join(phrase_tokens)
            if any(bad_phrase in phrase for bad_phrase in BAD_TOPIC_PHRASES):
                continue
            if len(phrase) >= 4:
                phrases.add(phrase)
    return phrases


def discover_topic_candidates(
    db_path: Path = DB_PATH,
    limit: int = 40,
    min_records: int = 3,
    source: str = "",
) -> list[dict[str, Any]]:
    sql = "SELECT id, source, title, text, tags FROM records"
    params: list[Any] = []
    if source:
        sql += " WHERE source = ?"
        params.append(source)
    with open_db(db_path) as conn:
        rows = list(conn.execute(sql, params))

    record_count = len(rows)
    phrase_records: dict[str, set[int]] = defaultdict(set)
    phrase_sources: dict[str, set[str]] = defaultdict(set)
    phrase_samples: dict[str, list[int]] = defaultdict(list)

    for row in rows:
        material = " ".join([row["title"], row["tags"], row["text"][:2000]])
        for phrase in phrase_candidates(material):
            phrase_records[phrase].add(row["id"])
            phrase_sources[phrase].add(row["source"])
            if len(phrase_samples[phrase]) < 5:
                phrase_samples[phrase].append(row["id"])

    candidates = []
    for phrase, ids in phrase_records.items():
        count = len(ids)
        if count < min_records:
            continue
        words = phrase.split()
        if len(words) < 2:
            continue
        specificity = 1.0 + (0.85 * (len(words) - 1))
        source_bonus = 1.0 + (0.12 * (len(phrase_sources[phrase]) - 1))
        score = count * specificity * source_bonus * math.log(record_count + 1)
        candidates.append(
            {
                "phrase": phrase,
                "score": score,
                "record_count": count,
                "sources": sorted(phrase_sources[phrase]),
                "sample_record_ids": phrase_samples[phrase],
            }
        )

    candidates.sort(key=lambda item: (-item["score"], item["phrase"]))
    return candidates[:limit]


def store_topic_candidates(db_path: Path, candidates: list[dict[str, Any]]) -> dict[str, Any]:
    now = utc_now_iso()
    with open_db(db_path) as conn:
        existing = {
            row["phrase"]
            for row in conn.execute("SELECT phrase FROM topic_candidates").fetchall()
        }
        conn.execute("DELETE FROM topic_candidates")
        for candidate in candidates:
            conn.execute(
                """
                INSERT INTO topic_candidates (
                    phrase, score, record_count, sources, sample_record_ids, created_at, updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(phrase) DO UPDATE SET
                    score = excluded.score,
                    record_count = excluded.record_count,
                    sources = excluded.sources,
                    sample_record_ids = excluded.sample_record_ids,
                    updated_at = excluded.updated_at
                """,
                (
                    candidate["phrase"],
                    candidate["score"],
                    candidate["record_count"],
                    ", ".join(candidate["sources"]),
                    json.dumps(candidate["sample_record_ids"]),
                    now,
                    now,
                ),
            )
        conn.commit()
    added = [candidate["phrase"] for candidate in candidates if candidate["phrase"] not in existing]
    if added:
        preview = ", ".join(added[:10])
        suffix = "" if len(added) <= 10 else f", +{len(added) - 10} more"
        log_info(f"candidate topics added: {len(added)} ({preview}{suffix})")
    else:
        log_info(f"candidate topics refreshed: {len(candidates)} candidates, 0 added")
    return {
        "stored": len(candidates),
        "added": len(added),
        "added_phrases": added,
    }


def refresh_topic_catalog(
    db_path: Path = DB_PATH,
    candidate_limit: int = 50,
    min_records: int = 3,
    source_candidate_limit: int = 3,
    source: str = "",
    output_path: Path | None = None,
    seed_curated: bool = True,
) -> dict[str, Any]:
    """
    Refresh curated and discovered topics after ingest.

    Candidate topics are mined from indexed record text and exported with the
    curated list for review. When seed_curated is true, curated seed topics are
    also synced into the topics table.
    """
    seed_count = seed_topics(db_path) if seed_curated else 0
    candidates = discover_topic_candidates(
        db_path=db_path,
        limit=candidate_limit,
        min_records=min_records,
        source=source,
    )
    if not source and source_candidate_limit > 0:
        with open_db(db_path) as conn:
            sources = [
                row["source"]
                for row in conn.execute("SELECT DISTINCT source FROM records ORDER BY source").fetchall()
            ]
        seen = {candidate["phrase"].casefold() for candidate in candidates}
        for source_name in sources:
            source_candidates = discover_topic_candidates(
                db_path=db_path,
                limit=source_candidate_limit,
                min_records=min_records,
                source=source_name,
            )
            for candidate in source_candidates:
                key = candidate["phrase"].casefold()
                if key in seen:
                    continue
                candidates.append(candidate)
                seen.add(key)
    candidate_stats = store_topic_candidates(db_path, candidates)
    topic_list_path = export_topic_list(db_path, output_path)
    return {
        "seed_topics": seed_count,
        "candidate_topics": len(candidates),
        "candidate_topics_added": candidate_stats["added"],
        "candidate_topics_added_phrases": candidate_stats["added_phrases"],
        "topic_list_path": str(topic_list_path),
    }


def list_classification_topics(
    db_path: Path = DB_PATH,
    include_candidates: bool = True,
    candidate_limit: int = 0,
) -> list[str]:
    """
    Return topic names the classifier should use.

    Falls back to SEED_TOPICS if the topics table has not been seeded yet.
    Candidate phrases are included after curated topics so newly recurring
    themes can be classified without manually editing SEED_TOPICS first.
    """
    seen: set[str] = set()
    topics: list[str] = []

    def add_topic(name: str) -> None:
        clean = " ".join((name or "").split())
        if not clean:
            return
        key = clean.casefold()
        if key in seen:
            return
        seen.add(key)
        topics.append(clean)

    with open_db(db_path) as conn:
        rows = conn.execute("SELECT name FROM topics ORDER BY id").fetchall()
        if rows:
            for row in rows:
                add_topic(row["name"])
        else:
            for name, _query in SEED_TOPICS:
                add_topic(name)

        if include_candidates:
            if candidate_limit and candidate_limit > 0:
                candidate_rows = conn.execute(
                    """
                    SELECT phrase
                    FROM topic_candidates
                    ORDER BY score DESC, phrase
                    LIMIT ?
                    """,
                    (candidate_limit,),
                ).fetchall()
            else:
                candidate_rows = conn.execute(
                    """
                    SELECT phrase
                    FROM topic_candidates
                    ORDER BY score DESC, phrase
                    """
                ).fetchall()
            for row in candidate_rows:
                add_topic(row["phrase"])

    return topics


def seed_topics(db_path: Path = DB_PATH) -> int:
    now = utc_now_iso()
    seed_names = [name for name, _definition in SEED_TOPICS]
    placeholders = ", ".join("?" for _name in seed_names)
    with open_db(db_path) as conn:
        if seed_names:
            conn.execute(
                f"DELETE FROM topics WHERE source = 'seed' AND name NOT IN ({placeholders})",
                seed_names,
            )
        else:
            conn.execute("DELETE FROM topics WHERE source = 'seed'")
        for name, definition in SEED_TOPICS:
            conn.execute(
                """
                INSERT INTO topics (name, query, description, source, created_at, updated_at)
                VALUES (?, ?, ?, 'seed', ?, ?)
                ON CONFLICT(name) DO UPDATE SET
                    query = excluded.query,
                    description = excluded.description,
                    source = excluded.source,
                    updated_at = excluded.updated_at
                """,
                (name, definition, definition, now, now),
            )
        conn.commit()
    return len(SEED_TOPICS)


def export_topic_list(db_path: Path = DB_PATH, output_path: Path | None = None) -> Path:
    output_path = output_path or (STATE_DIR / "topic-list.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open_db(db_path) as conn:
        topics = list(conn.execute("SELECT name, query, description, source FROM topics ORDER BY id"))
        candidates = list(
            conn.execute(
                """
                SELECT phrase, score, record_count, sources, sample_record_ids
                FROM topic_candidates
                ORDER BY score DESC, phrase
                """
            )
        )

    lines = [
        "Knowledge Topic List",
        f"Generated: {utc_now_iso()}",
        "",
        "Curated Topics",
        "==============",
    ]
    if topics:
        for idx, row in enumerate(topics, start=1):
            lines.append(f"{idx}. {row['name']}")
            lines.append(f"   definition: {row['description'] or row['query']}")
            if row["description"] and row["description"] != row["query"]:
                lines.append(f"   notes: {row['description']}")
    else:
        lines.append("(none)")

    lines.extend(["", "Discovered Candidate Topics", "=========================="])
    if candidates:
        for idx, row in enumerate(candidates, start=1):
            lines.append(
                f"{idx}. {row['phrase']} "
                f"(records={row['record_count']}, sources={row['sources']}, samples={row['sample_record_ids']})"
            )
    else:
        lines.append("(none)")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_path


def _load_json_list(value: str | None) -> list[str]:
    if not value:
        return []
    try:
        loaded = json.loads(value)
    except json.JSONDecodeError:
        return []
    if not isinstance(loaded, list):
        return []
    return [" ".join(str(item).split()) for item in loaded if " ".join(str(item).split())]


def export_topic_keyword_candidates(
    db_path: Path = DB_PATH,
    output_path: Path | None = None,
    limit_per_topic: int = 40,
    min_records: int = 2,
) -> Path:
    output_path = output_path or (STATE_DIR / "topic-keyword-candidates.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    topic_names = list_classification_topics(db_path, include_candidates=False)
    topic_keywords: dict[str, Counter[str]] = {topic: Counter() for topic in topic_names}
    topic_tools: dict[str, Counter[str]] = {topic: Counter() for topic in topic_names}
    topic_use_cases: dict[str, Counter[str]] = {topic: Counter() for topic in topic_names}
    topic_record_counts: dict[str, int] = {topic: 0 for topic in topic_names}

    with open_db(db_path) as conn:
        rows = list(
            conn.execute(
                """
                SELECT
                    records.id,
                    records.agent_topics,
                    record_annotations.keywords_json,
                    record_annotations.tools_json,
                    record_annotations.use_cases_json
                FROM records
                JOIN record_annotations ON record_annotations.record_id = records.id
                WHERE records.agent_topics != ''
                ORDER BY records.id
                """
            )
        )

    for row in rows:
        topics = [topic for topic in decode_topics(row["agent_topics"]) if topic in topic_keywords]
        if not topics:
            continue
        keywords = _load_json_list(row["keywords_json"])
        tools = _load_json_list(row["tools_json"])
        use_cases = _load_json_list(row["use_cases_json"])
        for topic in topics:
            topic_record_counts[topic] += 1
            topic_keywords[topic].update(item.casefold() for item in keywords)
            topic_tools[topic].update(item.casefold() for item in tools)
            topic_use_cases[topic].update(item.casefold() for item in use_cases)

    def ranked(counter: Counter[str]) -> list[tuple[str, int]]:
        return [
            (term, count)
            for term, count in counter.most_common()
            if count >= min_records and term not in STOPWORDS and term not in BAD_TOPIC_TOKENS
        ][:limit_per_topic]

    lines = [
        "# Topic Keyword Candidates",
        "",
        f"Generated: {utc_now_iso()}",
        f"Minimum records per candidate: {min_records}",
        f"Maximum candidates per section: {limit_per_topic}",
        "",
        "Review these candidates before using them for classification. They are mined from annotations on records already assigned to each curated topic.",
        "",
    ]
    for topic in topic_names:
        lines.extend([
            f"## {topic}",
            "",
            f"Current topic definition: {dict(SEED_TOPICS).get(topic, '')}",
            f"Classified annotated records: {topic_record_counts[topic]}",
            "",
            "### Keyword Candidates",
        ])
        candidates = ranked(topic_keywords[topic])
        lines.extend([f"- {term} ({count})" for term, count in candidates] or ["- (none)"])
        lines.extend(["", "### Tool/Project Candidates"])
        candidates = ranked(topic_tools[topic])
        lines.extend([f"- {term} ({count})" for term, count in candidates] or ["- (none)"])
        lines.extend(["", "### Use Case Candidates"])
        candidates = ranked(topic_use_cases[topic])
        lines.extend([f"- {term} ({count})" for term, count in candidates] or ["- (none)"])
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path
