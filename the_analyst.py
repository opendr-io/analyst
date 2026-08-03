#!/usr/bin/env python3
"""
Knowledge base Q&A agent with tool use.

One-shot:
    python the_or.py "What tools exist for MCP sandboxing?"

Interactive:
    python the_analyst.py
"""

import argparse
from dataclasses import dataclass
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

load_dotenv()

APP_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(APP_DIR))
from knowledge_agenting import knowledge_agent as ka
from knowledge_agenting.common import load_prompt
from knowledge_indexing import knowledge_index as ki
import llm_client
from config import llm_settings
from knowledge_agenting.topic_summarizer import SMALL_TOPIC_MAX_RECORDS, summarize_topic as summarize_topic_to_files

MODEL = llm_settings.get_model("qa")
SUMMARY_DIR = APP_DIR / "summaries"
TOPIC_ROUTING_ALIASES_PATH = APP_DIR / "config" / "topic_routing_aliases.tsv"
QA_MAX_OUTPUT_TOKENS = llm_settings.get_int("qa", "max_output_tokens")

ORACLE_BANNER = r"""

[0;91;1;40m▄[0;93;1;40m█[0;93;1;43m███████[0;37;40m [0;91;1;40m▄[0;93;1;43m██[0;37;40m [0;91;1;40m▄[0;93;1;43m██[0;37;40m [0;91;1;40m▄[0;93;1;43m██████[0;37;40m      [0;91;1;40m▄[0;93;1;43m██████[0;37;40m [0;91;1;40m▄[0;93;1;43m██████[0;37;40m [0;91;1;40m▄[0;93;1;43m██████[0;37;40m [0;91;1;40m▄[0;93;1;43m██[0;37;40m     [0;91;1;40m▄[0;93;1;43m██[0;37;40m [0;91;1;40m▄[0;93;1;43m██[0;37;40m [0;91;1;40m▄[0;93;1;43m██████[0;37;40m [0;91;1;40m▄[0;93;1;40m█[0;93;1;43m███████[0m
[0;91;1;40m▀▀▀█[0;93;1;43m█▓[0;91;1;40m▀▀[0;37;40m  [0;91;1;40m█[0;93;1;43m█▓[0;37;40m [0;91;1;40m█[0;93;1;43m▓█[0;37;40m [0;91;1;40m█[0;93;1;43m█▓[0;91;1;40m▀▀▀[0;37;40m       [0;91;1;40m█[0;93;1;43m█▓[0;91;1;40m▀█[0;93;1;43m▓█[0;37;40m [0;91;1;40m█[0;93;1;43m█▓[0;91;1;40m▀█[0;93;1;43m▓█[0;37;40m [0;91;1;40m█[0;93;1;43m█▓[0;91;1;40m▀█[0;93;1;43m▓█[0;37;40m [0;91;1;40m█[0;93;1;43m█▓[0;37;40m     [0;91;1;40m█[0;93;1;43m█▓[0;37;40m [0;91;1;40m█[0;93;1;43m▓█[0;37;40m [0;91;1;40m█[0;93;1;43m█▓[0;91;1;40m▀▀▀[0;37;40m  [0;91;1;40m▀▀▀█[0;93;1;43m█▓[0;91;1;40m▀▀[0;37;40m [0m
[0;37;40m   [0;91;1;40m█[0;93;1;43m▓▓[0;37;40m    [0;91;1;40m█[0;93;1;43m▓▒▓▒▒▓[0;37;40m [0;91;1;40m█[0;93;1;43m▓▓▒▓▒[0;37;40m       [0;91;1;40m█[0;93;1;43m▓▒▓▒▒▓[0;37;40m [0;91;1;40m█[0;93;1;43m▓▒[0;37;40m [0;91;1;40m█[0;93;1;43m▒▓[0;37;40m [0;91;1;40m█[0;93;1;43m▓▒▓▒▒▓[0;37;40m [0;91;1;40m█[0;93;1;43m▓▓[0;37;40m     [0;91;1;40m█[0;93;1;43m▓▓▒▓▒▓[0;37;40m [0;91;1;40m█[0;93;1;43m▓▓▒▓▒▒[0;37;40m    [0;91;1;40m█[0;93;1;43m▓▓[0;37;40m   [0m
[0;37;40m   [0;91;1;40m█[0;93;1;43m▒░[0;37;40m    [0;91;1;40m█[0;93;1;43m▒░[0;91;1;40m▀█[0;93;1;43m░▒[0;37;40m [0;91;1;40m█[0;93;1;43m▒░[0;91;1;40m▀▀[0;37;40m        [0;91;1;40m█[0;93;1;43m▒░[0;91;1;40m▀█[0;93;1;43m░▒[0;37;40m [0;91;1;40m█[0;93;1;43m▒░[0;37;40m [0;91;1;40m█[0;93;1;43m░▒[0;37;40m [0;91;1;40m█[0;93;1;43m▒░[0;91;1;40m▀█[0;93;1;43m░▒[0;37;40m [0;91;1;40m█[0;93;1;43m▒░[0;37;40m     [0;91;1;40m▀▀█[0;93;1;43m░░[0;91;1;40m▀[0;37;40m  [0;91;1;40m▀▀▀▀█[0;93;1;43m░▒[0;37;40m    [0;91;1;40m█[0;93;1;43m▒░[0;37;40m   [0m
[0;37;40m   [0;91;1;40m█[0;93;1;43m░ [0;37;40m    [0;91;1;40m█[0;93;1;43m░ [0;37;40m [0;91;1;40m█[0;93;1;43m ░[0;37;40m [0;91;1;40m█[0;93;1;43m░     [0;37;40m      [0;91;1;40m█[0;93;1;43m░ [0;37;40m [0;91;1;40m█[0;93;1;43m ░[0;37;40m [0;91;1;40m█[0;93;1;43m░ [0;37;40m [0;91;1;43m█[0;93;1;43m ░[0;37;40m [0;91;1;40m█[0;93;1;43m░ [0;37;40m [0;91;1;40m█[0;93;1;43m ░[0;37;40m [0;91;1;40m█[0;93;1;43m░     [0;37;40m   [0;91;1;40m█[0;93;1;43m░ [0;37;40m   [0;91;1;40m▄[0;91;1;43m     [0;93;1;43m░[0;37;40m    [0;91;1;40m█[0;93;1;43m░ [0;37;40m   [0m
[0;37;40m   [0;91;1;40m▀▀▀[0;37;40m    [0;91;1;40m▀▀▀[0;37;40m [0;91;1;40m▀▀[0;37;40m  [0;91;1;40m▀▀▀▀▀▀[0;37;40m       [0;91;1;40m▀▀▀[0;37;40m [0;91;1;40m▀▀[0;37;40m  [0;91;1;40m▀▀▀[0;37;40m [0;91;1;40m▀▀[0;37;40m  [0;91;1;40m▀▀▀[0;37;40m [0;91;1;40m▀▀[0;37;40m  [0;91;1;40m▀▀▀▀▀▀[0;37;40m    [0;91;1;40m▀▀[0;37;40m    [0;91;1;40m▀▀▀▀▀▀[0;37;40m     [0;91;1;40m▀▀▀[0;37;40m   [0m
            Maybe there are other ways to understand what happened..                                                                      

"""

