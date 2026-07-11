#!/usr/bin/env python3
"""
Deterministic prompt-injection scanner for knowledge records.

Examples:
    python prompt_injection_scan.py --record-id 2429
    python prompt_injection_scan.py --min-score 4 --limit 50
    python prompt_injection_scan.py --payload-only --export-md knowledge/prompt-injection-review.md
    python prompt_injection_scan.py --jsonl
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from knowledge_indexing import knowledge_index as ki


@dataclass(frozen=True)
class Rule:
    name: str
    weight: int
    pattern: re.Pattern[str]


RULES = [
    Rule("explicit_instruction_header", 4, re.compile(r"\b(?:operational|system|developer)\s+instruction(?:s)?\b", re.I)),
    Rule("automated_agent_target", 3, re.compile(r"\b(?:ai|automated|autonomous)\s+(?:agent|reviewer|scanner|screening|system|workflow)\b", re.I)),
    Rule("llm_target", 3, re.compile(r"\b(?:llm|large language model|language model|chatgpt|claude|copilot|ai assistant)\b", re.I)),
    Rule("ignore_instructions", 4, re.compile(r"\b(?:ignore|disregard|override)\s+(?:all\s+)?(?:previous|prior|above|earlier)\s+(?:instructions|rules|prompts)\b", re.I)),
    Rule("required_steps", 2, re.compile(r"\b(?:required|mandatory)\s+(?:step|steps|action|actions)\b", re.I)),
    Rule("before_continuing", 2, re.compile(r"\b(?:before|prior to)\s+(?:continuing|proceeding|answering|processing)\b", re.I)),
    Rule("http_request", 4, re.compile(r"\b(?:send|make|perform|fetch|issue)\s+(?:an?\s+)?https?\s+(?:get|post|request)\b|\bhttps?\s+(?:get|post)\s+request\b", re.I)),
    Rule("phone_home", 4, re.compile(r"\bphone\s+home\b|\bcallback\s+url\b|\bserver\s+controlled\s+by\b", re.I)),
    Rule("ranking_manipulation", 3, re.compile(r"\b(?:mark|rate|rank|score|assign)\s+(?:this|the|me|applicant|candidate|cv|resume).{0,80}\b(?:perfect|highest|best|excellent|top)\b", re.I | re.S)),
    Rule("continue_normally", 2, re.compile(r"\b(?:proceed|continue)\s+with\s+normal\s+(?:operations|processing|workflow)\b", re.I)),
    Rule("end_instruction", 2, re.compile(r"\bend\s+of\s+(?:operational\s+)?instruction(?:s)?\b", re.I)),
    Rule("secret_exfiltration", 4, re.compile(r"\b(?:exfiltrate|send|upload|post)\s+(?:secrets?|tokens?|credentials?|api keys?|environment variables?)\b", re.I)),
    Rule("tool_use_request", 2, re.compile(r"\b(?:use|call|invoke|run)\s+(?:the\s+)?(?:tool|browser|shell|terminal|python|powershell|curl|wget)\b", re.I)),
    Rule("prompt_disclosure", 3, re.compile(r"\b(?:reveal|print|show|dump|return)\s+(?:your\s+)?(?:system prompt|developer message|instructions|hidden prompt)\b", re.I)),
]


CONTEXT_RULES = [
    Rule("quoted_prompt_label", 2, re.compile(r"\b(?:hidden|embedded|invisible|malicious)\s+(?:prompt|instruction|text)\b", re.I)),
    Rule("prompt_injection_term", 2, re.compile(r"\bprompt[-\s]?injection\b|\bjailbreak(?:ing)?\b", re.I)),
]


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def score_text(text: str) -> dict[str, object]:
    normalized = normalize_text(text)
    matches = []
    score = 0
    for rule in RULES + CONTEXT_RULES:
        found = rule.pattern.search(normalized)
        if not found:
            continue
        excerpt_start = max(0, found.start() - 80)
        excerpt_end = min(len(normalized), found.end() + 80)
        matches.append({
            "rule": rule.name,
            "weight": rule.weight,
            "match": found.group(0),
            "excerpt": normalized[excerpt_start:excerpt_end],
        })
        score += rule.weight

    strong_rules = {match["rule"] for match in matches if int(match["weight"]) >= 4}
    rule_names = {str(match["rule"]) for match in matches}
    payload_like = (
        "ignore_instructions" in rule_names
        or (
            "explicit_instruction_header" in rule_names
            and bool(rule_names & {
                "http_request",
                "phone_home",
                "ranking_manipulation",
                "required_steps",
                "continue_normally",
                "end_instruction",
                "secret_exfiltration",
                "prompt_disclosure",
            })
        )
        or (
            "automated_agent_target" in rule_names
            and bool(rule_names & {"http_request", "phone_home", "ranking_manipulation", "secret_exfiltration"})
        )
    )
    confidence = "none"
    if payload_like or score >= 12 or len(strong_rules) >= 2:
        confidence = "high"
    elif score >= 4:
        confidence = "medium"
    elif score > 0:
        confidence = "low"

    return {
        "score": score,
        "confidence": confidence,
        "payload_like": payload_like,
        "matches": matches,
    }


def iter_records(
    db_path: Path,
    limit: int = 0,
    source: str = "",
    record_id: int = 0,
) -> Iterable[sqlite3.Row]:
    sql = "SELECT id, source, year, title, author, text FROM records WHERE 1 = 1"
    params: list[object] = []
    if record_id:
        sql += " AND id = ?"
        params.append(record_id)
    if source:
        sql += " AND source = ?"
        params.append(source)
    sql += " ORDER BY id"
    if limit and limit > 0:
        sql += " LIMIT ?"
        params.append(limit)
    with ki.open_db(db_path) as conn:
        yield from conn.execute(sql, params)


def scan_records(
    db_path: Path,
    min_score: int = 4,
    limit: int = 0,
    source: str = "",
    record_id: int = 0,
    payload_only: bool = False,
) -> list[dict[str, object]]:
    results = []
    for row in iter_records(db_path, limit=limit, source=source, record_id=record_id):
        text = "\n".join(str(row[key] or "") for key in ("title", "author", "text"))
        scored = score_text(text)
        if int(scored["score"]) < min_score:
            continue
        if payload_only and not scored["payload_like"]:
            continue
        results.append({
            "id": int(row["id"]),
            "source": row["source"],
            "year": row["year"],
            "title": row["title"],
            "author": row["author"],
            "text": row["text"],
            **scored,
        })
    return results


def safe_print(value: str) -> None:
    encoding = sys.stdout.encoding or "utf-8"
    sys.stdout.write(value.encode(encoding, errors="replace").decode(encoding, errors="replace") + "\n")


def print_result(result: dict[str, object]) -> None:
    safe_print(f"[{result['id']}] {result['source']} {result.get('year') or ''} score={result['score']} confidence={result['confidence']}")
    if result.get("payload_like"):
        safe_print("  payload-like: yes")
    safe_print(f"  title: {result['title']}")
    author = str(result.get("author") or "")
    if author:
        safe_print(f"  author: {author}")
    for match in result["matches"]:
        safe_print(f"  +{match['weight']} {match['rule']}: {match['match']}")
        safe_print(f"     {match['excerpt'][:260]}")
    safe_print("")


def markdown_review(results: list[dict[str, object]]) -> str:
    lines = [
        "# Prompt Injection Scanner Review",
        "",
        f"Flagged records: {len(results)}",
        "",
    ]
    for result in results:
        lines.extend([
            f"## Record {result['id']}: {result['title']}",
            "",
            f"- source: {result['source']}",
            f"- year: {result.get('year') or ''}",
            f"- author: {result.get('author') or ''}",
            f"- score: {result['score']}",
            f"- confidence: {result['confidence']}",
            f"- payload_like: {'yes' if result.get('payload_like') else 'no'}",
            "",
            "### Matches",
            "",
        ])
        for match in result["matches"]:
            lines.extend([
                f"- +{match['weight']} `{match['rule']}`: {match['match']}",
                f"  - {match['excerpt']}",
            ])
        lines.extend([
            "",
            "### Full Text",
            "",
            "```text",
            str(result.get("text") or ""),
            "```",
            "",
        ])
    return "\n".join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Score knowledge records for prompt-injection indicators.")
    parser.add_argument("--db", type=Path, default=ki.DB_PATH, help=f"SQLite database path (default {ki.DB_PATH}).")
    parser.add_argument("--min-score", type=int, default=4, help="Minimum score to print (default 4).")
    parser.add_argument("--limit", type=int, default=0, help="Maximum records to scan before filtering (default 0 = all).")
    parser.add_argument("--source", default="", help="Only scan one record source.")
    parser.add_argument("--record-id", type=int, default=0, help="Scan one record id.")
    parser.add_argument("--payload-only", action="store_true", help="Only print records that look like embedded instruction payloads.")
    parser.add_argument("--export-md", type=Path, help="Write flagged records with full text to a Markdown review file.")
    parser.add_argument("--jsonl", action="store_true", help="Print one JSON object per flagged record.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    results = scan_records(
        args.db,
        min_score=args.min_score,
        limit=args.limit,
        source=args.source,
        record_id=args.record_id,
        payload_only=args.payload_only,
    )
    if args.export_md:
        args.export_md.parent.mkdir(parents=True, exist_ok=True)
        args.export_md.write_text(markdown_review(results), encoding="utf-8")
        print(f"review_file: {args.export_md}")
    if args.jsonl:
        for result in results:
            print(json.dumps(result, ensure_ascii=False))
    else:
        for result in results:
            print_result(result)
        print(f"flagged_records: {len(results)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
