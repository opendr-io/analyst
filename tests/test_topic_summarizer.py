from knowledge_agenting import topic_summarizer as ts
from knowledge_indexing.knowledge_authors import split_authors
from types import SimpleNamespace

import pytest


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
    source_year_group = ts.SummaryGroup("source-year", "blackhat-2026", "Source: blackhat (2026)", "", "")
    author_group = ts.SummaryGroup("author", "Example Speaker", "Author: Example Speaker", "", "")

    assert ts.grouped_paths(tmp_path, topic_group).summary == tmp_path / "topics" / "threat-modeling.md"
    assert ts.grouped_paths(tmp_path, source_group).summary == tmp_path / "sources" / "defcon33.md"
    assert ts.grouped_paths(tmp_path, source_year_group).summary == tmp_path / "sources" / "blackhat-2026.md"
    assert ts.grouped_paths(tmp_path, author_group).summary == tmp_path / "authors" / "example-speaker.md"
    assert ts.grouped_paths(tmp_path, topic_group).audit == tmp_path / "artifacts" / "topics" / "threat-modeling.audit.json"
    assert ts.grouped_paths(tmp_path, source_group).prompt_input == tmp_path / "artifacts" / "sources" / "defcon33.prompt-input.md"
    assert ts.grouped_paths(tmp_path, source_year_group).prompt_input == tmp_path / "artifacts" / "sources" / "blackhat-2026.prompt-input.md"
    assert ts.grouped_paths(tmp_path, author_group).manifest == tmp_path / "artifacts" / "authors" / "example-speaker.manifest.json"
    assert ts.grouped_paths(tmp_path, source_year_group).validation == tmp_path / "artifacts" / "sources" / "blackhat-2026.validation.json"


def test_make_source_and_author_groups_have_report_context(tmp_path):
    source = ts.make_summary_group(tmp_path / "missing.sqlite3", "source", "defcon33")
    source_year = ts.make_summary_group(tmp_path / "missing.sqlite3", "source-year", "blackhat:2026")
    author = ts.make_summary_group(tmp_path / "missing.sqlite3", "author", "Example Speaker")

    assert source.group_by == "source"
    assert source.label == "Source: defcon33"
    assert "all records from source defcon33" in source.description
    assert source_year.group_by == "source-year"
    assert source_year.name == "blackhat-2026"
    assert source_year.label == "Source: blackhat (2026)"
    assert "blackhat in 2026" in source_year.description
    assert author.group_by == "author"
    assert author.label == "Author: Example Speaker"
    assert "Example Speaker" in author.description


def test_parse_args_supports_source_year_group():
    args = ts.parse_args(["--group-by", "source-year", "--source-year", "blackhat:2026"])

    assert args.group_by == "source-year"
    assert args.source_year == ["blackhat:2026"]


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
    assert ts.model_for_group("source-year") == ts.MODEL_SUMMARIZE


def test_parse_source_year_accepts_common_forms():
    assert ts.parse_source_year("blackhat:2026") == ("blackhat", "2026")
    assert ts.parse_source_year("bsideslv/2026") == ("bsideslv", "2026")
    assert ts.parse_source_year("defcon34-2026") == ("defcon34", "2026")