QUERY_SYNONYMS: dict[str, tuple[str, ...]] = {
    "appsec": ("application security", "application testing"),
    "apps": ("applications", "application security"),
    "application": ("appsec", "application security", "software security"),
    "applications": ("application", "appsec", "application security", "software security"),
    "auth": ("authentication", "authorization", "identity access"),
    "authentication": (
        "auth",
        "authorization",
        "access control",
        "identity access",
        "oauth",
        "mfa",
    ),
    "authorization": ("authentication", "access control", "identity access", "oauth"),
    "broken": ("vulnerability", "misconfiguration", "bypass"),
    "missing": ("absent", "unauthenticated", "access control"),
    "test": ("testing", "assessment", "evaluation"),
    "testing": ("test", "assessment", "evaluation"),
    "pentest": ("penetration testing", "security testing", "vulnerability discovery"),
    "pentesting": ("penetration testing", "security testing", "vulnerability discovery"),
    "agentic": ("agentic ai", "application security", "ai agents"),
    "agents": ("agentic ai", "application security", "ai agents"),
    "llm": ("large language model",),
    "mcp": ("model context protocol",),
    "oauth": ("identity access delegation", "authentication authorization"),
    "rag": ("retrieval augmented generation", "graphrag"),
    "web": ("web application", "application security"),
}

QUERY_PHRASE_EXPANSIONS: tuple[tuple[tuple[str, ...], tuple[str, ...]], ...] = (
    (
        ("applications", "test"),
        (
            "application security testing",
            "appsec",
            "vulnerability discovery",
            "penetration testing",
            "application security",
        ),
    ),
    (
        ("apps", "test"),
        (
            "application security testing",
            "appsec",
            "vulnerability discovery",
            "penetration testing",
            "application security",
        ),
    ),
    (
        ("appsec", "testing"),
        ("application security testing", "vulnerability discovery", "penetration testing"),
    ),
    (
        ("agentic", "appsec"),
        ("application security", "ai agent security testing"),
    ),
    (
        ("broken", "authentication"),
        (
            "oauth identity and access delegation",
            "authentication authorization",
            "access control testing",
            "authentication bypass",
            "missing authentication",
            "web application security testing",
        ),
    ),
    (
        ("missing", "authentication"),
        (
            "oauth identity and access delegation",
            "authentication authorization",
            "access control testing",
            "unauthenticated access",
            "web application security testing",
        ),
    ),
    (
        ("web", "applications"),
        ("web application security", "appsec", "application security testing"),
    ),
)

ORACLE_SYSTEM_PROMPT = APP_DIR / "knowledge_agenting" / "prompts" / "oracle_system.txt"
AGENT_SYSTEM = load_prompt("oracle_system.txt")
DEFAULT_SUMMARY_QUESTION_TOPICS = 3

TOOLS = [
    {
        "name": "get-status",
        "description": (
            "Report the current state of the knowledge index and classification pipeline: "
            "record counts by source, unclassified count, last import and classification "
            "timestamps, topic summary dates, and recent errors from the import log."
        ),
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "search-records",
        "description": (
            "Deterministically search the knowledge database for compact matching records by "
            "author name, talk title, tool name, URL, or keyword. Use for lookup and evidence "
            "discovery, not broad synthesis."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search term, author name, talk title, tool name, or keyword.",
                },
                "topic": {
                    "type": "string",
                    "description": "Optional: limit results to records tagged with this topic",
                },
                "limit": {
                    "type": "integer",
                    "description": "Optional max records to return. If omitted, all gathered matches are returned.",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "query-annotations",
        "description": (
            "Deterministically query structured record annotations by keyword, tool, person, "
            "claim, use case, security domain, AI relevance, or relevance note. Use for "
            "requests to find/list/show records matching annotation keywords, not for broad "
            "research synthesis."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "keywords": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Annotation keywords or phrases to match.",
                },
                "query": {
                    "type": "string",
                    "description": "Optional free-text query; used if keywords is omitted.",
                },
                "topic": {
                    "type": "string",
                    "description": "Optional topic filter using records.agent_topics.",
                },
                "source": {
                    "type": "string",
                    "description": "Optional source filter such as defcon33, blackhat, or promptorgtfo.",
                },
                "match": {
                    "type": "string",
                    "enum": ["any", "all"],
                    "description": "Whether any or all keywords must match. Default any.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Optional max annotation matches to return. If omitted, all gathered matches are returned.",
                },
            },
            "required": [],
        },
    },
    {
        "name": "answer-from-summaries",
        "description": (
            "Answer a broad research question using synthesized topic summary files and PDF document summaries. "
            "Better than search-records for questions about trends, themes, open problems, "
            "the overall state of a research area, or what multiple documents agree on."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "Optional: focus on a specific topic's summary file",
                },
                "question": {
                    "type": "string",
                    "description": "Original user question, used to rank the most relevant topics",
                },
                "max_topics": {
                    "type": "integer",
                    "description": "Optional maximum summary files to load. Defaults to 3.",
                },
            },
            "required": [],
        },
    },
    {
        "name": "answer-about-author",
        "description": (
            "Load evidence for a named author or speaker. Authors with multiple records use "
            "their generated author summary; authors with one record return that complete record."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "author": {
                    "type": "string",
                    "description": "Exact author or speaker name",
                },
            },
            "required": ["author"],
        },
    },
    {
        "name": "generate-topic-summary",
        "description": (
            "Regenerate the research summary for a specific topic using all classified records. "
            "Use when the user asks for a fresh, updated, or new summary of a topic."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "Exact topic name to summarize",
                },
            },
            "required": ["topic"],
        },
    },
]


def plan_search_query(question: str) -> str:
    tokens = re.findall(r"[a-zA-Z][a-zA-Z0-9+\-]{2,}", question.lower())
    search_terms: list[str] = []
    seen: set[str] = set()

    def add(term: str) -> None:
        normalized = term.strip().lower()
        if normalized and normalized not in seen:
            seen.add(normalized)
            search_terms.append(normalized)

    for token in tokens:
        if token not in ki.STOPWORDS:
            add(token)
        singular = token[:-1] if len(token) > 4 and token.endswith("s") else ""
        if singular and singular not in ki.STOPWORDS:
            add(singular)
        for synonym in QUERY_SYNONYMS.get(token, ()):
            add(synonym)
        if singular:
            for synonym in QUERY_SYNONYMS.get(singular, ()):
                add(synonym)

    token_set = set(tokens)
    for required, expansions in QUERY_PHRASE_EXPANSIONS:
        if all(term in token_set for term in required):
            for expansion in expansions:
                add(expansion)

    return " ".join(search_terms) if search_terms else question


def _fts_phrase(token: str) -> str:
    return f'"{token.replace(chr(34), chr(34) + chr(34))}"'


def question_to_fts_query(question: str) -> str:
    planned = plan_search_query(question)
    original_tokens = re.findall(r"[a-zA-Z][a-zA-Z0-9+\-]{2,}", question.lower())
    planned_tokens = re.findall(r"[a-zA-Z][a-zA-Z0-9+\-]{2,}", planned.lower())
    tokens: list[str] = []
    seen: set[str] = set()
    for token in [*original_tokens, *planned_tokens]:
        if token in ki.STOPWORDS or token in seen:
            continue
        seen.add(token)
        tokens.append(token)
    return " OR ".join(_fts_phrase(token) for token in tokens[:16])


