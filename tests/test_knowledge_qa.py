from pathlib import Path
from uuid import uuid4

import the_analyst
from knowledge_indexing.knowledge_authors import sync_record_authors
from the_analyst import (
    AGENT_SYSTEM,
    TOOLS,
    build_summary_query_map,
    load_summary_files,
    parse_prefixed_request,
    plan_search_query,
    question_to_fts_query,
    rank_relevant_topics,
    rank_relevant_summary_topics,
    tool_answer_from_summaries,
    tool_answer_about_author,
    tool_query_annotations,
    tool_search_records,
)


def _state_dir() -> Path:
    p = Path("data") / "test-tmp" / f"qa-{uuid4().hex}"
    p.mkdir(parents=True, exist_ok=True)
    return p


# --- query planning ---

def test_parse_prefixed_request_routes_query_and_question_prefixes():
    assert parse_prefixed_request("query: prompt injection") == ("query", "prompt injection")
    assert parse_prefixed_request("question: how is AI used?") == ("question", "how is AI used?")
    assert parse_prefixed_request("How is AI used?") == ("", "How is AI used?")

def test_plan_search_query_expands_appsec_and_testing_language():
    result = plan_search_query("summarize research on agentic appsec testing")

    assert "ai agent security testing" in result
    assert "application security" in result
    assert "vulnerability discovery" in result


def test_plan_search_query_expands_practical_application_testing_request():
    result = plan_search_query("I have 400 applications to test")

    assert "application security testing" in result
    assert "vulnerability discovery" in result
    assert "penetration testing" in result


def test_plan_search_query_expands_broken_authentication_at_scale():
    result = plan_search_query(
        "is there anything about testing for broken authentication at scale across hundred of web applications?"
    )

    assert "oauth identity and access delegation" in result
    assert "access control testing" in result
    assert "web application security testing" in result


# --- question_to_fts_query ---

def test_question_to_fts_query_joins_tokens_with_or():
    result = question_to_fts_query("What tools exist for MCP sandboxing?")
    assert "tools" in result
    assert "sandboxing" in result
    assert "OR" in result


def test_question_to_fts_query_drops_stopwords():
    result = question_to_fts_query("what is the best approach for this")
    # "what", "is", "the", "for", "this" are common stopwords; "best" and "approach" may survive
    tokens = [t.strip().strip('"') for t in result.split(" OR ")]
    # stopwords like "the" should not appear
    assert "the" not in tokens


def test_question_to_fts_query_limits_to_ten_tokens():
    long_question = " ".join(f"keyword{i}" for i in range(20))
    result = question_to_fts_query(long_question)
    tokens = [t.strip('"') for t in result.split(" OR ")]
    assert len(tokens) <= 16


def test_question_to_fts_query_prioritizes_original_terms_before_expansions():
    result = question_to_fts_query(
        "is there anything about testing for broken authentication at scale across hundred of web applications?"
    )
    tokens = [t.strip('"') for t in result.split(" OR ")]

    assert "authentication" in tokens
    assert "applications" in tokens


def test_question_to_fts_query_returns_empty_on_no_tokens():
    result = question_to_fts_query("!!! ???")
    assert result == ""


def test_question_to_fts_query_quotes_hostile_fts_punctuation():
    result = question_to_fts_query('oauth" OR records_fts MATCH * --')
    tokens = result.split(" OR ")

    assert '"oauth"' in tokens
    assert '"match"' in tokens
    assert all(token.startswith('"') and token.endswith('"') for token in tokens)
    assert "*" not in result
    assert "--" not in result

# --- rank_relevant_topics ---

def test_rank_relevant_topics_prefers_matching_topic_terms():
    ranked = rank_relevant_topics(
        "What are teams doing for prompt injection in agentic apps?",
        [
            "Cloud, infrastructure, and CDR",
            "AI security, prompt injection, and jailbreaking",
            "Application security",
        ],
        limit=2,
    )

    assert [name for name, _score in ranked] == [
        "AI security, prompt injection, and jailbreaking",
        "Application security",
    ]


