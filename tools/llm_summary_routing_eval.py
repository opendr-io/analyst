#!/usr/bin/env python3
"""Evaluate LLM summary selection against curated routing questions."""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

APP_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP_DIR))

import llm_client  # noqa: E402
from config import llm_settings  # noqa: E402


SYSTEM_PROMPT = """You route research questions to exactly one existing summary.
Choose the single best summary from the supplied catalog.
Return JSON only with this exact shape:
{"group":"topic|source|author","slug":"catalog-slug"}
The group and slug must exactly match one catalog entry. Do not invent entries."""


@dataclass(frozen=True)
class CatalogEntry:
    group: str
    slug: str
    description: str


@dataclass
class EvalResult:
    timestamp: str
    case_index: int
    repeat: int
    question: str
    expected_group: str
    expected_slug: str
    selected_group: str = ""
    selected_slug: str = ""
    status: str = ""
    correct: bool = False
    latency_ms: int = 0
    model: str = ""
    provider: str = ""
    raw_response: str = ""
    error: str = ""
    input_tokens: int | None = None
    output_tokens: int | None = None


def default_log_path() -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    return APP_DIR / "tests" / "logs" / f"llm-summary-routing-{timestamp}.txt"


def load_seed_descriptions(path: Path) -> dict[str, str]:
    descriptions: dict[str, str] = {}
    if not path.exists():
        return descriptions
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        name, description = line.split("\t", 1)
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        descriptions[slug] = description
    return descriptions


def build_catalog(summary_dir: Path, seed_path: Path) -> list[CatalogEntry]:
    seed_descriptions = load_seed_descriptions(seed_path)
    entries: list[CatalogEntry] = []
    for group in ("topic", "source", "author"):
        folder = summary_dir / f"{group}s"
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.md")):
            description = seed_descriptions.get(path.stem, path.stem.replace("-", " "))
            entries.append(CatalogEntry(group, path.stem, description))
    return entries


def catalog_prompt(catalog: list[CatalogEntry], question: str) -> str:
    lines = [
        f"- {entry.group}/{entry.slug}: {entry.description}"
        for entry in catalog
    ]
    return f"Question:\n{question}\n\nSummary catalog:\n" + "\n".join(lines)


def response_text(response: Any) -> str:
    return "\n".join(
        str(block.text)
        for block in response.content
        if getattr(block, "type", "") == "text" and getattr(block, "text", "")
    ).strip()


def parse_selection(text: str) -> tuple[str, str]:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    payload = json.loads(cleaned)
    group = str(payload.get("group", "")).strip().lower()
    slug = str(payload.get("slug", "")).strip().lower()
    if not group or not slug:
        raise ValueError("response JSON must contain non-empty group and slug")
    return group, slug


def usage_counts(response: Any) -> tuple[int | None, int | None]:
    raw = getattr(response, "raw", None) or response
    usage = getattr(raw, "usage", None)
    if isinstance(raw, dict):
        usage = raw.get("usage")
    if usage is None:
        return None, None

    def value(*names: str) -> int | None:
        for name in names:
            item = usage.get(name) if isinstance(usage, dict) else getattr(usage, name, None)
            if item is not None:
                return int(item)
        return None

    return value("input_tokens", "prompt_tokens"), value("output_tokens", "completion_tokens")


def evaluate_case(
    client: Any,
    case: dict[str, str],
    catalog: list[CatalogEntry],
    *,
    case_index: int,
    repeat: int,
    model: str,
    provider: str,
    max_output_tokens: int,
) -> EvalResult:
    expected = (case["group"], case["slug"])
    valid = {(entry.group, entry.slug) for entry in catalog}
    result = EvalResult(
        timestamp=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        case_index=case_index,
        repeat=repeat,
        question=case["question"],
        expected_group=expected[0],
        expected_slug=expected[1],
        model=model,
        provider=provider,
    )
    if expected not in valid:
        result.status = "missing_expected_summary"
        result.error = "expected summary is not present in the catalog"
        return result

    started = time.perf_counter()
    try:
        response = client.messages.create(
            model=model,
            max_tokens=max_output_tokens,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": catalog_prompt(catalog, case["question"])}],
        )
        result.latency_ms = round((time.perf_counter() - started) * 1000)
        result.raw_response = response_text(response)
        result.input_tokens, result.output_tokens = usage_counts(response)
        result.selected_group, result.selected_slug = parse_selection(result.raw_response)
        selected = (result.selected_group, result.selected_slug)
        if selected not in valid:
            result.status = "invalid_selection"
            result.error = "selected summary is not present in the catalog"
        else:
            result.correct = selected == expected
            result.status = "pass" if result.correct else "wrong_selection"
    except Exception as exc:
        result.latency_ms = round((time.perf_counter() - started) * 1000)
        result.status = "error"
        result.error = f"{type(exc).__name__}: {exc}"
    return result