def _topic_slug(topic: str) -> str:
    slug = topic.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def focus_routing_question(question: str) -> str:
    """Prefer the asserted subject over an explicitly rejected distractor."""
    question_l = question.lower()
    real_issue_marker = "but the real issue is "
    if real_issue_marker in question_l:
        marker_at = question_l.index(real_issue_marker) + len(real_issue_marker)
        return question[marker_at:]

    not_marker = ", not "
    if question_l.startswith("this is about ") and not_marker in question_l:
        subject_start = len("this is about ")
        subject_end = question_l.index(not_marker)
        return question[subject_start:subject_end]
    return question


@dataclass(frozen=True)
class SummaryFile:
    topic: str
    path: Path
    source: str


def _tokens(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-zA-Z][a-zA-Z0-9+\-]{2,}", value.lower())
        if token not in ki.STOPWORDS and token not in ki.BAD_TOPIC_TOKENS
    }


def rank_relevant_topics(question: str, topics: list[str], limit: int = 5) -> list[tuple[str, float]]:
    planned_question = plan_search_query(question)
    question_tokens = _tokens(planned_question)
    original_question_tokens = _tokens(question)
    if not question_tokens:
        return []

    ranked: list[tuple[str, float]] = []
    question_l = planned_question.lower()
    original_question_l = question.lower()
    for topic in topics:
        topic_tokens = _tokens(topic)
        if not topic_tokens:
            continue
        overlap = question_tokens & topic_tokens
        original_overlap = original_question_tokens & topic_tokens
        if not overlap and topic.lower() not in question_l:
            continue
        score = float(len(original_overlap) * 4)
        score += float(len(overlap - original_overlap) * 2)
        if topic.lower() in original_question_l:
            score += 8.0
        elif topic.lower() in question_l:
            score += 3.0
        topic_parts = topic.lower().split()
        for first, second in zip(topic_parts, topic_parts[1:]):
            if f"{first} {second}" in original_question_l:
                score += 6.0
        score += len(overlap) / max(len(topic_tokens), 1)
        ranked.append((topic, score))

    ranked.sort(key=lambda item: (-item[1], item[0].lower()))
    return ranked[:limit]


def _score_topic_text(question: str, topic_name: str, search_text: str) -> float:
    planned_question = plan_search_query(question)
    question_tokens = _tokens(planned_question)
    original_question_tokens = _tokens(question)
    topic_tokens = _tokens(search_text)
    if not question_tokens or not topic_tokens:
        return 0.0
    overlap = question_tokens & topic_tokens
    original_overlap = original_question_tokens & topic_tokens
    topic_l = topic_name.lower()
    search_l = search_text.lower()
    question_l = planned_question.lower()
    original_question_l = question.lower()
    if not overlap and topic_l not in question_l and search_l not in question_l:
        return 0.0
    score = float(len(original_overlap) * 4)
    score += float(len(overlap - original_overlap) * 2)
    if topic_l in original_question_l:
        score += 8.0
    elif topic_l in question_l:
        score += 3.0
    topic_parts = topic_l.split()
    for first, second in zip(topic_parts, topic_parts[1:]):
        if f"{first} {second}" in original_question_l:
            score += 6.0
    question_parts = re.findall(r"[a-zA-Z0-9][a-zA-Z0-9+\-]{1,}", original_question_l)
    for first, second in zip(question_parts, question_parts[1:]):
        phrase = f"{first} {second}"
        if (
            first not in ki.STOPWORDS
            and second not in ki.STOPWORDS
            and phrase in search_l
        ):
            score += 4.0
    question_numbers = set(re.findall(r"(?<!\d)\d{2,4}(?!\d)", original_question_l))
    topic_numbers = set(re.findall(r"(?<!\d)\d{2,4}(?!\d)", search_l))
    if question_numbers:
        matched_numbers = question_numbers & topic_numbers
        score += float(len(matched_numbers) * 8)
        if topic_numbers and not matched_numbers:
            score -= 3.0
    score += len(overlap) / max(len(topic_tokens), 1)
    return score

def _topic_from_summary_path(path: Path, legacy: bool = False) -> str:
    stem = path.stem
    if legacy and stem.startswith("summary-"):
        stem = stem.removeprefix("summary-")
    return stem.replace("-", " ")


def list_summary_files(state_dir: Path, summary_dir: Path | None = None) -> list[SummaryFile]:
    summary_dir = summary_dir or state_dir
    files: list[SummaryFile] = []
    seen: set[str] = set()

    def add(path: Path, topic: str, source: str) -> None:
        key = _topic_slug(topic)
        if not key or key in seen:
            return
        seen.add(key)
        files.append(SummaryFile(topic=topic, path=path, source=source))

    if summary_dir.exists():
        summary_paths = []
        for child in ("topics", "sources", "authors"):
            child_dir = summary_dir / child
            if child_dir.exists():
                summary_paths.extend(child_dir.glob("*.md"))
        summary_paths.extend(summary_dir.glob("*.md"))
        for path in summary_paths:
            name = path.name
            if (
                name.startswith("summary-")
                or name.endswith(".prompt-input.md")
                or name.endswith(".audit.md")
                or name.endswith(".manifest.md")
                or name.startswith("pdf-")
            ):
                continue
            add(path, _topic_from_summary_path(path), "summaries")

    if state_dir.exists():
        for path in sorted(state_dir.glob("summary-*.md")):
            add(path, _topic_from_summary_path(path, legacy=True), "legacy")

    return files


def _summary_topics_from_files(state_dir: Path, summary_dir: Path | None = None) -> list[str]:
    return [item.topic for item in list_summary_files(state_dir, summary_dir=summary_dir)]


def build_summary_query_map(
    state_dir: Path,
    db_path: Path = ki.DB_PATH,
    summary_dir: Path | None = None,
) -> dict[str, str]:
    topics = _summary_topics_from_files(state_dir, summary_dir=summary_dir)
    query_map = {topic: topic for topic in topics}
    topic_by_slug = {_topic_slug(topic): topic for topic in topics}

    if TOPIC_ROUTING_ALIASES_PATH.exists():
        for raw_line in TOPIC_ROUTING_ALIASES_PATH.read_text(encoding="utf-8").splitlines():
            if not raw_line.strip() or raw_line.lstrip().startswith("#"):
                continue
            slug, aliases = raw_line.split("\t", 1)
            topic = topic_by_slug.get(slug)
            if topic:
                query_map[topic] += f" {aliases}"

    if db_path.exists():
        with ki.open_db(db_path) as conn:
            for row in conn.execute("SELECT name, query, description FROM topics ORDER BY id"):
                topic = topic_by_slug.get(_topic_slug(row["name"]))
                if topic:
                    query_map[topic] += f" {row['query']} {row['description']}"

            candidates = list(conn.execute(
                "SELECT phrase, record_count FROM topic_candidates ORDER BY record_count DESC, phrase"
            ))

        for row in candidates:
            phrase = row["phrase"]
            phrase_tokens = _tokens(phrase)
            if not phrase_tokens:
                continue
            best_topic = ""
            best_score = 0.0
            for topic in topics:
                topic_tokens = _tokens(query_map[topic])
                score = len(phrase_tokens & topic_tokens) / max(len(phrase_tokens), 1)
                if score > best_score:
                    best_topic = topic
                    best_score = score
            if best_topic and best_score >= 0.25:
                query_map[best_topic] += f" {phrase}"

    return query_map