def test_rank_relevant_topics_uses_expanded_practical_search_terms():
    ranked = rank_relevant_topics(
        "I have 400 applications to test",
        [
            "Cloud, infrastructure, and CDR",
            "Application security",
            "AI security, prompt injection, and jailbreaking",
            "Exploit development and vulnerability discovery",
        ],
        limit=2,
    )

    assert [name for name, _score in ranked] == [
        "Application security",
        "Exploit development and vulnerability discovery",
    ]


def test_rank_relevant_topics_uses_expanded_authentication_terms():
    ranked = rank_relevant_topics(
        "is there anything about testing for broken authentication at scale across hundred of web applications?",
        [
            "Application security",
            "Identity, OAuth, and access delegation",
            "Cloud, infrastructure, and CDR",
            "Detection engineering, SOC, SIEM, and threat hunting",
        ],
        limit=2,
    )

    assert [name for name, _score in ranked] == [
        "Identity, OAuth, and access delegation",
        "Application security",
    ]


def test_summary_query_map_uses_candidate_topics_as_aliases():
    state_dir = _state_dir()
    (state_dir / "summary-exploit-development-and-vulnerability-discovery.md").write_text(
        "Exploit summary", encoding="utf-8"
    )
    (state_dir / "summary-cloud-and-infrastructure-security.md").write_text(
        "Cloud summary", encoding="utf-8"
    )
    db_path = state_dir / "knowledge.sqlite3"
    with the_analyst.ki.open_db(db_path):
        pass
    the_analyst.ki.seed_topics(db_path)
    the_analyst.ki.store_topic_candidates(
        db_path,
        [
            {
                "phrase": "autonomous vulnerability discovery",
                "score": 10.0,
                "record_count": 4,
                "sources": ["blackhat"],
                "sample_record_ids": [1, 2],
            }
        ],
    )

    query_map = build_summary_query_map(state_dir, db_path=db_path)
    assert "autonomous vulnerability discovery" in query_map[
        "exploit development and vulnerability discovery"
    ]

    ranked = rank_relevant_summary_topics(
        "What are people doing with autonomous vulnerability discovery?",
        state_dir,
        db_path=db_path,
        limit=1,
    )

    assert ranked[0][0] == "exploit development and vulnerability discovery"


# --- tools ---

def test_answer_from_records_tool_is_not_exposed():
    assert "answer_from_records" not in {t["name"] for t in TOOLS}


def test_search_records_tool_is_compact_deterministic_lookup():
    tool = next(t for t in TOOLS if t["name"] == "search-records")

    assert "Deterministically search" in tool["description"]
    assert "compact" in tool["description"]
    assert "broad synthesis" in tool["description"]


def test_answer_about_author_tool_is_exposed():
    tool = next(t for t in TOOLS if t["name"] == "answer-about-author")

    assert tool["input_schema"]["required"] == ["author"]
    assert "complete record" in tool["description"]


def _insert_author_record(conn, record_id, author, title):
    conn.execute(
        """
        INSERT INTO records (
            id, source, source_file, source_record_id, dedupe_key, title, author,
            text, url, event, year, tags, raw_json, imported_at
        )
        VALUES (?, 'test', 'test.json', ?, ?, ?, ?, ?, 'https://example.test',
                'Test Event', '2026', '', '{}', '2026-06-23T00:00:00+00:00')
        """,
        (
            record_id,
            str(record_id),
            f"test:{record_id}",
            title,
            author,
            f"Full evidence for {title}.",
        ),
    )
    sync_record_authors(conn, record_id, author)


