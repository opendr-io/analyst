import configparser
import os
from pathlib import Path


CONFIG_DIR = Path(__file__).resolve().parent
APP_DIR = CONFIG_DIR.parent
DEFAULT_CONFIG_PATH = CONFIG_DIR / "llm.ini"


def load_llm_config(path: Path | None = None) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    config_path = path or Path(os.getenv("LLM_CONFIG", DEFAULT_CONFIG_PATH))
    if not config_path.exists():
        raise FileNotFoundError(f"LLM config file not found: {config_path}")
    cfg.read(config_path, encoding="utf-8")
    return cfg


_CONFIG = load_llm_config()


def get_str(section: str, option: str) -> str:
    return _CONFIG.get(section, option)


def get_int(section: str, option: str) -> int:
    return _CONFIG.getint(section, option)


def get_provider(explicit: str | None = None) -> str:
    return (explicit or os.getenv("LLM_PROVIDER") or get_str("provider", "name")).strip().lower()


def get_model(name: str) -> str:
    env_name = f"LLM_MODEL_{name.upper()}"
    return os.getenv(env_name) or get_str("models", name)
