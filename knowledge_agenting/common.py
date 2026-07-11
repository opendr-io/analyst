import json
from pathlib import Path

from knowledge_indexing import knowledge_index as ki
from config import llm_settings


PROMPT_DIR = Path(__file__).resolve().parent / "prompts"

MODEL_CLASSIFY = llm_settings.get_model("classify")
MODEL_ANNOTATE = llm_settings.get_model("annotate")
MODEL_SUMMARIZE = llm_settings.get_model("summarize")

SUMMARY_RECORD_LIMIT = llm_settings.get_int("summary", "record_limit")
SUMMARY_RECORD_CHARS = llm_settings.get_int("summary", "record_chars")
SUMMARY_CHUNK_SIZE = llm_settings.get_int("summary", "chunk_size")
SUMMARY_CHARS_PER_TOKEN = llm_settings.get_int("summary", "chars_per_token")
ANNOTATION_SCHEMA_VERSION = llm_settings.get_int("annotation", "schema_version")
ANNOTATION_RECORD_CHARS = llm_settings.get_int("annotation", "record_chars")
ANNOTATION_MAX_INPUT_TOKENS = llm_settings.get_int("annotation", "max_input_tokens")
ANNOTATION_MAX_OUTPUT_TOKENS = llm_settings.get_int("annotation", "max_output_tokens")
ANNOTATION_DEFAULT_BATCH_SIZE = llm_settings.get_int("annotation", "default_batch_size")
CLASSIFICATION_SCHEMA_VERSION = llm_settings.get_int("classification", "schema_version")
CLASSIFICATION_MAX_INPUT_TOKENS = llm_settings.get_int("classification", "max_input_tokens")
CLASSIFICATION_MAX_OUTPUT_TOKENS = llm_settings.get_int("classification", "max_output_tokens")
CLASSIFICATION_DEFAULT_BATCH_SIZE = llm_settings.get_int("classification", "default_batch_size")
OPEN_TOPICS_MAX_OUTPUT_TOKENS = llm_settings.get_int("open_topics", "max_output_tokens")

TOPICS = [name for name, _ in ki.SEED_TOPICS]


def load_prompt(name: str) -> str:
    return (PROMPT_DIR / name).read_text(encoding="utf-8").strip()


CLASSIFY_SYSTEM_TEMPLATE = load_prompt("classify_system.txt")
ANNOTATE_SYSTEM = load_prompt("annotate_system.txt")

_TOPICS_NUMBERED = "\n".join(
    f"{i + 1}. {name}\n   Definition: {definition}"
    for i, (name, definition) in enumerate(ki.SEED_TOPICS)
)
CLASSIFY_SYSTEM = (
    CLASSIFY_SYSTEM_TEMPLATE
    .replace("{topic_count}", str(len(ki.SEED_TOPICS)))
    .replace("{topics_numbered}", _TOPICS_NUMBERED)
)


def strip_code_fence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text


def as_string_list(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def json_list_text(value: str | None) -> str:
    if not value:
        return ""
    try:
        loaded = json.loads(value)
    except json.JSONDecodeError:
        return ""
    if not isinstance(loaded, list):
        return ""
    return ", ".join(str(item).strip() for item in loaded if str(item).strip())


def estimate_tokens(text: str) -> int:
    return max(1, (len(text) + SUMMARY_CHARS_PER_TOKEN - 1) // SUMMARY_CHARS_PER_TOKEN)