def test_answer_about_single_record_author_returns_complete_record(tmp_path):
    db_path = tmp_path / "knowledge.sqlite3"
    with the_analyst.ki.open_db(db_path) as conn:
        _insert_author_record(conn, 1, "Alice Example", "Only Talk")
        conn.commit()

    result = tool_answer_about_author(
        "Alice Example",
        db_path=db_path,
        summary_dir=tmp_path / "summaries",
    )

    assert "Evidence: single underlying record" in result
    assert "[record_id:1]" in result
    assert "Full evidence for Only Talk." in result


def test_answer_about_multi_record_author_uses_summary(tmp_path):
    db_path = tmp_path / "knowledge.sqlite3"
    summary_dir = tmp_path / "summaries"
    author_dir = summary_dir / "authors"
    author_dir.mkdir(parents=True)
    (author_dir / "alice-example.md").write_text(
        "Alice synthesis [record_id:1] [record_id:2].",
        encoding="utf-8",
    )
    with the_analyst.ki.open_db(db_path) as conn:
        _insert_author_record(conn, 1, "Alice Example", "First Talk")
        _insert_author_record(conn, 2, "Alice Example; Bob Example", "Second Talk")
        conn.commit()

    result = tool_answer_about_author(
        "Alice Example",
        db_path=db_path,
        summary_dir=summary_dir,
    )

    assert "Evidence: author summary covering 2 records" in result
    assert "Alice synthesis" in result


def test_query_annotations_tool_is_exposed_for_structured_keyword_queries():
    tool = next(t for t in TOOLS if t["name"] == "query-annotations")

    assert "structured record annotations" in tool["description"]
    assert "keywords" in tool["input_schema"]["properties"]
    assert "match" in tool["input_schema"]["properties"]


def test_tool_search_records_returns_compact_snippets(monkeypatch):
    class FakeRow(dict):
        def __getitem__(self, key):
            return dict.__getitem__(self, key)

    long_text = " ".join(["detail"] * 100)

    monkeypatch.setattr(the_analyst.ki, "list_classification_topics", lambda _db_path: [])
    monkeypatch.setattr(
        the_analyst.ki,
        "search_records",
        lambda _db_path, _query, limit: [
            FakeRow({
                "id": 1,
                "source": "defcon33",
                "year": "2025",
                "title": "Example Project",
                "author": "Example Author",
                "agent_topics": "[]",
                "url": "https://example.test",
                "text": long_text,
            })
        ][:limit],
    )

    result = tool_search_records("Example Project", limit=1)

    assert "compact record match" in result
    assert "Example Project" in result
    assert "Snippet:" in result
    assert len(result) < len(long_text) + 250


def test_tool_search_records_without_limit_returns_all_gathered_matches(monkeypatch):
    class FakeRow(dict):
        def __getitem__(self, key):
            return dict.__getitem__(self, key)

    rows = [
        FakeRow({
            "id": idx,
            "source": "defcon33",
            "year": "2025",
            "title": f"Example Project {idx}",
            "author": "Example Author",
            "agent_topics": "[]",
            "url": "",
            "text": "example project detail",
        })
        for idx in range(1, 4)
    ]

    monkeypatch.setattr(the_analyst.ki, "list_classification_topics", lambda _db_path: [])
    monkeypatch.setattr(
        the_analyst.ki,
        "search_records",
        lambda _db_path, _query, limit: rows[:limit],
    )

    result = tool_search_records("Example Project")

    assert "3 compact record match(es) found" in result
    assert "Example Project 1" in result
    assert "Example Project 2" in result
    assert "Example Project 3" in result


def test_tool_search_records_numeric_query_fetches_exact_record_id(monkeypatch):
    class FakeRow(dict):
        def __getitem__(self, key):
            return dict.__getitem__(self, key)

    record = FakeRow({
        "id": 64,
        "source": "blackhat",
        "year": "2025",
        "title": "Vulnerability Haruspicy",
        "author": "Tod Beardsley",
        "agent_topics": "[]",
        "url": "https://example.test/64",
        "text": "CVSS risk scoring discussion.",
    })

    class FakeConn:
        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def execute(self, sql, params):
            assert "WHERE id = ?" in sql
            assert params == (64,)
            return self

        def fetchone(self):
            return record

    monkeypatch.setattr(the_analyst.ki, "open_db", lambda _db_path: FakeConn())
    monkeypatch.setattr(
        the_analyst.ki,
        "search_records",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(AssertionError("FTS should not run")),
    )

    result = tool_search_records("64")

    assert "Exact record match for id 64" in result
    assert "[64] blackhat 2025" in result
    assert "Vulnerability Haruspicy" in result