def calculate_metrics(results: list[EvalResult]) -> dict[str, Any]:
    skipped_statuses = {"missing_expected_summary"}
    scored = [result for result in results if result.status not in skipped_statuses]
    correct = sum(result.correct for result in scored)
    statuses = Counter(result.status for result in results)
    per_expected: dict[str, dict[str, Any]] = {}
    for result in scored:
        key = f"{result.expected_group}/{result.expected_slug}"
        item = per_expected.setdefault(
            key,
            {"attempts": 0, "correct": 0, "accuracy": 0.0, "statuses": Counter()},
        )
        item["attempts"] += 1
        item["correct"] += int(result.correct)
        item["statuses"][result.status] += 1
    for item in per_expected.values():
        item["accuracy"] = item["correct"] / item["attempts"] if item["attempts"] else 0.0
        item["statuses"] = dict(sorted(item["statuses"].items()))

    confusion_pairs = Counter()
    for result in scored:
        if result.correct:
            continue
        expected = f"{result.expected_group}/{result.expected_slug}"
        selected = (
            f"{result.selected_group}/{result.selected_slug}"
            if result.selected_group and result.selected_slug
            else f"({result.status})"
        )
        confusion_pairs[f"{expected} -> {selected}"] += 1

    return {
        "total_attempts": len(results),
        "scored_attempts": len(scored),
        "skipped_attempts": len(results) - len(scored),
        "correct": correct,
        "accuracy": correct / len(scored) if scored else 0.0,
        "statuses": dict(sorted(statuses.items())),
        "per_expected": dict(sorted(per_expected.items())),
        "confusion_pairs": dict(sorted(confusion_pairs.items(), key=lambda item: (-item[1], item[0]))),
        "average_latency_ms": (
            round(sum(result.latency_ms for result in scored) / len(scored))
            if scored else 0
        ),
        "input_tokens": sum(result.input_tokens or 0 for result in results),
        "output_tokens": sum(result.output_tokens or 0 for result in results),
    }


def format_result(result: EvalResult) -> str:
    lines = [
        f"=== Attempt {result.case_index} / repeat {result.repeat} ===",
        f"Timestamp: {result.timestamp}",
        f"Question: {result.question}",
        f"Expected: {result.expected_group}/{result.expected_slug}",
        f"Selected: {result.selected_group or '(none)'}/{result.selected_slug or '(none)'}",
        f"Status: {result.status}",
        f"Correct: {'yes' if result.correct else 'no'}",
        f"Model: {result.model}",
        f"Provider: {result.provider}",
        f"Latency ms: {result.latency_ms}",
        f"Input tokens: {result.input_tokens if result.input_tokens is not None else '(unavailable)'}",
        f"Output tokens: {result.output_tokens if result.output_tokens is not None else '(unavailable)'}",
        f"Raw response: {result.raw_response or '(none)'}",
    ]
    if result.error:
        lines.append(f"Error: {result.error}")
    return "\n".join(lines)