def test_source_year_listing_and_loading_filters_records(tmp_path):
    db_path = tmp_path / "knowledge.sqlite3"
    with ts.ki.open_db(db_path) as conn:
        conn.execute(
            """
            INSERT INTO topics (name, query, description, source, created_at, updated_at)
            VALUES ('Application security', 'appsec', 'appsec', 'seed', 'now', 'now')
            """
        )
        for record_id, source, year in [
            (1, "blackhat", "2025"),
            (2, "blackhat", "2026"),
            (3, "blackhat", "2026"),
            (4, "bsideslv", "2026"),
        ]:
            conn.execute(
                """
                INSERT INTO records (
                    id, source, source_file, source_record_id, dedupe_key, title, author,
                    text, url, event, year, tags, raw_json, imported_at, agent_topics
                )
                VALUES (?, ?, 'test.json', ?, ?, ?, 'Speaker', 'Text', '',
                        'Event', ?, '', '{}', 'now', '|Application security|')
                """,
                (record_id, source, str(record_id), f"{source}:{year}:{record_id}", f"Talk {record_id}", year),
            )
            conn.execute(
                """
                INSERT INTO record_classifications (
                    record_id, model, schema_version, primary_topic, secondary_topics_json,
                    confidence, rationale, new_topic_candidate, raw_json, created_at, updated_at
                )
                VALUES (?, 'model', 1, 'Application security', '[]', 'high', '', '', '{}', 'now', 'now')
                """,
                (record_id,),
            )
            conn.execute(
                """
                INSERT INTO record_annotations (
                    record_id, model, schema_version, short_summary, keywords_json, tools_json,
                    people_json, claims_json, use_cases_json, ai_relevance, content_types_json,
                    security_domains_json, source_quality, contains_prompt_injection, relevance_notes,
                    raw_json, created_at, updated_at
                )
                VALUES (?, 'model', 1, 'summary', '[]', '[]', '[]', '[]', '[]', '',
                        '[]', '[]', '', 0, '', '{}', 'now', 'now')
                """,
                (record_id,),
            )
        conn.commit()

    assert ts.list_source_years_for_summary(db_path) == [
        "blackhat:2025",
        "blackhat:2026",
        "bsideslv:2026",
    ]
    group = ts.make_summary_group(db_path, "source-year", "blackhat:2026")
    rows = ts.load_group_rows(db_path, group)

    assert [row["id"] for row in rows] == [2, 3]


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


def test_print_summary_result_includes_validation_status(capsys):
    ts.print_summary_result(
        {
            "summary_status": "complete",
            "validation_status": "pass",
            "expected_record_count": 2,
            "estimated_input_tokens": 100,
            "output_max_tokens": 3000,
            "artifacts_written": True,
            "summary_input_artifact_path": "summaries/artifacts/sources/example.prompt-input.md",
            "audit_file_path": "summaries/artifacts/sources/example.audit.json",
            "validation_file_path": "summaries/artifacts/sources/example.validation.json",
            "summary_file_path": "summaries/sources/example.md",
        },
        dry_run=False,
    )

    output = capsys.readouterr().out
    assert "  validation_status: pass" in output
    assert "  validation: summaries/artifacts/sources/example.validation.json" in output


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


def _write_validation_artifacts(summary_dir, group, summary):
    paths = ts.grouped_paths(summary_dir, group)
    paths.summary.parent.mkdir(parents=True)
    paths.audit.parent.mkdir(parents=True)
    prompt = "## [record_id:1]\nSource one\n\n## [record_id:2]\nSource two\n"
    paths.summary.write_text(summary, encoding="utf-8")
    paths.prompt_input.write_text(prompt, encoding="utf-8")
    summary_hash = ts.text_hash(summary)
    prompt_hash = ts.text_hash(prompt)
    ts.write_json(
        paths.audit,
        {
            "group_by": group.group_by,
            "group_name": group.name,
            "expected_record_count": 2,
            "expected_record_ids": [1, 2],
            "summary_hash": summary_hash,
        },
    )
    ts.write_json(
        paths.manifest,
        {
            "group_by": group.group_by,
            "group_name": group.name,
            "status": "complete",
            "summary_hash": summary_hash,
            "prompt_hash": prompt_hash,
        },
    )
    return paths


def test_validate_summary_group_passes_complete_summary(tmp_path):
    group = ts.SummaryGroup("source", "defcon33", "Source: defcon33", "", "")
    summary = """# Topic: Source: defcon33

## Executive Summary
Summary [record_id:1].

## Research Landscape
Landscape.

## Major Themes And Trends
Themes.

## Methods, Tools, And Approaches Discussed
Methods.

## Notable Talks, Records, And Evidence
Evidence [record_id:2].

## Gaps, Limits, And Open Questions
Gaps.

## Coverage And Evidence Notes
Coverage [record_id:1] [record_id:2].
"""
    paths = _write_validation_artifacts(tmp_path, group, summary)

    validation = ts.validate_summary_group(tmp_path, group)

    assert validation["validation_status"] == "pass_with_warnings"
    assert validation["errors"] == []
    assert paths.validation.exists()