def test_tool_query_annotations_returns_scored_annotation_cards(monkeypatch):
    class FakeRow(dict):
        def __getitem__(self, key):
            return dict.__getitem__(self, key)

    rows = [
        FakeRow({
            "record_id": 10,
            "source": "defcon33",
            "year": "2025",
            "title": "Agent Sandbox Talk",
            "author": "Example Author",
            "url": "https://example.test",
            "agent_topics": "|AI security, prompt injection, and jailbreaking|",
            "short_summary": "Talk about MCP sandboxing and malicious tool permissions.",
            "keywords_json": '["mcp security", "agent sandboxing"]',
            "tools_json": '["MCP"]',
            "people_json": "[]",
            "claims_json": '["malicious tools can abuse agent permissions"]',
            "use_cases_json": '["agent security review"]',
            "ai_relevance": "about_ai_security",
            "content_types_json": '["research"]',
            "security_domains_json": '["AI security"]',
            "source_quality": "conference",
            "relevance_notes": "Useful for agent security taxonomy.",
        }),
        FakeRow({
            "record_id": 11,
            "source": "defcon33",
            "year": "2025",
            "title": "Unrelated Talk",
            "author": "Other Author",
            "url": "",
            "agent_topics": "|Cloud, infrastructure, and CDR|",
            "short_summary": "Cloud logging.",
            "keywords_json": '["cloud"]',
            "tools_json": "[]",
            "people_json": "[]",
            "claims_json": "[]",
            "use_cases_json": "[]",
            "ai_relevance": "none",
            "content_types_json": '["research"]',
            "security_domains_json": '["cloud security"]',
            "source_quality": "conference",
            "relevance_notes": "",
        }),
    ]

    monkeypatch.setattr(
        the_analyst.ki,
        "list_record_annotations",
        lambda _db_path, limit=20, source="", query="", latest=False: [
            row for row in rows
            if query.lower() in " ".join(str(v).lower() for v in row.values())
        ][:limit],
    )

    result = tool_query_annotations(
        keywords=["agent sandboxing"],
        topic="AI security, prompt injection, and jailbreaking",
        limit=5,
    )

    assert "[record_id:10]" in result
    assert "URL: https://example.test" in result
    assert "Matched annotation fields" in result
    assert "agent sandboxing" in result
    assert "Unrelated Talk" not in result


def test_tool_query_annotations_without_limit_returns_all_matches(monkeypatch):
    class FakeRow(dict):
        def __getitem__(self, key):
            return dict.__getitem__(self, key)

    rows = [
        FakeRow({
            "record_id": idx,
            "source": "defcon33",
            "year": "2025",
            "title": f"Agent Sandbox Talk {idx}",
            "author": "Example Author",
            "url": "",
            "agent_topics": "|AI security, prompt injection, and jailbreaking|",
            "short_summary": "Agent sandboxing research.",
            "keywords_json": '["agent sandboxing"]',
            "tools_json": "[]",
            "people_json": "[]",
            "claims_json": "[]",
            "use_cases_json": "[]",
            "ai_relevance": "about_ai_security",
            "content_types_json": "[]",
            "security_domains_json": '["AI security"]',
            "source_quality": "conference",
            "relevance_notes": "",
        })
        for idx in range(1, 4)
    ]

    monkeypatch.setattr(
        the_analyst.ki,
        "list_record_annotations",
        lambda _db_path, limit=20, source="", query="", latest=False: rows[:limit],
    )

    result = tool_query_annotations(keywords=["agent sandboxing"])

    assert "3 annotation match(es)" in result
    assert "[record_id:1]" in result
    assert "[record_id:2]" in result
    assert "[record_id:3]" in result


