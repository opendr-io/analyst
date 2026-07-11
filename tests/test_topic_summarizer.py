from knowledge_agenting import topic_summarizer as ts
from knowledge_indexing.knowledge_authors import split_authors
from types import SimpleNamespace


def _record(record_id: int = 42) -> dict:
    return {
        "id": record_id,
        "source": "blackhat",
        "source_record_id": "source-42",
        "title": "Example Talk",
        "author": "Example Speaker",
        "event": "Example Event",
        "year": "2026",
        "url": "https://example.test/talk",
        "tags": "Briefings",
        "primary_topic": "Threat modeling",
        "secondary_topics_json": "[]",
        "text": "This talk discusses threat modeling with AI systems.",
    }


def test_topic_summary_prompt_is_loaded_from_prompt_files():
    assert ts.TOPIC_SUMMARY_USER_PROMPT.exists()
    assert ts.TOPIC_SUMMARY_SYSTEM_PROMPT.exists()

    prompt = ts.build_prompt(
        "Threat modeling",
        [_record()],
        {
            "query": "Threat modeling query",
            "description": "Threat modeling description",
        },
    )

    assert "Topic: Threat modeling" in prompt
    assert "Threat modeling query" in prompt
    assert "## Executive Summary" in prompt
    assert "## Coverage And Evidence Notes" in prompt
    assert "## [record_id:42]" in prompt
    assert "{topic}" not in prompt
    assert "{records_text}" not in prompt


def test_topic_summary_system_prompt_is_external_report_prompt():
    system = ts.build_system_prompt()

    assert "long-form research report" in system
    assert "Do not write database-style indexes" in system


def test_grouped_paths_use_group_subdirectories(tmp_path):
    topic_group = ts.SummaryGroup("topic", "Threat modeling", "Threat modeling", "", "")
    source_group = ts.SummaryGroup("source", "defcon33", "Source: defcon33", "", "")
    author_group = ts.SummaryGroup("author", "Example Speaker", "Author: Example Speaker", "", "")

    assert ts.grouped_paths(tmp_path, topic_group).summary == tmp_path / "topics" / "threat-modeling.md"
    assert ts.grouped_paths(tmp_path, source_group).summary == tmp_path / "sources" / "defcon33.md"
    assert ts.grouped_paths(tmp_path, author_group).summary == tmp_path / "authors" / "example-speaker.md"
    assert ts.grouped_paths(tmp_path, topic_group).audit == tmp_path / "artifacts" / "topics" / "threat-modeling.audit.json"
    assert ts.grouped_paths(tmp_path, source_group).prompt_input == tmp_path / "artifacts" / "sources" / "defcon33.prompt-input.md"
    assert ts.grouped_paths(tmp_path, author_group).manifest == tmp_path / "artifacts" / "authors" / "example-speaker.manifest.json"


def test_make_source_and_author_groups_have_report_context(tmp_path):
    source = ts.make_summary_group(tmp_path / "missing.sqlite3", "source", "defcon33")
    author = ts.make_summary_group(tmp_path / "missing.sqlite3", "author", "Example Speaker")

    assert source.group_by == "source"
    assert source.label == "Source: defcon33"
    assert "all records from source defcon33" in source.description
    assert author.group_by == "author"
    assert author.label == "Author: Example Speaker"
    assert "Example Speaker" in author.description


def test_parse_args_supports_parallel():
    args = ts.parse_args(["--group-by", "source", "--source", "defcon33", "--parallel", "3"])

    assert args.parallel == 3


def test_parse_args_supports_skip_existing():
    args = ts.parse_args(["--group-by", "author", "--all", "--skip-existing"])

    assert args.skip_existing is True


def test_parse_args_leaves_group_specific_minimum_unset():
    args = ts.parse_args(["--group-by", "author", "--all"])

    assert args.min_records is None