def rank_relevant_summary_topics(
    question: str,
    state_dir: Path,
    db_path: Path = ki.DB_PATH,
    limit: int = 5,
    summary_dir: Path | None = None,
) -> list[tuple[str, float]]:
    question = focus_routing_question(question)
    query_map = build_summary_query_map(state_dir, db_path=db_path, summary_dir=summary_dir)
    ranked = [
        (topic, score)
        for topic, search_text in query_map.items()
        if (score := _score_topic_text(question, topic, search_text)) > 0
    ]
    ranked.sort(key=lambda item: (-item[1], item[0].lower()))
    if not ranked:
        return []
    top_score = ranked[0][1]
    cutoff = top_score * 0.35
    focused = [item for item in ranked if item[1] >= cutoff]
    return focused[:limit]


def _record_ids_in_text(text: str) -> list[int]:
    seen: set[int] = set()
    record_ids: list[int] = []
    for match in re.finditer(r"\[record_id:(\d+)\]", text):
        record_id = int(match.group(1))
        if record_id not in seen:
            seen.add(record_id)
            record_ids.append(record_id)
    return record_ids



def _record_citation_url(row: Any) -> str:
    return str(row["url"] or "").strip()


def _record_citation_text(row: Any) -> str:
    title = str(row["title"] or "").strip() or "(untitled)"
    author = str(row["author"] or "").strip() or "(unknown)"
    url = _record_citation_url(row)
    if url:
        return f"{title}, {author}, <{url}>"
    return f"{title}, {author}"


def enrich_summary_citations(text: str, db_path: Path | None = None) -> str:
    record_ids = _record_ids_in_text(text)
    resolved_db_path = db_path or ki.DB_PATH
    if not record_ids or not resolved_db_path.exists():
        return text

    rows_by_id: dict[int, Any] = {}
    with ki.open_db(resolved_db_path) as conn:
        for record_id in record_ids:
            row = conn.execute(
                """
                SELECT id, title, author, source, year, url
                FROM records
                WHERE id = ?
                """,
                (record_id,),
            ).fetchone()
            if row:
                rows_by_id[record_id] = row

    def replace_record_id(match: re.Match[str]) -> str:
        record_id = int(match.group(1))
        row = rows_by_id.get(record_id)
        if not row:
            return match.group(0)
        return "[" + _record_citation_text(row) + "]"

    enriched_text = re.sub(r"\[record_id:(\d+)\]", replace_record_id, text)
    detail_lines: list[str] = []
    for record_id in record_ids:
        row = rows_by_id.get(record_id)
        if row:
            detail_lines.append(f"- {_record_citation_text(row)}")

    if not detail_lines:
        return enriched_text
    return f"{enriched_text.rstrip()}\n\n# Citation details\n\n" + "\n".join(detail_lines)
def load_summary_files(
    state_dir: Path,
    topic: str = "",
    question: str = "",
    max_topics: int = 1,
    summary_dir: Path | None = None,
    include_auxiliary: bool = True,
    db_path: Path | None = None,
) -> str:
    state_dir_resolved = state_dir.resolve()
    summary_dir = summary_dir or state_dir
    summary_dir_resolved = summary_dir.resolve()
    summary_files = list_summary_files(state_dir, summary_dir=summary_dir)
    summary_by_slug = {_topic_slug(item.topic): item for item in summary_files}

    if topic:
        slug = _topic_slug(topic)
        item = summary_by_slug.get(slug)
        if not item:
            ranked = rank_relevant_summary_topics(
                topic,
                state_dir,
                db_path=db_path or ki.DB_PATH,
                limit=1,
                summary_dir=summary_dir,
            )
            if ranked:
                item = summary_by_slug.get(_topic_slug(ranked[0][0]))
        if not item:
            legacy_path = (state_dir / f"summary-{slug}.md").resolve()
            if not str(legacy_path).startswith(str(state_dir_resolved)):
                return ""
            if legacy_path.exists():
                item = SummaryFile(topic=topic, path=legacy_path, source="legacy")
        if item:
            path = item.path.resolve()
            valid_root = summary_dir_resolved if item.source == "summaries" else state_dir_resolved
            if not str(path).startswith(str(valid_root)):
                return ""
            return (
                "# Summary Evidence\n\n"
                "Use ONLY the summary file below to answer. Do not use outside knowledge.\n\n"
                f"Selected summary file: {path}\n"
                f"Selected summary: {item.topic}\n\n"
                f"# {item.topic}\n\n{enrich_summary_citations(path.read_text(encoding='utf-8'), db_path=db_path)}"
            )
        return _small_topic_record_evidence(topic, db_path=db_path)
    parts = []

    summary_topics = [item.topic for item in summary_files]
    if question:
        ranked_topics = [
            name
            for name, _score in rank_relevant_summary_topics(
                question,
                state_dir,
                db_path=db_path or ki.DB_PATH,
                limit=max_topics,
                summary_dir=summary_dir,
            )
        ]
    else:
        ranked_topics = summary_topics

    summary_by_slug = {_topic_slug(item.topic): item for item in summary_files}
    for topic_name in ranked_topics:
        item = summary_by_slug.get(_topic_slug(topic_name))
        if not item or not item.path.exists():
            continue
        parts.append(
            f"# Summary file: {item.topic}\n\n"
            f"Source file: {item.path}\n\n"
            f"{enrich_summary_citations(item.path.read_text(encoding='utf-8'), db_path=db_path)}"
        )
    if include_auxiliary:
        for path in sorted(state_dir.glob("pdf-*.md")):
            doc_name = path.stem.replace("pdf-", "").replace("-", " ")
            parts.append(f"# PDF: {doc_name}\n\n{path.read_text(encoding='utf-8')}")
    return "\n\n---\n\n".join(parts)


# --- Tool implementations ---

def tool_get_status() -> str:
    lines: list[str] = []
    db_path = ki.DB_PATH

    if not db_path.exists():
        return f"Database not found: {db_path}"

    with ki.open_db(db_path) as conn:
        source_rows = conn.execute(
            "SELECT source, COUNT(*) FROM records GROUP BY source ORDER BY source"
        ).fetchall()
        lines.append("Records by source:")
        total = 0
        for source, cnt in source_rows:
            lines.append(f"  {source}: {cnt}")
            total += cnt
        lines.append(f"  total: {total}")

        unread = conn.execute(
            "SELECT COUNT(*) FROM records WHERE agent_read = 0"
        ).fetchone()[0]
        lines.append(f"\nunclassified: {unread}")

        annotated = conn.execute("SELECT COUNT(*) FROM record_annotations").fetchone()[0]
        total_records = conn.execute("SELECT COUNT(*) FROM records").fetchone()[0]
        lines.append(f"record annotations: {annotated}/{total_records}")

        last_import = conn.execute("SELECT MAX(imported_at) FROM records").fetchone()[0]
        lines.append(f"last import: {last_import or 'never'}")

        last_classified = conn.execute(
            "SELECT MAX(agent_read_at) FROM records WHERE agent_read = 1"
        ).fetchone()[0]
        lines.append(f"last classified: {last_classified or 'never'}")

    log_path = ki.LOG_PATH
    if log_path.exists():
        recent = log_path.read_text(encoding="utf-8").splitlines()[-10:]
        if recent:
            lines.append("\nRecent import log:")
            lines.extend(f"  {line}" for line in recent)

    return "\n".join(lines)


def _optional_positive_limit(limit: Any) -> int | None:
    if limit in (None, "", 0):
        return None
    try:
        parsed = int(limit)
    except (TypeError, ValueError):
        return None
    return max(1, parsed)