def test_validate_summary_group_fails_missing_record_and_section(tmp_path):
    group = ts.SummaryGroup("source", "defcon33", "Source: defcon33", "", "")
    summary = """# Topic: Source: defcon33

## Executive Summary
Summary [record_id:1].
"""
    _write_validation_artifacts(tmp_path, group, summary)

    validation = ts.validate_summary_group(tmp_path, group)

    assert validation["validation_status"] == "fail"
    assert any("missing output record ids" in error for error in validation["errors"])
    assert any("missing required sections" in error for error in validation["errors"])


def test_validate_summaries_cli_reports_selected_group(monkeypatch, tmp_path, capsys):
    group = ts.SummaryGroup("source", "defcon33", "Source: defcon33", "", "")
    monkeypatch.setattr(ts, "groups_from_args", lambda args: [group])
    _write_validation_artifacts(
        tmp_path,
        group,
        """# Topic: Source: defcon33

## Executive Summary
Summary [record_id:1].

## Research Landscape
Landscape.

## Major Themes And Trends
Themes.

## Methods, Tools, And Approaches Discussed
Methods.

## Notable Talks, Records, And Evidence
Evidence [record_id:2].

## Gaps, Limits, And Open Questions
Gaps.

## Coverage And Evidence Notes
Coverage [record_id:1] [record_id:2].
""",
    )

    result = ts.main(["--summary-dir", str(tmp_path), "--group-by", "source", "--source", "defcon33", "--validate-summaries"])

    output = capsys.readouterr().out
    assert result == 0
    assert "validation_status: pass_with_warnings" in output
    assert "validated: 1" in output


def test_write_preflight_artifacts_requires_dry_run(capsys):
    result = ts.main(["--topic", "Threat modeling", "--write-preflight-artifacts"])

    error = capsys.readouterr().err
    assert result == 2
    assert "--write-preflight-artifacts requires --dry-run" in error

def test_archive_existing_moves_outputs_under_archive_root(tmp_path):
    group = ts.SummaryGroup("topic", "Threat modeling", "Threat modeling", "", "")
    paths = ts.grouped_paths(tmp_path, group)
    paths.summary.parent.mkdir(parents=True)
    paths.audit.parent.mkdir(parents=True)
    paths.summary.write_text("old summary", encoding="utf-8")
    paths.audit.write_text("old audit", encoding="utf-8")

    archived = ts.archive_existing(
        paths,
        tmp_path / "artifacts" / "topics" / "archive",
        "20260715T000000Z",
        summary_dir=tmp_path,
    )

    archived_paths = [ts.Path(path) for path in archived]
    assert tmp_path / "artifacts" / "topics" / "archive" / "20260715T000000Z" / "threat-modeling.md" in archived_paths
    assert tmp_path / "artifacts" / "topics" / "archive" / "20260715T000000Z" / "threat-modeling.audit.json" in archived_paths
    assert not paths.summary.exists()
    assert not paths.audit.exists()


def test_archive_existing_rejects_source_outside_summary_dir(tmp_path):
    outside = tmp_path.parent / f"{tmp_path.name}-outside.md"
    outside.write_text("do not move", encoding="utf-8")
    paths = ts.TopicPaths(
        summary=outside,
        audit=tmp_path / "artifacts" / "topics" / "safe.audit.json",
        prompt_input=tmp_path / "artifacts" / "topics" / "safe.prompt-input.md",
        manifest=tmp_path / "artifacts" / "topics" / "safe.manifest.json",
        validation=tmp_path / "artifacts" / "topics" / "safe.validation.json",
    )

    with pytest.raises(ValueError, match="archive source must stay within summary_dir"):
        ts.archive_existing(
            paths,
            tmp_path / "artifacts" / "topics" / "archive",
            "20260715T000000Z",
            summary_dir=tmp_path,
        )

    assert outside.exists()
    outside.unlink()


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