def format_metrics(metrics: dict[str, Any]) -> str:
    status_text = ", ".join(
        f"{name}={count}" for name, count in metrics["statuses"].items()
    ) or "(none)"
    lines = [
        "=== Accuracy Summary ===",
        f"Total attempts: {metrics['total_attempts']}",
        f"Scored attempts: {metrics['scored_attempts']}",
        f"Skipped attempts: {metrics['skipped_attempts']}",
        f"Correct: {metrics['correct']}",
        f"Accuracy: {metrics['accuracy']:.2%}",
        f"Statuses: {status_text}",
        f"Average latency ms: {metrics['average_latency_ms']}",
        f"Input tokens: {metrics['input_tokens']}",
        f"Output tokens: {metrics['output_tokens']}",
    ]
    if metrics.get("per_expected"):
        lines.append("")
        lines.append("=== Per Expected Summary ===")
        for expected, item in metrics["per_expected"].items():
            statuses = ", ".join(f"{k}={v}" for k, v in item["statuses"].items())
            lines.append(
                f"{expected}: accuracy={item['accuracy']:.2%}, "
                f"correct={item['correct']}/{item['attempts']}, statuses={statuses}"
            )
    if metrics.get("confusion_pairs"):
        lines.append("")
        lines.append("=== Confusion Pairs ===")
        for pair, count in metrics["confusion_pairs"].items():
            lines.append(f"{pair}: {count}")
    return "\n".join(lines)


def append_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(text)
        handle.write("\n\n")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Use a live LLM to select one summary for each curated question and report accuracy."
    )
    parser.add_argument(
        "--cases",
        type=Path,
        default=APP_DIR / "config" / "summary_routing_smoke.json",
    )
    parser.add_argument("--summary-dir", type=Path, default=APP_DIR / "summaries")
    parser.add_argument(
        "--seed-topics",
        type=Path,
        default=APP_DIR / "config" / "seed_topics.tsv",
    )
    parser.add_argument("--provider", default=None)
    parser.add_argument(
        "--model",
        default=llm_settings.get_model("qa"),
    )
    parser.add_argument("--max-output-tokens", type=int, default=100)
    parser.add_argument("--repeats", type=int, default=1)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument(
        "--minimum-accuracy",
        type=float,
        default=None,
        help=(
            "Optional minimum scored accuracy required for success, as a fraction "
            "from 0.0 to 1.0. Errors and invalid selections count as failed scored attempts."
        ),
    )
    parser.add_argument("--log", type=Path, default=None)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate inputs and print planned attempt counts without calling the LLM.",
    )
    args = parser.parse_args(argv)
    args.log = args.log or default_log_path()
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    cases = json.loads(args.cases.read_text(encoding="utf-8"))
    if args.limit is not None:
        cases = cases[:max(0, args.limit)]
    catalog = build_catalog(args.summary_dir, args.seed_topics)
    provider = llm_settings.get_provider(args.provider)
    repeats = max(1, args.repeats)

    print(f"cases: {len(cases)}")
    print(f"catalog_entries: {len(catalog)}")
    print(f"repeats: {repeats}")
    print(f"planned_attempts: {len(cases) * repeats}")
    print(f"provider: {provider}")
    print(f"model: {args.model}")
    print(f"log: {args.log}")
    if args.dry_run:
        return 0

    client = llm_client.create_client(provider)
    results: list[EvalResult] = []
    for repeat in range(1, repeats + 1):
        for case_index, case in enumerate(cases, start=1):
            result = evaluate_case(
                client,
                case,
                catalog,
                case_index=case_index,
                repeat=repeat,
                model=args.model,
                provider=provider,
                max_output_tokens=max(1, args.max_output_tokens),
            )
            results.append(result)
            append_text(args.log, format_result(result))
            print(
                f"[{len(results)}/{len(cases) * repeats}] {result.status} "
                f"{result.expected_group}/{result.expected_slug} -> "
                f"{result.selected_group or '(none)'}/{result.selected_slug or '(none)'}"
            )

    metrics = calculate_metrics(results)
    append_text(args.log, format_metrics(metrics))
    print(json.dumps(metrics, indent=2))
    if args.minimum_accuracy is not None:
        minimum_accuracy = min(1.0, max(0.0, args.minimum_accuracy))
        if metrics["accuracy"] < minimum_accuracy:
            print(
                f"minimum accuracy not met: {metrics['accuracy']:.2%} < {minimum_accuracy:.2%}",
                file=sys.stderr,
            )
            return 1
    return 1 if metrics["statuses"].get("error") or metrics["statuses"].get("invalid_selection") else 0


if __name__ == "__main__":
    raise SystemExit(main())