def _record_id_from_query(query: str) -> int | None:
    def valid_record_id(value: str) -> int | None:
        record_id = int(value)
        return record_id if 0 < record_id <= 9_223_372_036_854_775_807 else None

    stripped = query.strip()
    if re.fullmatch(r"\d+", stripped):
        return valid_record_id(stripped)
    match = re.search(r"\b(?:record|record_id)\s*:?\s*#?(\d+)\b", stripped, flags=re.I)
    if match:
        return valid_record_id(match.group(1))
    return None


def _get_record_by_id(db_path: Path, record_id: int) -> Any | None:
    with ki.open_db(db_path) as conn:
        return conn.execute("SELECT * FROM records WHERE id = ?", (record_id,)).fetchone()


SOURCE_QUERY_ALIASES: dict[str, tuple[str, ...]] = {
    "defcon": ("defcon33", "defcon34"),
    "def con": ("defcon33", "defcon34"),
    "defcon 33": ("defcon33",),
    "def con 33": ("defcon33",),
    "dc33": ("defcon33",),
    "defcon 34": ("defcon34",),
    "def con 34": ("defcon34",),
    "dc34": ("defcon34",),
    "black hat": ("blackhat",),
    "blackhat": ("blackhat",),
    "bsideslv": ("bsideslv",),
    "bsides lv": ("bsideslv",),
    "bsides las vegas": ("bsideslv",),
    "prompt or gtfo": ("promptorgtfo",),
    "promptorgtfo": ("promptorgtfo",),
    "unprompted": ("unprompted2026",),
    "unprompted2026": ("unprompted2026",),
    "[un]prompted": ("unprompted2026",),
}

SOURCE_QUERY_FILLER_WORDS = {
    "all",
    "about",
    "any",
    "by",
    "for",
    "from",
    "in",
    "list",
    "of",
    "records",
    "record",
    "show",
    "source",
    "talks",
    "the",
}


def _available_record_sources(db_path: Path = ki.DB_PATH) -> set[str]:
    if not db_path.exists():
        return set()
    with ki.open_db(db_path) as conn:
        return {
            str(row["source"]).strip()
            for row in conn.execute("SELECT DISTINCT source FROM records ORDER BY source")
            if str(row["source"]).strip()
        }


def _source_alias_map(db_path: Path = ki.DB_PATH) -> dict[str, tuple[str, ...]]:
    aliases = dict(SOURCE_QUERY_ALIASES)
    for source_name in _available_record_sources(db_path):
        aliases[source_name.lower()] = (source_name,)
        aliases[source_name.lower().replace("-", " ")] = (source_name,)
    return aliases


def _resolve_source_names(value: str, db_path: Path = ki.DB_PATH) -> list[str]:
    cleaned = " ".join(value.strip().lower().replace("_", " ").split())
    aliases = _source_alias_map(db_path)
    sources = list(aliases.get(cleaned, ()))
    available = _available_record_sources(db_path)
    if available:
        sources = [source for source in sources if source in available]
    return sources


def _sources_matching_years(sources: list[str], years: list[str], db_path: Path = ki.DB_PATH) -> list[str]:
    if not sources or not years:
        return sources
    source_set = set(sources)
    year_set = set(years)
    if {"defcon33", "defcon34"}.issubset(source_set):
        if "2026" in year_set:
            return ["defcon34"]
        if "2025" in year_set:
            return ["defcon33"]
    if not db_path.exists():
        return sources
    placeholders = ", ".join("?" for _ in sources)
    year_placeholders = ", ".join("?" for _ in years)
    with ki.open_db(db_path) as conn:
        rows = conn.execute(
            f"""
            SELECT DISTINCT source
            FROM records
            WHERE source IN ({placeholders})
              AND year IN ({year_placeholders})
            ORDER BY source
            """,
            [*sources, *years],
        ).fetchall()
    narrowed = [str(row["source"]) for row in rows]
    return narrowed or sources

def _extract_source_filter(query: str = "", source: str = "", db_path: Path = ki.DB_PATH) -> tuple[list[str], list[str], str]:
    sources: list[str] = []
    years: list[str] = []
    residual = query.strip()

    def add_sources(values: list[str]) -> None:
        for value in values:
            if value not in sources:
                sources.append(value)

    def add_year(value: str) -> None:
        if re.fullmatch(r"20\d{2}", value) and value not in years:
            years.append(value)

    if source:
        add_sources(_resolve_source_names(source, db_path=db_path) or [source.strip()])

    explicit = re.search(r"\bsource\s*[:=]\s*([a-zA-Z0-9_\-\[\] ]+)", residual, flags=re.IGNORECASE)
    if explicit:
        value = explicit.group(1).strip()
        add_sources(_resolve_source_names(value, db_path=db_path))
        residual = (residual[: explicit.start()] + " " + residual[explicit.end() :]).strip()

    year_matches = re.findall(r"(?<!\d)(20\d{2})(?!\d)", residual)
    for year in year_matches:
        add_year(year)
    residual = re.sub(r"(?<!\d)20\d{2}(?!\d)", " ", residual).strip()

    aliases = _source_alias_map(db_path)
    for alias in sorted(aliases, key=len, reverse=True):
        pattern = r"(?<![a-zA-Z0-9])" + re.escape(alias) + r"(?![a-zA-Z0-9])"
        if re.search(pattern, residual, flags=re.IGNORECASE):
            add_sources(list(aliases[alias]))
            residual = re.sub(pattern, " ", residual, flags=re.IGNORECASE).strip()
            break

    residual_tokens = re.findall(r"[a-zA-Z][a-zA-Z0-9_\-]*", residual.lower())
    if sources and residual_tokens and all(token in SOURCE_QUERY_FILLER_WORDS for token in residual_tokens):
        residual = ""
    sources = _sources_matching_years(sources, years, db_path=db_path)
    return sources, years, " ".join(residual.split())

def _format_source_record_results(
    records: list[Any],
    sources: list[str],
    requested_limit: int | None,
    years: list[str] | None = None,
) -> str:
    filters = [f"source: {', '.join(sources)}"]
    if years:
        filters.append(f"year: {', '.join(years)}")
    filter_text = "; ".join(filters)
    if not records:
        return f"No records found for {filter_text}"
    limit_note = f" (limit {requested_limit})" if requested_limit is not None else ""
    parts = [f"{len(records)} source record match(es) for {filter_text}{limit_note}\n"]
    parts.extend(_format_compact_record(record) for record in records)
    return "\n\n---\n\n".join(parts)

def _format_compact_record(r: Any) -> str:
    topics = ki.decode_topics(r["agent_topics"])
    part = (
        f"[{r['id']}] {r['source']} {r['year']}\n"
        f"Title: {r['title']}\n"
        f"Author: {r['author']}\n"
    )
    if topics:
        part += f"Topics: {', '.join(topics)}\n"
    url = _record_citation_url(r)
    if url:
        part += f"URL: {url}\n"
    snippet = " ".join(r["text"].split())[:240]
    if snippet:
        part += f"Snippet: {snippet}"
    return part


def _format_complete_record_evidence(r: Any) -> str:
    topics = ki.decode_topics(r["agent_topics"])
    lines = [
        f"## [record_id:{r['id']}] {r['title']}",
        f"Source: {r['source']}",
        f"Year: {r['year']}",
        f"Author: {r['author']}",
    ]
    url = _record_citation_url(r)
    if url:
        lines.append(f"URL: {url}")
    if topics:
        lines.append(f"Topics: {', '.join(topics)}")
    lines.append("")
    lines.append(str(r["text"] or ""))
    return "\n".join(lines).strip()