def test_model_for_group_uses_author_specific_model():
    assert ts.model_for_group("author") == ts.llm_settings.get_model("summarize_author")
    assert ts.model_for_group("topic") == ts.MODEL_SUMMARIZE
    assert ts.model_for_group("source") == ts.MODEL_SUMMARIZE


def test_split_authors_expands_common_coauthor_separators():
    assert split_authors(
        "Alice Example; Bob Example, Carol Example & Dan Example and Erin Example"
    ) == [
        "Alice Example",
        "Bob Example",
        "Carol Example",
        "Dan Example",
        "Erin Example",
    ]
    assert split_authors("& Michael Sulmeyer") == ["Michael Sulmeyer"]


def test_parse_args_places_legacy_check_dirs_under_summaries():
    args = ts.parse_args(["--summary-dir", "summaries-validation", "--topic", "Threat modeling"])

    assert args.summary_dir == ts.DEFAULT_SUMMARY_DIR / "summaries-validation"


def test_parse_args_keeps_explicit_nested_summary_dir():
    args = ts.parse_args(["--summary-dir", "summaries/summaries-validation", "--topic", "Threat modeling"])

    assert args.summary_dir == ts.DEFAULT_SUMMARY_DIR / "summaries-validation"


def test_parse_args_keeps_default_summary_dir():
    args = ts.parse_args(["--topic", "Threat modeling"])

    assert args.summary_dir == ts.DEFAULT_SUMMARY_DIR


def test_normalized_parallelism_is_bounded():
    assert ts.normalized_parallelism(0) == 1
    assert ts.normalized_parallelism(4) == 4
    assert ts.normalized_parallelism(99) == 8


def test_filter_existing_groups_skips_existing_summary_files(tmp_path):
    existing = ts.SummaryGroup("author", "Existing Speaker", "Author: Existing Speaker", "", "")
    missing = ts.SummaryGroup("author", "Missing Speaker", "Author: Missing Speaker", "", "")
    existing_path = ts.grouped_paths(tmp_path, existing).summary
    existing_path.parent.mkdir(parents=True)
    existing_path.write_text("# Existing Speaker\n", encoding="utf-8")

    pending, skipped = ts.filter_existing_groups(tmp_path, [existing, missing])

    assert pending == [missing]
    assert skipped == [existing]


def test_print_dry_run_totals_sums_token_estimates(capsys):
    ts.print_dry_run_totals([
        {
            "expected_record_count": 2,
            "estimated_input_tokens": 100,
            "output_max_tokens": 3000,
        },
        {
            "expected_record_count": 3,
            "estimated_input_tokens": 250,
            "output_max_tokens": 8000,
        },
    ])

    output = capsys.readouterr().out
    assert "dry_run_totals:" in output
    assert "  summaries: 2" in output
    assert "  records: 5" in output
    assert "  estimated_input_tokens: 350" in output
    assert "  output_max_tokens: 11000" in output


def test_list_existing_summaries_reads_manifest_and_audit(tmp_path):
    summary_dir = tmp_path / "summaries"
    topic_dir = summary_dir / "topics"
    artifact_dir = summary_dir / "artifacts" / "topics"
    topic_dir.mkdir(parents=True)
    artifact_dir.mkdir(parents=True)
    (topic_dir / "threat-modeling.md").write_text("# Threat modeling\n", encoding="utf-8")
    ts.write_json(
        artifact_dir / "threat-modeling.manifest.json",
        {
            "group_by": "topic",
            "group_name": "Threat modeling",
            "status": "complete",
            "generated_at": "2026-01-02T03:04:05+00:00",
        },
    )
    ts.write_json(
        artifact_dir / "threat-modeling.audit.json",
        {
            "group_by": "topic",
            "group_name": "Threat modeling",
            "summary_status": "complete",
            "expected_record_count": 12,
        },
    )

    listings = ts.list_existing_summaries(summary_dir)

    assert len(listings) == 1
    assert listings[0].name == "Threat modeling"
    assert listings[0].status == "complete"
    assert listings[0].records == 12
    assert listings[0].generated_at == "2026-01-02T03:04:05+00:00"
    assert listings[0].summary_path == topic_dir / "threat-modeling.md"