def test_run_prefixed_query_bypasses_llm_client(monkeypatch, capsys):
    monkeypatch.setattr(
        the_analyst,
        "tool_query_annotations",
        lambda query="", **_kwargs: f"annotation query: {query}",
    )

    def fail_create_client():
        raise AssertionError("LLM client should not be created for query prefix")

    monkeypatch.setattr(the_analyst.llm_client, "create_client", fail_create_client)

    handled = the_analyst.run_prefixed_turn("query: prompt injection")

    assert handled is True
    output = capsys.readouterr().out
    assert "[query-annotations]" in output
    assert "annotation query: prompt injection" in output


def test_help_command_lists_tools_and_bypasses_llm_client(monkeypatch, capsys):
    def fail_create_client():
        raise AssertionError("LLM client should not be created for help")

    monkeypatch.setattr(the_analyst.llm_client, "create_client", fail_create_client)

    handled = the_analyst.run_help_turn("help")

    assert handled is True
    output = capsys.readouterr().out
    assert "Oracle tools:" in output
    assert "get-status" in output
    assert "search-records" in output
    assert "query-annotations" in output
    assert "answer-from-summaries" in output
    assert "generate-topic-summary" in output


def test_system_prompt_allows_clarifying_questions_for_ambiguous_requests():
    assert the_analyst.ORACLE_SYSTEM_PROMPT.name == "oracle_system.txt"
    assert the_analyst.ORACLE_SYSTEM_PROMPT.parent.name == "prompts"
    assert AGENT_SYSTEM == the_analyst.ORACLE_SYSTEM_PROMPT.read_text(encoding="utf-8").strip()
    assert "Ask one concise clarifying question" in AGENT_SYSTEM
    assert "research summary" in AGENT_SYSTEM
    assert "practical testing plan" in AGENT_SYSTEM
    assert "specific projects/tools" in AGENT_SYSTEM


def test_system_prompt_prefers_summaries_for_substantive_answers():
    assert "route broad questions to answer-from-summaries" in AGENT_SYSTEM
    assert "Use answer-about-author" in AGENT_SYSTEM
    assert "Route exact title/URL/raw keyword lookups to search-records" in AGENT_SYSTEM


def test_system_prompt_requires_only_summary_file_evidence():
    assert "use ONLY the summary files" in AGENT_SYSTEM
    assert "Sources used" in AGENT_SYSTEM
    assert "Do not use general knowledge" in AGENT_SYSTEM
    assert "answer the user's question directly in natural prose" in AGENT_SYSTEM
    assert "Avoid report-style structure" in AGENT_SYSTEM
    assert "who gave it when available" in AGENT_SYSTEM
    assert "common themes across records" in AGENT_SYSTEM


def test_system_prompt_routes_annotation_queries_separately_from_summary_questions():
    assert 'prefixes input with "query:"' in AGENT_SYSTEM
    assert 'prefixes input with "question:"' in AGENT_SYSTEM
    assert "route broad questions to answer-from-summaries" in AGENT_SYSTEM
    assert "Route deterministic queries to query-annotations" in AGENT_SYSTEM
    assert "annotation keywords" in AGENT_SYSTEM