def _small_topic_record_evidence(
    topic: str,
    db_path: Path | None = None,
    max_records: int = SMALL_TOPIC_MAX_RECORDS,
) -> str:
    resolved_db_path = db_path or ki.DB_PATH
    rows = ki.list_records_for_topic(resolved_db_path, topic, limit=max_records + 1)
    if not rows or len(rows) > max_records:
        return ""
    records_text = "\n\n---\n\n".join(_format_complete_record_evidence(row) for row in rows)
    return (
        "# Complete Record Evidence\n\n"
        "No generated summary file was found for this small topic. "
        "Use ONLY the complete records below to answer. Do not use outside knowledge.\n\n"
        f"Selected topic: {topic}\n"
        f"Record count: {len(rows)}\n\n"
        f"{records_text}"
    )


def tool_search_records(query: str, topic: str = "", limit: int | None = None) -> str:
    db_path = ki.DB_PATH
    record_id = _record_id_from_query(query)
    if record_id is not None:
        record = _get_record_by_id(db_path, record_id)
        if record is None:
            return f"No record found with id: {record_id}"
        return f"Exact record match for id {record_id}:\n\n{_format_compact_record(record)}"

    source_names, years, search_query = _extract_source_filter(query, db_path=db_path)
    requested_limit = _optional_positive_limit(limit)
    scan_limit = requested_limit or 10_000
    if source_names and not search_query and not topic:
        records = ki.list_records_for_sources(db_path, source_names, limit=scan_limit, years=years)
        if requested_limit is not None:
            records = records[:requested_limit]
        return _format_source_record_results(records, source_names, requested_limit, years=years)

    search_text = search_query or query
    fts_query = question_to_fts_query(search_text)
    if not fts_query:
        if source_names:
            records = ki.list_records_for_sources(db_path, source_names, limit=scan_limit, years=years)
            if requested_limit is not None:
                records = records[:requested_limit]
            return _format_source_record_results(records, source_names, requested_limit, years=years)
        return f"No searchable terms found for: {query!r}"
    ranked_topics = rank_relevant_topics(search_text, ki.list_classification_topics(db_path), limit=3)

    if topic:
        topic_rows = ki.list_records_for_topic(db_path, topic, limit=scan_limit)
        try:
            fts_rows = ki.search_records(db_path, fts_query, limit=scan_limit)
            fts_ids = {r["id"] for r in fts_rows}
            records = [r for r in topic_rows if r["id"] in fts_ids]
            if len(records) < 3:
                records = list(topic_rows)
        except Exception:
            records = list(topic_rows)
        if source_names:
            source_set = set(source_names)
            records = [r for r in records if r["source"] in source_set]
        if years:
            year_set = set(years)
            records = [r for r in records if str(r["year"]) in year_set]
        if requested_limit is not None:
            records = records[:requested_limit]
    else:
        try:
            records = ki.search_records(db_path, fts_query, limit=scan_limit)
        except Exception:
            return f"Search failed for query: {query!r}"
        if source_names:
            source_set = set(source_names)
            records = [r for r in records if r["source"] in source_set]
        if years:
            year_set = set(years)
            records = [r for r in records if str(r["year"]) in year_set]
        if ranked_topics:
            ranked_names = [name for name, _score in ranked_topics]
            ranked_set = set(ranked_names)
            topic_filtered = [
                r for r in records
                if ranked_set & set(ki.decode_topics(r["agent_topics"]))
            ]
            if topic_filtered:
                records = topic_filtered
        if requested_limit is not None:
            records = records[:requested_limit]

    if not records:
        filters = []
        if source_names:
            filters.append(f"source={', '.join(source_names)}")
        if years:
            filters.append(f"year={', '.join(years)}")
        if topic:
            filters.append(f"topic={topic}")
        suffix = f" ({'; '.join(filters)})" if filters else ""
        return f"No records found for: {search_text!r}{suffix}"

    parts = [f"{len(records)} compact record match(es) found:\n"]
    if source_names:
        parts.append("Source filter: " + ", ".join(source_names))
    if years:
        parts.append("Year filter: " + ", ".join(years))
    if ranked_topics:
        parts.append(
            "Relevant topics considered: "
            + ", ".join(name for name, _score in ranked_topics)
        )
    for r in records:
        parts.append(_format_compact_record(r))

    return "\n\n---\n\n".join(parts)

def _row_value(row: object, key: str, default: str = "") -> Any:
    try:
        value = row[key]  # sqlite3.Row and local fake rows both support this.
    except (KeyError, IndexError, TypeError):
        return default
    return default if value is None else value


def _json_list_values(value: str | None) -> list[str]:
    if not value:
        return []
    try:
        loaded = json.loads(value)
    except json.JSONDecodeError:
        return []
    if not isinstance(loaded, list):
        return []
    return [str(item).strip() for item in loaded if str(item).strip()]


def _annotation_terms(query: str = "", keywords: list[str] | None = None) -> list[str]:
    terms: list[str] = []
    seen: set[str] = set()
    raw_terms = keywords or []
    if query and not raw_terms:
        raw_terms = re.findall(r"[a-zA-Z][a-zA-Z0-9+\- ]{2,}", query)
    for term in raw_terms:
        cleaned = " ".join(str(term).strip().lower().split())
        if cleaned and cleaned not in seen and cleaned not in ki.STOPWORDS:
            seen.add(cleaned)
            terms.append(cleaned)
    return terms


def _annotation_search_blob(row: object) -> str:
    parts = [
        str(_row_value(row, "title")),
        str(_row_value(row, "short_summary")),
        str(_row_value(row, "ai_relevance")),
        str(_row_value(row, "source_quality")),
        str(_row_value(row, "relevance_notes")),
    ]
    for column in [
        "keywords_json",
        "tools_json",
        "people_json",
        "claims_json",
        "use_cases_json",
        "content_types_json",
        "security_domains_json",
    ]:
        parts.extend(_json_list_values(_row_value(row, column)))
    return " ".join(parts).lower()


def _annotation_match_fields(row: object, terms: list[str]) -> tuple[int, list[str]]:
    fields = [
        ("title", str(_row_value(row, "title"))),
        ("summary", str(_row_value(row, "short_summary"))),
        ("keywords", " ".join(_json_list_values(_row_value(row, "keywords_json")))),
        ("tools", " ".join(_json_list_values(_row_value(row, "tools_json")))),
        ("people", " ".join(_json_list_values(_row_value(row, "people_json")))),
        ("claims", " ".join(_json_list_values(_row_value(row, "claims_json")))),
        ("use_cases", " ".join(_json_list_values(_row_value(row, "use_cases_json")))),
        ("content_types", " ".join(_json_list_values(_row_value(row, "content_types_json")))),
        ("security_domains", " ".join(_json_list_values(_row_value(row, "security_domains_json")))),
        ("ai_relevance", str(_row_value(row, "ai_relevance"))),
        ("relevance_notes", str(_row_value(row, "relevance_notes"))),
    ]
    score = 0
    matched_fields: list[str] = []
    weights = {
        "keywords": 5,
        "tools": 5,
        "people": 4,
        "claims": 4,
        "use_cases": 4,
        "security_domains": 4,
        "summary": 3,
        "relevance_notes": 3,
        "title": 2,
        "content_types": 2,
        "ai_relevance": 2,
    }
    for field, value in fields:
        value_l = value.lower()
        if any(term in value_l for term in terms):
            matched_fields.append(field)
            score += weights.get(field, 1)
    return score, matched_fields