def test_list_summaries_mode_does_not_require_topic(tmp_path, capsys):
    summary_dir = tmp_path / "summaries"
    (summary_dir / "topics").mkdir(parents=True)
    (summary_dir / "topics" / "file-only.md").write_text("# File only\n", encoding="utf-8")

    result = ts.main(["--summary-dir", str(summary_dir), "--list-summaries"])

    output = capsys.readouterr().out
    assert result == 0
    assert "file-only" in output
    assert "file_only" in output
    assert "summaries: 1" in output


def test_list_topics_mode_does_not_require_topic(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(ts, "list_topics_for_summary", lambda db_path: ["Application security", "Threat modeling"])

    result = ts.main(["--db", str(tmp_path / "knowledge.sqlite3"), "--list-topics"])

    output = capsys.readouterr().out
    assert result == 0
    assert "Application security" in output
    assert "Threat modeling" in output
    assert "topics: 2" in output


def test_list_topics_mode_rejects_non_topic_group(capsys):
    result = ts.main(["--group-by", "source", "--list-topics"])

    error = capsys.readouterr().err
    assert result == 2
    assert "--list-topics only applies to --group-by topic" in error


def test_skip_existing_allows_all_existing_groups_to_exit_cleanly(monkeypatch, tmp_path, capsys):
    group = ts.SummaryGroup("author", "Existing Speaker", "Author: Existing Speaker", "", "")
    summary_path = ts.grouped_paths(tmp_path, group).summary
    summary_path.parent.mkdir(parents=True)
    summary_path.write_text("# Existing Speaker\n", encoding="utf-8")
    monkeypatch.setattr(ts, "groups_from_args", lambda args: [group])

    result = ts.main(["--summary-dir", str(tmp_path), "--group-by", "author", "--all", "--skip-existing"])

    output = capsys.readouterr().out
    assert result == 0
    assert "skipped_existing: 1" in output
    assert "no summaries to generate" in output


def test_list_missing_reports_only_missing_summary_files(monkeypatch, tmp_path, capsys):
    existing = ts.SummaryGroup("author", "Existing Speaker", "Author: Existing Speaker", "", "")
    missing = ts.SummaryGroup("author", "Missing Speaker", "Author: Missing Speaker", "", "")
    summary_path = ts.grouped_paths(tmp_path, existing).summary
    summary_path.parent.mkdir(parents=True)
    summary_path.write_text("# Existing Speaker\n", encoding="utf-8")
    monkeypatch.setattr(ts, "groups_from_args", lambda args: [existing, missing])

    result = ts.main(["--summary-dir", str(tmp_path), "--group-by", "author", "--all", "--list-missing"])

    output = capsys.readouterr().out
    assert result == 0
    assert "Missing Speaker" in output
    assert "Existing Speaker" not in output
    assert "missing: 1" in output


def test_write_preflight_artifacts_requires_dry_run(capsys):
    result = ts.main(["--topic", "Threat modeling", "--write-preflight-artifacts"])

    error = capsys.readouterr().err
    assert result == 2
    assert "--write-preflight-artifacts requires --dry-run" in error


def test_summarize_group_dry_run_is_read_only_by_default(monkeypatch, tmp_path):
    group = ts.SummaryGroup("author", "Existing Speaker", "Author: Existing Speaker", "", "")
    paths = ts.grouped_paths(tmp_path, group)
    paths.prompt_input.parent.mkdir(parents=True)
    paths.prompt_input.write_text("old prompt", encoding="utf-8")
    paths.audit.write_text("old audit", encoding="utf-8")
    paths.manifest.write_text("old manifest", encoding="utf-8")
    monkeypatch.setattr(ts, "run_global_preflight", lambda db_path: {"ok": True})
    monkeypatch.setattr(
        ts,
        "preflight_group",
        lambda db_path, group, max_input_tokens: (
            [],
            {},
            "new prompt",
            {
                "expected_record_count": 0,
                "expected_record_ids": [],
                "estimated_input_tokens": 0,
                "output_max_tokens": 3000,
            },
        ),
    )
    monkeypatch.setattr(ts, "topic_table_hash", lambda db_path: "topic-hash")
    monkeypatch.setattr(ts, "source_fingerprint", lambda label, records, topic_def: "source-hash")
    monkeypatch.setattr(ts, "file_fingerprint", lambda db_path: {"path": str(db_path)})

    audit = ts.summarize_group(
        group=group,
        db_path=tmp_path / "knowledge.sqlite3",
        summary_dir=tmp_path,
        dry_run=True,
    )

    assert audit["artifacts_written"] is False
    assert paths.prompt_input.read_text(encoding="utf-8") == "old prompt"
    assert paths.audit.read_text(encoding="utf-8") == "old audit"
    assert paths.manifest.read_text(encoding="utf-8") == "old manifest"
    assert not (paths.prompt_input.parent / "archive").exists()


def test_summarize_group_can_write_preflight_artifacts_without_archiving(monkeypatch, tmp_path):
    group = ts.SummaryGroup("author", "Existing Speaker", "Author: Existing Speaker", "", "")
    paths = ts.grouped_paths(tmp_path, group)
    paths.prompt_input.parent.mkdir(parents=True)
    paths.prompt_input.write_text("old prompt", encoding="utf-8")
    monkeypatch.setattr(ts, "run_global_preflight", lambda db_path: {"ok": True})
    monkeypatch.setattr(
        ts,
        "preflight_group",
        lambda db_path, group, max_input_tokens: (
            [],
            {},
            "new prompt",
            {
                "expected_record_count": 0,
                "expected_record_ids": [],
                "estimated_input_tokens": 0,
                "output_max_tokens": 3000,
            },
        ),
    )
    monkeypatch.setattr(ts, "topic_table_hash", lambda db_path: "topic-hash")
    monkeypatch.setattr(ts, "source_fingerprint", lambda label, records, topic_def: "source-hash")
    monkeypatch.setattr(ts, "file_fingerprint", lambda db_path: {"path": str(db_path)})

    audit = ts.summarize_group(
        group=group,
        db_path=tmp_path / "knowledge.sqlite3",
        summary_dir=tmp_path,
        dry_run=True,
        write_preflight_artifacts=True,
    )

    assert audit["artifacts_written"] is True
    assert paths.prompt_input.read_text(encoding="utf-8") == "new prompt"
    assert paths.audit.exists()
    assert paths.manifest.exists()
    assert not (paths.prompt_input.parent / "archive").exists()


def test_repair_missing_ids_appends_addendum_and_includes_source_evidence():
    calls = []

    class FakeMessages:
        def create(self, **kwargs):
            calls.append(kwargs)
            return SimpleNamespace(
                content=[SimpleNamespace(text="## Coverage Addendum\n\nEvidence [record_id:2].")]
            )

    client = SimpleNamespace(messages=FakeMessages())
    repaired = ts.repair_missing_ids(
        client,
        "Threat modeling",
        "# Existing report\n\nPrior evidence [record_id:1].",
        "## [record_id:2]\nMissing source evidence.",
        [2],
        4000,
    )

    assert repaired.startswith("# Existing report")
    assert "[record_id:1]" in repaired
    assert repaired.endswith("Evidence [record_id:2].")
    repair_prompt = calls[0]["messages"][0]["content"]
    assert "Return only an addendum" in repair_prompt
    assert "## [record_id:2]\nMissing source evidence." in repair_prompt
