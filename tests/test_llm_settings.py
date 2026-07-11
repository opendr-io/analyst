import pytest

from config import llm_settings


def test_load_llm_config_requires_existing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        llm_settings.load_llm_config(tmp_path / "missing.ini")


def test_llm_settings_reads_models_from_ini(tmp_path):
    config_path = tmp_path / "llm.ini"
    config_path.write_text(
        "\n".join(
            [
                "[provider]",
                "name = anthropic",
                "",
                "[models]",
                "qa = claude-test-model",
            ]
        ),
        encoding="utf-8",
    )

    cfg = llm_settings.load_llm_config(config_path)

    assert cfg.get("provider", "name") == "anthropic"
    assert cfg.get("models", "qa") == "claude-test-model"
    with pytest.raises(Exception):
        cfg.get("models", "summarize_author")
