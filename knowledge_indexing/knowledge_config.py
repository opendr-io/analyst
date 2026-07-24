from pathlib import Path


APP_DIR = Path(__file__).resolve().parent.parent
STATE_DIR = APP_DIR / "knowledge"
DB_PATH = STATE_DIR / "knowledge.sqlite3"
LOG_PATH = STATE_DIR / "import.log"
SUMMARY_ARCHIVE_DIR = STATE_DIR / "archive" / "summaries"
LINKEDIN_DB_PATH = APP_DIR / "data" / "linkedin" / "linkedin_ingest.sqlite3"
CONFIG_DIR = APP_DIR / "config"

DEFCON33_LATEST = APP_DIR / "youtube_summaries" / "defcon33" / "defcon33_latest.json"
BSIDESSF_MD = APP_DIR / "pdf" / "markdown" / "BSidesSF_2025_PrintedProgram_PROOF-10.md"


def _find_latest_promptorgtfo() -> Path | None:
    candidates = sorted((APP_DIR / "youtube_summaries").glob("promptorgtfo_*.json"))
    return candidates[-1] if candidates else None


PROMPTORGTFO_LATEST = _find_latest_promptorgtfo()


def _load_text_set(path: Path) -> set[str]:
    if not path.exists():
        return set()
    items: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        value = line.strip().lower()
        if value and not value.startswith("#"):
            items.add(value)
    return items


def _load_seed_topics(path: Path) -> list[tuple[str, str]]:
    topics: list[tuple[str, str]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        value = line.strip()
        if not value or value.startswith("#"):
            continue
        if "\t" not in value:
            raise ValueError(f"{path}:{line_no}: expected '<topic><tab><definition>'")
        name, definition = value.split("\t", 1)
        name = name.strip()
        definition = definition.strip()
        if not name or not definition:
            raise ValueError(f"{path}:{line_no}: topic and definition are required")
        topics.append((name, definition))
    return topics


STOPWORDS = _load_text_set(CONFIG_DIR / "stopwords.txt")
BAD_TOPIC_TOKENS = _load_text_set(CONFIG_DIR / "bad_topic_tokens.txt")
BAD_TOPIC_PHRASES = _load_text_set(CONFIG_DIR / "bad_topic_phrases.txt")
SEED_TOPICS = _load_seed_topics(CONFIG_DIR / "seed_topics.tsv")