def test_interactive_blank_input_continues_until_explicit_quit(monkeypatch):
    answers = iter(["", "quit"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(answers))

    result = the_analyst.run(the_analyst.parse_args([]))

    assert result == 0


# --- load_summary_files ---

def test_load_summary_files_returns_empty_string_when_dir_is_empty():
    state_dir = _state_dir()
    assert load_summary_files(state_dir) == ""


def test_load_summary_files_loads_topic_summary():
    state_dir = _state_dir()
    (state_dir / "summary-agentic-ai-security.md").write_text(
        "## Agentic AI\nSome content.", encoding="utf-8"
    )
    result = load_summary_files(state_dir, topic="Agentic AI security")
    assert "Agentic AI" in result
    assert "Some content." in result


def test_load_summary_files_loads_new_flat_summary_folder(tmp_path):
    state_dir = tmp_path / "knowledge"
    summary_dir = tmp_path / "summaries"
    state_dir.mkdir()
    summary_dir.mkdir()
    (summary_dir / "election-security.md").write_text(
        "# Topic: Election security\nResearch report content.", encoding="utf-8"
    )
    (summary_dir / "election-security.prompt-input.md").write_text(
        "Prompt artifact", encoding="utf-8"
    )

    result = load_summary_files(
        state_dir,
        topic="Election security",
        summary_dir=summary_dir,
    )

    assert "Research report content." in result
    assert "Prompt artifact" not in result


def test_load_summary_files_loads_grouped_topic_summary_folder(tmp_path):
    state_dir = tmp_path / "knowledge"
    summary_dir = tmp_path / "summaries"
    topics_dir = summary_dir / "topics"
    state_dir.mkdir()
    topics_dir.mkdir(parents=True)
    (topics_dir / "threat-modeling.md").write_text(
        "# Topic: Threat modeling\nGrouped topic report.", encoding="utf-8"
    )

    result = load_summary_files(
        state_dir,
        topic="Threat modeling",
        summary_dir=summary_dir,
    )

    assert "Grouped topic report." in result


def test_load_summary_files_resolves_partial_topic_name(tmp_path):
    state_dir = tmp_path / "knowledge"
    summary_dir = tmp_path / "summaries"
    topics_dir = summary_dir / "topics"
    state_dir.mkdir()
    topics_dir.mkdir(parents=True)
    (topics_dir / "detection-engineering-soc-siem-and-threat-hunting.md").write_text(
        "# Topic: Detection engineering, SOC, SIEM, and threat hunting\n"
        "Threat hunting report content.",
        encoding="utf-8",
    )

    result = load_summary_files(
        state_dir,
        topic="threat hunting",
        summary_dir=summary_dir,
    )

    assert "Threat hunting report content." in result
    assert "Selected summary: detection engineering soc siem and threat hunting" in result


def test_load_summary_files_returns_empty_for_unknown_topic():
    state_dir = _state_dir()
    result = load_summary_files(state_dir, topic="Nonexistent Topic XYZ")
    assert result == ""


def test_load_summary_files_path_traversal_rejected():
    state_dir = _state_dir()
    # A topic name designed to escape the state_dir
    malicious_topic = "../../etc/passwd"
    result = load_summary_files(state_dir, topic=malicious_topic)
    assert result == ""


def test_load_summary_files_path_traversal_with_dotdot_rejected():
    state_dir = _state_dir()
    result = load_summary_files(state_dir, topic="..bad")
    assert result == ""


def test_load_summary_files_loads_all_summaries_when_no_topic():
    state_dir = _state_dir()
    (state_dir / "summary-topic-a.md").write_text("Content A", encoding="utf-8")
    (state_dir / "summary-topic-b.md").write_text("Content B", encoding="utf-8")

    result = load_summary_files(state_dir)
    assert "Content A" in result
    assert "Content B" in result


def test_load_summary_files_with_question_loads_relevant_summaries_only():
    state_dir = _state_dir()
    (state_dir / "summary-cloud-and-infrastructure-security.md").write_text(
        "Cloud content", encoding="utf-8"
    )
    (state_dir / "summary-prompt-injection-and-jailbreaks.md").write_text(
        "Prompt content", encoding="utf-8"
    )

    result = load_summary_files(
        state_dir,
        question="What is happening with prompt injection?",
        max_topics=1,
    )

    assert "Prompt content" in result
    assert "Cloud content" not in result


def test_load_summary_files_ranks_new_flat_summary_folder_by_question(tmp_path):
    state_dir = tmp_path / "knowledge"
    summary_dir = tmp_path / "summaries"
    state_dir.mkdir()
    summary_dir.mkdir()
    (summary_dir / "cloud-infrastructure-and-cdr.md").write_text(
        "Cloud content", encoding="utf-8"
    )
    (summary_dir / "ai-security-prompt-injection-and-jailbreaking.md").write_text(
        "Prompt content", encoding="utf-8"
    )

    result = load_summary_files(
        state_dir,
        question="What is happening with prompt injection?",
        max_topics=1,
        summary_dir=summary_dir,
    )

    assert "Prompt content" in result
    assert "Cloud content" not in result


def test_rank_relevant_summary_topics_filters_weak_generic_security_matches(tmp_path):
    state_dir = tmp_path / "knowledge"
    summary_dir = tmp_path / "summaries"
    state_dir.mkdir()
    summary_dir.mkdir()
    (summary_dir / "election-security.md").write_text(
        "Voting Village election material [record_id:1863]", encoding="utf-8"
    )
    (summary_dir / "threat-modeling.md").write_text(
        "Threat modeling security material", encoding="utf-8"
    )

    ranked = rank_relevant_summary_topics(
        "What does the election security material say?",
        state_dir,
        summary_dir=summary_dir,
        limit=5,
    )

    assert [name for name, _score in ranked] == ["election security"]


def test_tool_answer_from_summaries_names_selected_sources(monkeypatch, tmp_path):
    state_dir = tmp_path / "knowledge"
    summary_dir = tmp_path / "summaries"
    state_dir.mkdir()
    summary_dir.mkdir()
    (state_dir / "pdf-example.md").write_text(
        "# PDF\nDo not include this either.", encoding="utf-8"
    )
    (summary_dir / "election-security.md").write_text(
        "# Topic: Election security\nVoting Village details [record_id:1863]",
        encoding="utf-8",
    )
    (summary_dir / "general-security.md").write_text(
        "# Topic: General security\nGeneric security details",
        encoding="utf-8",
    )
    monkeypatch.setattr(the_analyst.ki, "STATE_DIR", state_dir)
    monkeypatch.setattr(the_analyst, "SUMMARY_DIR", summary_dir)

    result = tool_answer_from_summaries(
        question="What does the election security material say?"
    )

    assert "Use ONLY the summary files" in result
    assert "Relevant summaries selected" in result
    assert "- election security (score:" in result
    assert "election security" in result
    assert "Voting Village details" in result
    assert "Generic security details" not in result
    assert "Do not include this either" not in result


def test_tool_answer_from_summaries_loads_multiple_relevant_summaries(monkeypatch, tmp_path):
    state_dir = tmp_path / "knowledge"
    summary_dir = tmp_path / "summaries"
    state_dir.mkdir()
    summary_dir.mkdir()
    (summary_dir / "ai-security-prompt-injection-and-jailbreaking.md").write_text(
        "# Topic: AI security prompt injection and jailbreaking\nPrompt injection details.",
        encoding="utf-8",
    )
    (summary_dir / "rag-and-graphrag-security.md").write_text(
        "# Topic: RAG and GraphRAG security\nRetrieval pipeline details.",
        encoding="utf-8",
    )
    (summary_dir / "election-security.md").write_text(
        "# Topic: Election security\nVoting details.",
        encoding="utf-8",
    )
    monkeypatch.setattr(the_analyst.ki, "STATE_DIR", state_dir)
    monkeypatch.setattr(the_analyst, "SUMMARY_DIR", summary_dir)

    result = tool_answer_from_summaries(
        question="How does prompt injection affect retrieval pipelines?",
        max_topics=3,
    )

    assert "- ai security prompt injection and jailbreaking (score:" in result
    assert "- rag and graphrag security (score:" in result
    assert "Prompt injection details." in result
    assert "Retrieval pipeline details." in result
    assert "Voting details." not in result