def tool_query_annotations(
    query: str = "",
    keywords: list[str] | None = None,
    topic: str = "",
    source: str = "",
    match: str = "any",
    limit: int | None = None,
) -> str:
    source_names, years, filtered_query = _extract_source_filter(query, source=source, db_path=ki.DB_PATH)
    terms = _annotation_terms(query=filtered_query, keywords=keywords)

    requested_limit = _optional_positive_limit(limit)
    scan_limit = requested_limit or 10_000
    if not terms:
        if source_names:
            records = ki.list_records_for_sources(ki.DB_PATH, source_names, limit=scan_limit, years=years)
            if requested_limit is not None:
                records = records[:requested_limit]
            return _format_source_record_results(records, source_names, requested_limit, years=years)
        return "No annotation keywords provided."

    match = match if match in {"any", "all"} else "any"
    candidate_rows: dict[int, object] = {}
    sources_to_scan = source_names or [""]
    for term in terms:
        for source_name in sources_to_scan:
            for row in ki.list_record_annotations(ki.DB_PATH, limit=scan_limit, source=source_name, query=term):
                if years and str(_row_value(row, "year")) not in set(years):
                    continue
                record_id = int(_row_value(row, "record_id", 0))
                if record_id:
                    candidate_rows[record_id] = row
    scored: list[tuple[int, object, list[str]]] = []
    topic_l = topic.strip().lower()
    for row in candidate_rows.values():
        topics = ki.decode_topics(str(_row_value(row, "agent_topics")))
        if topic_l and topic_l not in {t.lower() for t in topics}:
            continue
        blob = _annotation_search_blob(row)
        if match == "all" and not all(term in blob for term in terms):
            continue
        if match == "any" and not any(term in blob for term in terms):
            continue
        score, fields = _annotation_match_fields(row, terms)
        scored.append((score, row, fields))

    scored.sort(key=lambda item: (-item[0], int(_row_value(item[1], "record_id", 0))))
    if requested_limit is not None:
        scored = scored[:requested_limit]

    if not scored:
        filters = []
        if topic:
            filters.append(f"topic={topic!r}")
        if source_names:
            filters.append(f"source={', '.join(source_names)!r}")
        if years:
            filters.append(f"year={', '.join(years)!r}")
        suffix = f" ({', '.join(filters)})" if filters else ""
        return f"No annotation matches found for: {', '.join(terms)}{suffix}"

    parts = [
        f"{len(scored)} annotation match(es) for: {', '.join(terms)}",
        f"match mode: {match}",
    ]
    if topic:
        parts.append(f"topic filter: {topic}")
    if source_names:
        parts.append(f"source filter: {', '.join(source_names)}")
    if years:
        parts.append(f"year filter: {', '.join(years)}")

    cards = ["\n".join(parts)]
    for score, row, fields in scored:
        topics = ki.decode_topics(str(_row_value(row, "agent_topics")))
        keywords_text = ", ".join(_json_list_values(_row_value(row, "keywords_json"))[:8])
        tools_text = ", ".join(_json_list_values(_row_value(row, "tools_json"))[:8])
        claims_text = "; ".join(_json_list_values(_row_value(row, "claims_json"))[:3])
        use_cases_text = "; ".join(_json_list_values(_row_value(row, "use_cases_json"))[:3])
        domains_text = ", ".join(_json_list_values(_row_value(row, "security_domains_json"))[:6])
        card = (
            f"[record_id:{int(_row_value(row, 'record_id', 0))}] "
            f"{_row_value(row, 'source')} {_row_value(row, 'year')}\n"
            f"Title: {_row_value(row, 'title')}\n"
            f"Author: {_row_value(row, 'author')}\n"
            f"Matched annotation fields: {', '.join(fields) or '(none)'}; score={score}\n"
        )
        url = str(_row_value(row, "url")).strip()
        if url:
            card += f"URL: {url}\n"
        if topics:
            card += f"Topics: {', '.join(topics)}\n"
        if keywords_text:
            card += f"Keywords: {keywords_text}\n"
        if tools_text:
            card += f"Tools: {tools_text}\n"
        if domains_text:
            card += f"Security domains: {domains_text}\n"
        if claims_text:
            card += f"Claims: {claims_text}\n"
        if use_cases_text:
            card += f"Use cases: {use_cases_text}\n"
        summary = str(_row_value(row, "short_summary"))
        if summary:
            card += f"Summary: {summary[:500]}"
        cards.append(card.strip())

    return "\n\n---\n\n".join(cards)


def tool_answer_from_summaries(
    topic: str = "",
    question: str = "",
    max_topics: int = DEFAULT_SUMMARY_QUESTION_TOPICS,
) -> str:
    max_topics = max(1, int(max_topics))
    text = load_summary_files(
        ki.STATE_DIR,
        topic=topic,
        question=question,
        max_topics=max_topics,
        summary_dir=SUMMARY_DIR,
        include_auxiliary=False,
    )
    if not text:
        return "No summary files found in the summaries folder or legacy knowledge folder."
    if not topic and question:
        ranked = rank_relevant_summary_topics(
            question,
            ki.STATE_DIR,
            limit=max_topics,
            summary_dir=SUMMARY_DIR,
        )
        if ranked:
            selected_lines = "\n".join(
                f"- {name} (score: {score:.2f})" for name, score in ranked
            )
            text = (
                "# Summary Evidence Instructions\n\n"
                "Use ONLY the summary files included in this tool result. "
                "Do not use general knowledge or any source not listed here. "
                "The final answer must start with a short 'Sources used' line naming every selected summary used. "
                "When citing records, use the expanded citation format from the summary evidence: title, author or speaker, URL. Preserve URLs as Markdown autolinks when available. "
                "Do not reduce expanded citations back to bare record IDs.\n\n"
                "# Relevant summaries selected\n\n"
                f"{selected_lines}\n\n---\n\n{text}"
            )
    # Return the summary content; the agent model will reason over it in its next turn.
    return text


def tool_answer_about_author(
    author: str,
    db_path: Path = ki.DB_PATH,
    summary_dir: Path = SUMMARY_DIR,
) -> str:
    with ki.open_db(db_path) as conn:
        rows = conn.execute(
            """
            SELECT records.*
            FROM authors
            JOIN author_records ON author_records.author_id = authors.id
            JOIN records ON records.id = author_records.record_id
            WHERE authors.name = ? COLLATE NOCASE
            ORDER BY records.id
            """,
            (author.strip(),),
        ).fetchall()

    if not rows:
        return f"No records found for author: {author}"

    canonical_author = author.strip()
    if len(rows) == 1:
        row = rows[0]
        url = _record_citation_url(row)
        return (
            f"Author: {canonical_author}\n"
            "Evidence: single underlying record\n\n"
            f"[record_id:{row['id']}] {row['source']} {row['year']}\n"
            f"Title: {row['title']}\n"
            f"Author metadata: {row['author']}\n"
            + (f"URL: {url}\n\n" if url else "")
            + f"{row['text']}"
        ).strip()

    summary_path = summary_dir / "authors" / f"{_topic_slug(canonical_author)}.md"
    if summary_path.exists():
        return (
            f"Author: {canonical_author}\n"
            f"Evidence: author summary covering {len(rows)} records\n"
            f"Source file: {summary_path}\n\n"
            f"{summary_path.read_text(encoding='utf-8')}"
        )

    record_ids = ", ".join(str(row["id"]) for row in rows)
    return (
        f"Author {canonical_author} has {len(rows)} records but no generated author summary. "
        f"Generate it before answering broad author questions. Record IDs: {record_ids}"
    )


def tool_generate_topic_summary(client: Any, topic: str) -> str:
    topics = ka.get_classification_topics(ki.DB_PATH)
    if topic not in topics:
        close = [t for t in topics if topic.lower() in t.lower()]
        hint = f" Did you mean: {', '.join(close)}?" if close else f" Valid topics: {', '.join(topics)}"
        return f"Unknown topic {topic!r}.{hint}"

    try:
        audit = summarize_topic_to_files(
            topic=topic,
            db_path=ki.DB_PATH,
            summary_dir=SUMMARY_DIR,
            client=client,
        )
    except ValueError as exc:
        ki.log_info(f"summary regeneration failed: topic={topic!r}, error={exc}")
        return f"Summary regeneration failed for {topic!r}: {exc}. No summary was written."

    ki.log_info(
        f"summary regenerated by qa: topic={topic!r}, "
        f"records={audit['expected_record_count']}, path={audit['summary_file_path']}"
    )

    return (
        f"Summary regenerated for {topic!r} ({audit['expected_record_count']} records). "
        f"Written to {audit['summary_file_path']}. "
        f"Audit: {audit['summary_input_artifact_path'].replace('.prompt-input.md', '.audit.json')}"
    )


# --- Agent loop ---

def dispatch_tool(
    client: Any,
    tool_name: str,
    tool_input: dict,
    question_context: str = "",
) -> str:
    normalized_tool_name = tool_name.replace("_", "-")
    if normalized_tool_name == "get-status":
        return tool_get_status()
    if normalized_tool_name == "search-records":
        return tool_search_records(
            query=tool_input["query"],
            topic=tool_input.get("topic", ""),
            limit=tool_input.get("limit"),
        )
    if normalized_tool_name == "query-annotations":
        return tool_query_annotations(
            query=tool_input.get("query", ""),
            keywords=tool_input.get("keywords") or None,
            topic=tool_input.get("topic", ""),
            source=tool_input.get("source", ""),
            match=tool_input.get("match", "any"),
            limit=tool_input.get("limit"),
        )
    if normalized_tool_name == "answer-from-summaries":
        return tool_answer_from_summaries(
            topic=tool_input.get("topic", ""),
            question=tool_input.get("question", "") or question_context,
            max_topics=tool_input.get("max_topics", DEFAULT_SUMMARY_QUESTION_TOPICS),
        )
    if normalized_tool_name == "answer-about-author":
        return tool_answer_about_author(tool_input["author"])
    if normalized_tool_name == "generate-topic-summary":
        return tool_generate_topic_summary(client, tool_input["topic"])
    return f"Unknown tool: {tool_name}"


def parse_prefixed_request(text: str) -> tuple[str, str]:
    stripped = text.strip()
    lowered = stripped.lower()
    if lowered.startswith("query:"):
        return "query", stripped[6:].strip()
    if lowered.startswith("question:"):
        return "question", stripped[9:].strip()
    return "", stripped


def run_summary_question(client: Any, question: str) -> None:
    evidence = tool_answer_from_summaries(question=question)
    response = client.messages.create(
        model=MODEL,
        max_tokens=QA_MAX_OUTPUT_TOKENS,
        system=AGENT_SYSTEM,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Question: {question}\n\n"
                    "Answer using ONLY the summary evidence below. "
                    "Start with a Sources used line naming every summary file you relied on. "
                    "Then answer directly in natural prose. "
                    "Avoid report-style sections and numbered lists unless they are necessary for clarity. "
                    "If the question asks about talks, presentations, or records, include the title, speaker or author when available, source or venue, and what each contributes. "
                    "When citing records, use the expanded citation format from the summary evidence: title, author or speaker, URL. Preserve URLs as Markdown autolinks when available. "
                    "Do not reduce expanded citations back to bare record IDs. "
                    "Call out common themes and unique items.\n\n"
                    f"{evidence}"
                ),
            }
        ],
    )
    for block in response.content:
        if hasattr(block, "text"):
            ki.safe_print(block.text)


def create_llm_client_or_report() -> Any | None:
    try:
        return llm_client.create_client()
    except Exception as exc:
        ki.safe_print(
            "LLM client unavailable: "
            f"{exc}\n"
            "Set the required API key for the configured provider, or use "
            "'query: <text>' for local annotation search without the LLM."
        )
        return None

def run_prefixed_turn(question: str) -> bool:
    mode, payload = parse_prefixed_request(question)
    if not mode:
        return False
    if not payload:
        ki.safe_print(f"No {mode} text provided.")
        return True
    if mode == "query":
        ki.safe_print("[query-annotations]")
        ki.safe_print(tool_query_annotations(query=payload))
        return True
    if mode == "question":
        ki.safe_print("[answer-from-summaries]")
        client = create_llm_client_or_report()
        if client is None:
            return True
        run_summary_question(client, payload)
        return True
    return False


def format_help() -> str:
    tool_lines = [
        "Analyst commands:",
        "  help                 Show this help text.",
        "  query: <text>        Search structured record annotations without using the LLM.",
        "  question: <text>     Answer from summary files using the summary-answer flow.",
        "  quit                 Exit interactive mode.",
        "",
        "Analyst tools:",
    ]
    for tool in TOOLS:
        description = re.sub(r"\s+", " ", str(tool.get("description", ""))).strip()
        tool_lines.append(f"  {tool['name']}")
        if description:
            tool_lines.append(f"    {description}")
        tool_lines.append("")
    return "\n".join(tool_lines)


def run_help_turn(question: str) -> bool:
    if question.strip().lower() not in {"help", "?", "--help", "/help"}:
        return False
    ki.safe_print(format_help())
    return True


def run_agent_turn(client: Any, question: str) -> None:
    messages: list[dict] = [{"role": "user", "content": question}]

    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=QA_MAX_OUTPUT_TOKENS,
            system=AGENT_SYSTEM,
            tools=TOOLS,
            messages=messages,
        )

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text"):
                    ki.safe_print(block.text)
            break

        if response.stop_reason != "tool_use":
            break

        tool_results = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            ki.safe_print(f"[{block.name}]")
            result = dispatch_tool(client, block.name, block.input, question_context=question)
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": result,
            })

        messages.append({"role": "user", "content": tool_results})


def run(args: argparse.Namespace) -> int:
    if args.question:
        question = " ".join(args.question)
        if run_help_turn(question):
            return 0
        if run_prefixed_turn(question):
            return 0
        client = create_llm_client_or_report()
        if client is None:
            return 1
        run_agent_turn(client, question)
        return 0

    print(ORACLE_BANNER)
    print("Knowledge base Q&A - type your question, or 'quit' to exit.\n")
    while True:
        try:
            question = input("Q: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not question:
            continue
        if question.lower() in ("quit", "exit", "q"):
            break
        print()
        if run_help_turn(question):
            pass
        elif not run_prefixed_turn(question):
            client = create_llm_client_or_report()
            if client is not None:
                run_agent_turn(client, question)
        print()

    return 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ask questions about the knowledge base.")
    parser.add_argument("question", nargs="*", help="Question to answer (omit for interactive mode).")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())






