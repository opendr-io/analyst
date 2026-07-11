from pathlib import Path
import sqlite3
from uuid import uuid4

import json
import pytest

from knowledge_indexing.knowledge_index import (
    _validate_ident,
    decode_topics,
    discover_topic_candidates,
    export_topic_keyword_candidates,
    export_topic_list,
    import_exports,
    list_classification_topics,
    list_record_annotations,
    list_record_annotation_errors,
    list_record_classifications,
    list_record_classification_errors,
    list_unread_records,
    mark_records_read,
    open_db,
    refresh_topic_catalog,
    search_records,
    seed_topics,
    set_record_topics,
    get_record_annotation_map,
    list_records_missing_annotations,
    list_records_missing_classifications,
    clear_record_annotation_error,
    clear_record_classification_error,
    store_record_annotation,
    store_record_annotation_error,
    store_record_classification,
    store_record_classification_error,
    store_topic_candidates,
    sync_linkedin_db,
    phrase_candidates,
    records_from_youtube_playlist,
    records_from_bsideslv,
)


def local_tmp_dir() -> Path:
    path = Path("data") / "test-tmp" / f"knowledge-{uuid4().hex}"
    path.mkdir(parents=True, exist_ok=True)
    return path


def test_records_from_bsideslv_export_uses_bsideslv_source():
    records = records_from_bsideslv(
        {
            "talks": [
                {
                    "event": "BSidesLV 2025",
                    "year": 2025,
                    "session_id": "HUP7L3",
                    "title": "OAuth Token Replay Attacks",
                    "speakers": "Darryl G. Baker",
                    "abstract": "A technical session about OAuth and OIDC token replay attacks.",
                    "url": "https://archive.bsideslv.org/2025/talks#oauth",
                    "track": "Ground Floor",
                    "room": "Florentine E",
                    "date": "Monday",
                    "time": "18:00-18:45",
                }
            ]
        },
        Path("bsideslv-talks.json"),
    )

    assert len(records) == 1
    record = records[0]
    assert record.source == "bsideslv"
    assert record.source_record_id == "HUP7L3"
    assert record.dedupe_key == "bsideslv:id:HUP7L3"
    assert record.event == "BSidesLV 2025"
    assert "Florentine E" in record.tags

def test_import_exports_normalizes_and_searches_sources():
    test_dir = local_tmp_dir()
    blackhat = test_dir / "blackhat-talks.json"
    camlis = test_dir / "camlis-talks.json"
    linkedin = test_dir / "linkedin-saved.json"

    blackhat.write_text(
        """
        {
          "talks": [
            {
              "session_id": "1",
              "title": "OAuth Risks in Agentic AI",
              "speakers": "Speaker: Researcher One (Head of Research (AI), Example Corp)",
              "abstract": "Connection-based OAuth can create confused deputy risk.",
              "url": "https://blackhat.example/talk-1",
              "event": "US",
              "year": 2025,
              "track": "Application Security",
              "listing_text": "Briefings"
            }
          ]
        }
        """,
        encoding="utf-8",
    )
    camlis.write_text(
        """
        {
          "talks": [
            {
              "year": 2025,
              "speaker": "Speaker Two",
              "title": "Privacy for Agents",
              "abstract": "Agentic systems create new data sinks.",
              "url": "https://camlis.example/talk-1",
              "section": "DAY-1"
            }
          ]
        }
        """,
        encoding="utf-8",
    )
    linkedin.write_text(
        """
        {
          "config": {"source": "saved"},
          "ingested_at": "2026-05-15T18:46:55+00:00",
          "posts": [
            {
              "source": "saved",
              "author": "Poster One",
              "text": "A saved post about threat modeling AI systems.",
              "url": "https://www.linkedin.com/feed/update/1"
            }
          ]
        }
        """,
        encoding="utf-8",
    )
    db_path = test_dir / f"knowledge-{uuid4().hex}.sqlite3"

    stats = import_exports([blackhat, camlis, linkedin], db_path=db_path)
    rows = search_records(db_path, "agentic", limit=10)

    assert stats["inserted"] == 3
    assert stats["updated"] == 0
    assert stats.get("errors", 0) == 0
    assert {row["source"] for row in rows} == {"blackhat", "camlis"}
    with open_db(db_path) as conn:
        count = conn.execute("SELECT COUNT(*) FROM records").fetchone()[0]
        unread = conn.execute("SELECT COUNT(*) FROM records WHERE agent_read = 0").fetchone()[0]
        blackhat_author = conn.execute(
            "SELECT author FROM records WHERE source = 'blackhat'"
        ).fetchone()[0]
    assert count == 3
    assert unread == 3
    assert blackhat_author == "Researcher One"


def test_record_annotations_store_and_filter_missing_records():
    test_dir = local_tmp_dir()
    db_path = test_dir / "knowledge.sqlite3"
    export_path = test_dir / "blackhat-talks.json"
    export_path.write_text(
        json.dumps({
            "talks": [
                {
                    "session_id": "1",
                    "title": "OAuth Testing",
                    "speakers": "Researcher One",
                    "abstract": "Testing authentication and authorization controls.",
                    "url": "https://example.test/1",
                    "year": 2026,
                },
                {
                    "session_id": "2",
                    "title": "Prompt Injection",
                    "speakers": "Researcher Two",
                    "abstract": "Testing prompt injection controls.",
                    "url": "https://example.test/2",
                    "year": 2026,
                },
            ]
        }),
        encoding="utf-8",
    )
    import_exports([export_path], db_path=db_path)

    missing = list_records_missing_annotations(db_path, limit=10)
    assert len(missing) == 2

    store_record_annotation(
        db_path,
        record_id=missing[0]["id"],
        short_summary="Authentication testing record.",
        keywords=["authentication", "authorization"],
        tools=["ExampleTool"],
        people=["Researcher One"],
        claims=["Auth testing can be automated."],
        use_cases=["application audit"],
        ai_relevance="none",
        content_types=["research"],
        security_domains=["application security", "identity security"],
        contains_prompt_injection=True,
        relevance_notes="Substantive authentication testing record.",
        raw={"id": missing[0]["id"]},
        model="test-model",
        schema_version=2,
    )

    annotations = get_record_annotation_map(db_path, [missing[0]["id"], missing[1]["id"]])
    assert missing[0]["id"] in annotations
    assert annotations[missing[0]["id"]]["short_summary"] == "Authentication testing record."
    assert annotations[missing[0]["id"]]["ai_relevance"] == "none"
    assert json.loads(annotations[missing[0]["id"]]["content_types_json"]) == ["research"]
    assert "identity security" in json.loads(annotations[missing[0]["id"]]["security_domains_json"])
    assert annotations[missing[0]["id"]]["contains_prompt_injection"] == 1
    assert annotations[missing[0]["id"]]["relevance_notes"] == "Substantive authentication testing record."
    assert len(list_records_missing_annotations(db_path, limit=10)) == 1

    listed = list_record_annotations(db_path, limit=10, query="identity security")
    assert len(listed) == 1
    assert listed[0]["record_id"] == missing[0]["id"]
    assert listed[0]["short_summary"] == "Authentication testing record."
    assert listed[0]["schema_version"] == 2


def test_record_annotation_errors_are_durable_and_clearable():
    test_dir = local_tmp_dir()
    db_path = test_dir / "knowledge.sqlite3"
    export_path = test_dir / "blackhat-talks.json"
    export_path.write_text(
        json.dumps({
            "talks": [
                {
                    "session_id": "1",
                    "title": "OAuth Testing",
                    "speakers": "Researcher One",
                    "abstract": "Testing authentication and authorization controls.",
                    "url": "https://example.test/1",
                    "year": 2026,
                }
            ]
        }),
        encoding="utf-8",
    )
    import_exports([export_path], db_path=db_path)
    record_id = list_records_missing_annotations(db_path, limit=1)[0]["id"]

    store_record_annotation_error(
        db_path,
        record_id=record_id,
        model="test-model",
        error_type="PermissionDeniedError",
        error_message="first failure",
    )
    store_record_annotation_error(
        db_path,
        record_id=record_id,
        model="test-model",
        error_type="PermissionDeniedError",
        error_message="second failure",
    )

    errors = list_record_annotation_errors(db_path, limit=10)
    assert len(errors) == 1
    assert errors[0]["record_id"] == record_id
    assert errors[0]["attempts"] == 2
    assert errors[0]["error_message"] == "second failure"

    clear_record_annotation_error(db_path, record_id)

    assert list_record_annotation_errors(db_path, limit=10) == []


def test_record_classifications_and_errors_are_listable():
    test_dir = local_tmp_dir()
    db_path = test_dir / "knowledge.sqlite3"
    export_path = test_dir / "blackhat-talks.json"
    export_path.write_text(
        json.dumps({
            "talks": [
                {
                    "session_id": "1",
                    "title": "OAuth Testing",
                    "speakers": "Researcher One",
                    "abstract": "Testing authentication and authorization controls.",
                    "url": "https://example.test/1",
                    "year": 2026,
                }
            ]
        }),
        encoding="utf-8",
    )
    import_exports([export_path], db_path=db_path)
    record_id = list_unread_records(db_path, limit=1)[0]["id"]

    store_record_classification(
        db_path,
        record_id=record_id,
        primary_topic="Unclassified",
        secondary_topics=[],
        confidence="low",
        rationale="No curated topic fits.",
        new_topic_candidate="Authentication testing operations",
        model="test-model",
        schema_version=2,
    )

    low = list_record_classifications(db_path, limit=10, low_confidence=True)
    candidates = list_record_classifications(db_path, limit=10, new_topic_candidates=True)
    assert len(low) == 1
    assert low[0]["record_id"] == record_id
    assert len(candidates) == 1
    assert candidates[0]["new_topic_candidate"] == "Authentication testing operations"

    store_record_classification_error(
        db_path,
        record_id=record_id,
        model="test-model",
        error_type="PermissionDeniedError",
        error_message="first failure",
    )
    store_record_classification_error(
        db_path,
        record_id=record_id,
        model="test-model",
        error_type="PermissionDeniedError",
        error_message="second failure",
    )

    errors = list_record_classification_errors(db_path, limit=10)
    assert len(errors) == 1
    assert errors[0]["attempts"] == 2
    assert errors[0]["error_message"] == "second failure"

    clear_record_classification_error(db_path, record_id)

    assert list_record_classification_errors(db_path, limit=10) == []


def test_records_missing_classifications_ignores_legacy_read_state():
    test_dir = local_tmp_dir()
    db_path = test_dir / "knowledge.sqlite3"
    export_path = test_dir / "blackhat-talks.json"
    export_path.write_text(
        json.dumps({
            "talks": [
                {
                    "session_id": "1",
                    "title": "Already Read But Not Classified",
                    "speakers": "Researcher One",
                    "abstract": "Testing classification selection.",
                    "url": "https://example.test/1",
                    "year": 2026,
                }
            ]
        }),
        encoding="utf-8",
    )
    import_exports([export_path], db_path=db_path)
    record_id = list_unread_records(db_path, limit=1)[0]["id"]
    mark_records_read(db_path, [record_id], reader="legacy")
    store_record_annotation(
        db_path,
        record_id=record_id,
        short_summary="Annotated but not classified.",
    )

    missing = list_records_missing_classifications(db_path, limit=10)

    assert [row["id"] for row in missing] == [record_id]
    store_record_classification(
        db_path,
        record_id=record_id,
        primary_topic="Application security",
        confidence="high",
    )
    assert list_records_missing_classifications(db_path, limit=10) == []


def test_import_exports_dedupes_by_normalized_url():
    test_dir = local_tmp_dir()
    export = test_dir / "blackhat-talks.json"
    export.write_text(
        """
        {
          "talks": [
            {
              "session_id": "1",
              "title": "First Title",
              "speakers": "A",
              "abstract": "First body",
              "url": "https://blackhat.example/talk?tracking=1"
            }
          ]
        }
        """,
        encoding="utf-8",
    )
    db_path = test_dir / f"knowledge-{uuid4().hex}.sqlite3"

    first = import_exports([export], db_path=db_path)
    second = import_exports([export], db_path=db_path)

    assert first["inserted"] == 1
    assert second["inserted"] == 0
    assert second["updated"] == 1


def test_import_exports_preserves_blackhat_hash_urls_as_distinct_records():
    test_dir = local_tmp_dir()
    export = test_dir / "blackhat-talks.json"
    export.write_text(
        """
        {
          "talks": [
            {
              "session_id": "1",
              "title": "First Title",
              "speakers": "A",
              "abstract": "First body",
              "url": "https://blackhat.example/schedule/#first-1"
            },
            {
              "session_id": "2",
              "title": "Second Title",
              "speakers": "B",
              "abstract": "Second body",
              "url": "https://blackhat.example/schedule/#second-2"
            }
          ]
        }
        """,
        encoding="utf-8",
    )
    db_path = test_dir / f"knowledge-{uuid4().hex}.sqlite3"

    stats = import_exports([export], db_path=db_path)

    assert stats["inserted"] == 2


def test_import_exports_preserves_camlis_shared_detail_url_records():
    test_dir = local_tmp_dir()
    export = test_dir / "camlis-talks.json"
    export.write_text(
        """
        {
          "talks": [
            {
              "year": 2025,
              "speaker": "Speaker A",
              "title": "First Shared Page Talk",
              "abstract": "First body",
              "url": "https://camlis.example/shared"
            },
            {
              "year": 2025,
              "speaker": "Speaker B",
              "title": "Second Shared Page Talk",
              "abstract": "Second body",
              "url": "https://camlis.example/shared"
            }
          ]
        }
        """,
        encoding="utf-8",
    )
    db_path = test_dir / f"knowledge-{uuid4().hex}.sqlite3"

    stats = import_exports([export], db_path=db_path)

    assert stats["inserted"] == 2


def test_defcon_youtube_playlist_skips_live_music_records():
    records = records_from_youtube_playlist(
        {
            "playlist": "DEF CON 33",
            "records": [
                {
                    "id": "music-1",
                    "talk_title": "Live Music - Saturday Night",
                    "speakers": "DJ null",
                    "abstract": "Live Set from DJ null, Saturday Night at the LVCC.",
                    "url": "https://example.test/music",
                    "upload_date": "2025-08-01",
                },
                {
                    "id": "talk-1",
                    "talk_title": "Prompt Injection Research",
                    "speakers": "Researcher One",
                    "abstract": "A substantive security talk about prompt injection attacks and mitigations.",
                    "url": "https://example.test/talk",
                    "upload_date": "2025-08-01",
                },
            ],
        },
        Path("defcon33_latest.json"),
    )

    assert len(records) == 1
    assert records[0].source_record_id == "talk-1"
    assert records[0].title == "Prompt Injection Research"


def test_generic_youtube_playlist_dedupes_by_video_id():
    records = records_from_youtube_playlist(
        {
            "playlist": "[un]prompted 2026",
            "records": [
                {
                    "id": "video-one",
                    "talk_title": "First Talk",
                    "speakers": "Speaker One",
                    "abstract": "A substantive talk about security research and AI systems.",
                    "url": "https://www.youtube.com/watch?v=video-one",
                    "upload_date": "2026-06-01",
                },
                {
                    "id": "video-two",
                    "talk_title": "Second Talk",
                    "speakers": "Speaker Two",
                    "abstract": "Another substantive talk about security research and AI systems.",
                    "url": "https://www.youtube.com/watch?v=video-two",
                    "upload_date": "2026-06-02",
                },
            ],
        },
        Path("unprompted2026_latest.json"),
    )

    assert len(records) == 2
    assert [record.dedupe_key for record in records] == [
        "unprompted2026:id:video-one",
        "unprompted2026:id:video-two",
    ]


def test_defcon_video_team_segment_is_not_treated_as_an_author():
    records = records_from_youtube_playlist(
        {
            "playlist": "DEF CON 33",
            "records": [
                {
                    "id": "video-one",
                    "title": "DEF CON 33 Video Team - AIxCC with ShellPhish",
                    "talk_title": "DEFCON 33 Video Team",
                    "speakers": "AIxCC with ShellPhish",
                    "abstract": "Silk interviews members of ShellPhish about the DARPA contest.",
                    "url": "https://www.youtube.com/watch?v=video-one",
                    "upload_date": "2025-08-18",
                }
            ],
        },
        Path("defcon33_latest.json"),
    )

    assert records[0].title == "AIxCC with ShellPhish"
    assert records[0].author == ""


def test_defcon_generic_panel_is_not_treated_as_an_author():
    records = records_from_youtube_playlist(
        {
            "playlist": "DEF CON 33",
            "records": [
                {
                    "id": "video-one",
                    "talk_title": "Cyber Game Changers",
                    "speakers": "Panel",
                    "abstract": "A substantive panel about women reshaping cybersecurity.",
                    "url": "https://www.youtube.com/watch?v=video-one",
                    "upload_date": "2025-10-22",
                }
            ],
        },
        Path("defcon33_latest.json"),
    )

    assert records[0].author == ""


def test_defcon_author_drops_erroneous_leading_year():
    records = records_from_youtube_playlist(
        {
            "playlist": "DEF CON 33",
            "records": [
                {
                    "id": "video-one",
                    "talk_title": "The Worst ICS/OT Love Story Ever Told",
                    "speakers": "2025 Mike Holcomb",
                    "abstract": "A substantive talk about changes in the industrial security threat landscape.",
                    "url": "https://www.youtube.com/watch?v=video-one",
                    "upload_date": "2025-10-10",
                }
            ],
        },
        Path("defcon33_latest.json"),
    )

    assert records[0].author == "Mike Holcomb"


def test_unprompted_playlist_recovers_author_and_title_from_full_video_title():
    records = records_from_youtube_playlist(
        {
            "playlist": "[un]prompted 2026",
            "records": [
                {
                    "id": "video-one",
                    "title": "Adam Krivka & Ondrej Vlcek - AI Found 12 Zero-Days in OpenSSL | [un]prompted 2026",
                    "talk_title": "Adam Krivka & Ondrej Vlcek",
                    "speakers": "AI Found 12 Zero-Days in OpenSSL | [un]prompted 2026",
                    "abstract": "A substantive talk about using AI to discover vulnerabilities in OpenSSL.",
                    "url": "https://www.youtube.com/watch?v=video-one",
                    "upload_date": "2026-06-01",
                }
            ],
        },
        Path("unprompted2026_latest.json"),
    )

    assert records[0].title == "AI Found 12 Zero-Days in OpenSSL"
    assert records[0].author == "Adam Krivka & Ondrej Vlcek"


def test_unprompted_playlist_allows_event_only_video_without_author():
    records = records_from_youtube_playlist(
        {
            "playlist": "[un]prompted 2026",
            "records": [
                {
                    "id": "video-one",
                    "title": "Flash Talks | [un]prompted 2026",
                    "talk_title": "Flash Talks | [un]prompted 2026",
                    "speakers": "",
                    "abstract": "A collection of substantive short talks about AI and security research.",
                    "url": "https://www.youtube.com/watch?v=video-one",
                    "upload_date": "2026-06-01",
                }
            ],
        },
        Path("unprompted2026_latest.json"),
    )

    assert records[0].title == "Flash Talks"
    assert records[0].author == ""


def test_discover_topic_candidates_finds_and_stores_recurring_phrases():
    test_dir = local_tmp_dir()
    export = test_dir / "blackhat-talks.json"
    export.write_text(
        """
        {
          "talks": [
            {
              "session_id": "1",
              "title": "Agentic AI OAuth Security",
              "speakers": "A",
              "abstract": "Agentic AI platforms need OAuth security controls.",
              "url": "https://blackhat.example/schedule/#one-1"
            },
            {
              "session_id": "2",
              "title": "Agentic AI Identity Controls",
              "speakers": "B",
              "abstract": "Agentic AI tools amplify identity and OAuth risk.",
              "url": "https://blackhat.example/schedule/#two-2"
            },
            {
              "session_id": "3",
              "title": "OAuth Token Abuse",
              "speakers": "C",
              "abstract": "OAuth security failures affect agentic AI integrations.",
              "url": "https://blackhat.example/schedule/#three-3"
            }
          ]
        }
        """,
        encoding="utf-8",
    )
    db_path = test_dir / f"knowledge-{uuid4().hex}.sqlite3"
    import_exports([export], db_path=db_path)

    candidates = discover_topic_candidates(db_path=db_path, limit=10, min_records=2)
    stats = store_topic_candidates(db_path, candidates)

    phrases = {candidate["phrase"] for candidate in candidates}
    assert "agentic ai" in phrases
    assert "oauth security" in phrases
    assert stats["added"] >= 2
    with open_db(db_path) as conn:
        stored = conn.execute("SELECT COUNT(*) FROM topic_candidates").fetchone()[0]
    assert stored >= 2


def test_seed_topics_stores_curated_starter_taxonomy():
    test_dir = local_tmp_dir()
    db_path = test_dir / f"knowledge-{uuid4().hex}.sqlite3"

    count = seed_topics(db_path)

    assert count >= 5
    with open_db(db_path) as conn:
        row = conn.execute(
            "SELECT query FROM topics WHERE name = 'AI security, prompt injection, and jailbreaking'"
        ).fetchone()
    assert "prompt injection" in row["query"]


def test_export_topic_list_writes_readable_text_file():
    test_dir = local_tmp_dir()
    db_path = test_dir / f"knowledge-{uuid4().hex}.sqlite3"
    out_path = test_dir / "topics.txt"
    seed_topics(db_path)

    result = export_topic_list(db_path, out_path)

    text = result.read_text(encoding="utf-8")
    assert "Curated Topics" in text
    assert "AI security, prompt injection, and jailbreaking" in text


def test_export_topic_keyword_candidates_uses_annotated_topic_records():
    test_dir = local_tmp_dir()
    db_path = test_dir / f"knowledge-{uuid4().hex}.sqlite3"
    export = test_dir / "blackhat-talks.json"
    export.write_text(
        json.dumps(
            {
                "talks": [
                    {
                        "session_id": str(i),
                        "title": f"Agent Harness {i}",
                        "speakers": "A",
                        "abstract": "Agent harness sandboxing for AI agents.",
                        "url": f"https://blackhat.example/{i}",
                    }
                    for i in range(2)
                ]
            }
        ),
        encoding="utf-8",
    )
    import_exports([export], db_path=db_path)
    seed_topics(db_path)
    with open_db(db_path) as conn:
        ids = [row["id"] for row in conn.execute("SELECT id FROM records ORDER BY id")]
    for record_id in ids:
        set_record_topics(db_path, record_id, ["AI security, prompt injection, and jailbreaking"])
        store_record_annotation(
            db_path,
            record_id=record_id,
            short_summary="Agent harness security.",
            keywords=["agent harness", "sandboxing"],
            tools=["MCP"],
            use_cases=["agent containment"],
        )

    out_path = test_dir / "topic-keywords.md"
    result = export_topic_keyword_candidates(db_path, out_path, min_records=2)

    text = result.read_text(encoding="utf-8")
    assert "## AI security, prompt injection, and jailbreaking" in text
    assert "- agent harness (2)" in text
    assert "- mcp (2)" in text
    assert "- agent containment (2)" in text


def test_refresh_topic_catalog_makes_candidates_available_to_classifier(tmp_path, monkeypatch):
    test_dir = local_tmp_dir()
    monkeypatch.setattr("knowledge_indexing.knowledge_index.LOG_PATH", tmp_path / "import.log")
    export = test_dir / "blackhat-talks.json"
    export.write_text(
        """
        {
          "talks": [
            {
              "session_id": "1",
              "title": "Browser Extension Supply Chain",
              "speakers": "A",
              "abstract": "Browser extension supply chain controls need review.",
              "url": "https://blackhat.example/schedule/#one-1"
            },
            {
              "session_id": "2",
              "title": "Browser Extension Permissions",
              "speakers": "B",
              "abstract": "Browser extension permissions expand supply chain risk.",
              "url": "https://blackhat.example/schedule/#two-2"
            }
          ]
        }
        """,
        encoding="utf-8",
    )
    db_path = test_dir / f"knowledge-{uuid4().hex}.sqlite3"
    topic_list_path = test_dir / "topic-list.txt"
    import_exports([export], db_path=db_path)

    stats = refresh_topic_catalog(
        db_path=db_path,
        candidate_limit=10,
        min_records=2,
        output_path=topic_list_path,
    )

    assert stats["seed_topics"] >= 5
    assert stats["candidate_topics"] >= 1
    assert topic_list_path.exists()
    topics = list_classification_topics(db_path=db_path, candidate_limit=10)
    assert "AI security, prompt injection, and jailbreaking" in topics
    assert "browser extension" in topics


def test_refresh_topic_catalog_can_skip_curated_topic_seed(tmp_path):
    db_path = tmp_path / "knowledge.sqlite3"
    topic_list_path = tmp_path / "topic-list.txt"

    stats = refresh_topic_catalog(
        db_path=db_path,
        candidate_limit=10,
        min_records=2,
        output_path=topic_list_path,
        seed_curated=False,
    )

    assert stats["seed_topics"] == 0
    assert topic_list_path.exists()
    with open_db(db_path) as conn:
        topic_count = conn.execute("SELECT COUNT(*) FROM topics").fetchone()[0]
    assert topic_count == 0


def test_list_classification_topics_includes_all_candidates_by_default(tmp_path):
    db_path = tmp_path / "knowledge.sqlite3"
    with open_db(db_path):
        pass
    seed_topics(db_path)
    store_topic_candidates(
        db_path,
        [
            {
                "phrase": f"candidate topic {idx}",
                "score": float(100 - idx),
                "record_count": 3,
                "sources": ["blackhat"],
                "sample_record_ids": [idx],
            }
            for idx in range(3)
        ],
    )

    all_topics = list_classification_topics(db_path)
    limited_topics = list_classification_topics(db_path, candidate_limit=1)

    assert "candidate topic 0" in all_topics
    assert "candidate topic 1" in all_topics
    assert "candidate topic 2" in all_topics
    assert "candidate topic 0" in limited_topics
    assert "candidate topic 1" not in limited_topics


def test_refresh_topic_catalog_keeps_source_specific_candidates(tmp_path, monkeypatch):
    test_dir = local_tmp_dir()
    monkeypatch.setattr("knowledge_indexing.knowledge_index.LOG_PATH", tmp_path / "import.log")
    dominant = test_dir / "blackhat-talks.json"
    niche = test_dir / "camlis-talks.json"
    dominant.write_text(
        json.dumps(
            {
                "talks": [
                    {
                        "session_id": str(i),
                        "title": f"Cloud Detection Pipeline {i}",
                        "speakers": "A",
                        "abstract": "Cloud detection pipeline telemetry automation incident response.",
                        "url": f"https://blackhat.example/schedule/#{i}",
                    }
                    for i in range(6)
                ]
            }
        ),
        encoding="utf-8",
    )
    niche.write_text(
        json.dumps(
            {
                "talks": [
                    {
                        "year": 2026,
                        "speaker": "B",
                        "title": f"Bio Signal Analysis {i}",
                        "abstract": "Bio signal analysis for specialized safety workflows.",
                        "url": f"https://camlis.example/{i}",
                    }
                    for i in range(2)
                ]
            }
        ),
        encoding="utf-8",
    )
    db_path = test_dir / f"knowledge-{uuid4().hex}.sqlite3"
    import_exports([dominant, niche], db_path=db_path)

    stats = refresh_topic_catalog(
        db_path=db_path,
        candidate_limit=1,
        min_records=2,
        source_candidate_limit=2,
        output_path=test_dir / "topic-list.txt",
    )

    assert stats["candidate_topics"] > 1
    with open_db(db_path) as conn:
        sources = {
            row["sources"]
            for row in conn.execute("SELECT sources FROM topic_candidates").fetchall()
        }
    assert "camlis" in sources


def test_phrase_candidates_filters_venue_and_event_names():
    phrases = phrase_candidates(
        "AMC at Metreon theater DEF CON Prompt GTFO prompt injection threat hunting"
    )

    assert "amc at" not in phrases
    assert "at metreon" not in phrases
    assert "def con" not in phrases
    assert "prompt gtfo" not in phrases
    assert "prompt injection" in phrases
    assert "threat hunting" in phrases


def test_phrase_candidates_filters_low_value_action_phrases():
    phrases = phrase_candidates(
        "look at here are how do join us its own your own deep dive whether re "
        "demonstrates how demonstrates hwo how he link comments he uses no longer "
        "see github April th PM video team are now discover how gain insights how ai how attackers threat intelligence"
    )

    for phrase in [
        "look at",
        "here are",
        "how do",
        "join us",
        "its own",
        "your own",
        "deep dive",
        "whether re",
        "demonstrates how",
        "demonstrates hwo",
        "how he",
        "link comments",
        "he uses",
        "no longer",
        "see github",
        "april th",
        "th pm",
        "video team",
        "are now",
        "discover how",
        "gain insights",
        "how ai",
        "how attackers",
    ]:
        assert phrase not in phrases
    assert "threat intelligence" in phrases


def test_store_topic_candidates_logs_added_topics(tmp_path, monkeypatch):
    db_path = tmp_path / "knowledge.sqlite3"
    log_path = tmp_path / "import.log"
    monkeypatch.setattr("knowledge_indexing.knowledge_db.LOG_PATH", log_path)

    stats = store_topic_candidates(
        db_path,
        [
            {
                "phrase": "browser extension",
                "score": 100.0,
                "record_count": 3,
                "sources": ["blackhat"],
                "sample_record_ids": [1, 2, 3],
            }
        ],
    )

    assert stats["added"] == 1
    text = log_path.read_text(encoding="utf-8")
    assert "candidate topics added: 1" in text
    assert "browser extension" in text


def test_mark_records_read_tracks_agent_state():
    test_dir = local_tmp_dir()
    export = test_dir / "blackhat-talks.json"
    export.write_text(
        """
        {
          "talks": [
            {
              "session_id": "1",
              "title": "First Topic",
              "speakers": "A",
              "abstract": "First body",
              "url": "https://blackhat.example/schedule/#one-1"
            },
            {
              "session_id": "2",
              "title": "Second Topic",
              "speakers": "B",
              "abstract": "Second body",
              "url": "https://blackhat.example/schedule/#two-2"
            }
          ]
        }
        """,
        encoding="utf-8",
    )
    db_path = test_dir / f"knowledge-{uuid4().hex}.sqlite3"
    import_exports([export], db_path=db_path)
    first_id = list_unread_records(db_path, limit=1)[0]["id"]

    assert mark_records_read(db_path, [first_id], reader="tester", notes="processed") == 1
    unread_ids = {row["id"] for row in list_unread_records(db_path, limit=10)}
    assert first_id not in unread_ids
    with open_db(db_path) as conn:
        row = conn.execute("SELECT agent_read, agent_reader, agent_notes FROM records WHERE id = ?", (first_id,)).fetchone()
    assert row["agent_read"] == 1
    assert row["agent_reader"] == "tester"
    assert row["agent_notes"] == "processed"

    assert mark_records_read(db_path, [first_id], read=False) == 1
    unread_ids = {row["id"] for row in list_unread_records(db_path, limit=10)}
    assert first_id in unread_ids


def test_sync_linkedin_db_imports_saved_posts_and_skips_unscreened_feed_posts():
    test_dir = local_tmp_dir()
    knowledge_db = test_dir / f"knowledge-{uuid4().hex}.sqlite3"
    linkedin_db = test_dir / "linkedin.sqlite3"
    with sqlite3.connect(linkedin_db) as conn:
        conn.executescript(
            """
            CREATE TABLE linkedin_posts (
                id INTEGER PRIMARY KEY,
                dedupe_key TEXT NOT NULL,
                identity_url TEXT NOT NULL DEFAULT '',
                source_first_seen TEXT NOT NULL,
                first_seen_at TEXT NOT NULL,
                last_seen_at TEXT NOT NULL,
                author TEXT NOT NULL DEFAULT '',
                headline TEXT NOT NULL DEFAULT '',
                text TEXT NOT NULL DEFAULT '',
                url TEXT NOT NULL DEFAULT '',
                time_text TEXT NOT NULL DEFAULT '',
                reaction_count TEXT NOT NULL DEFAULT '',
                comment_count TEXT NOT NULL DEFAULT '',
                repost_count TEXT NOT NULL DEFAULT '',
                content_hash TEXT NOT NULL,
                raw_json TEXT NOT NULL,
                agent_read INTEGER NOT NULL DEFAULT 0
            );
            CREATE TABLE post_observations (
                id INTEGER PRIMARY KEY,
                post_id INTEGER NOT NULL,
                run_id INTEGER NOT NULL,
                source TEXT NOT NULL,
                seen_at TEXT NOT NULL,
                position INTEGER NOT NULL,
                reaction_count TEXT NOT NULL DEFAULT '',
                comment_count TEXT NOT NULL DEFAULT '',
                repost_count TEXT NOT NULL DEFAULT '',
                raw_json TEXT NOT NULL
            );
            """
        )
        conn.execute(
            """
            INSERT INTO linkedin_posts (
                dedupe_key, source_first_seen, first_seen_at, last_seen_at, author,
                text, url, content_hash, raw_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "url:https://linkedin.example/1",
                "saved",
                "2026-05-15T00:00:00+00:00",
                "2026-05-15T00:00:00+00:00",
                "Poster One",
                "Saved post about OAuth security.",
                "https://linkedin.example/1",
                "hash1",
                '{"source":"saved"}',
            ),
        )
        conn.execute(
            """
            INSERT INTO post_observations (post_id, run_id, source, seen_at, position, raw_json)
            VALUES (1, 1, 'saved', '2026-05-15T00:00:00+00:00', 1, '{}')
            """
        )
        conn.execute(
            """
            INSERT INTO linkedin_posts (
                dedupe_key, source_first_seen, first_seen_at, last_seen_at, author,
                text, url, content_hash, raw_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "url:https://linkedin.example/2",
                "feed",
                "2026-05-15T00:00:00+00:00",
                "2026-05-15T00:00:00+00:00",
                "Poster Two",
                "Unscreened feed post about prompt injection.",
                "https://linkedin.example/2",
                "hash2",
                '{"source":"feed"}',
            ),
        )
        conn.execute(
            """
            INSERT INTO post_observations (post_id, run_id, source, seen_at, position, raw_json)
            VALUES (2, 1, 'feed', '2026-05-15T00:00:00+00:00', 2, '{}')
            """
        )

    first = sync_linkedin_db(knowledge_db, linkedin_db_path=linkedin_db)
    second = sync_linkedin_db(knowledge_db, linkedin_db_path=linkedin_db)

    assert first["records"] == 1 and first["inserted"] == 1 and first["updated"] == 0
    assert second["records"] == 1 and second["inserted"] == 1 and second["updated"] == 0
    rows = search_records(knowledge_db, "oauth", limit=5)
    assert len(rows) == 1
    assert rows[0]["source"] == "linkedin_saved"
    assert search_records(knowledge_db, "unscreened", limit=5) == []


# --- _validate_ident ---

def test_validate_ident_accepts_valid_names():
    _validate_ident("records")
    _validate_ident("agent_read")
    _validate_ident("record_classifications")


def test_validate_ident_rejects_sql_injection():
    with pytest.raises(ValueError):
        _validate_ident("records; DROP TABLE records--")


def test_validate_ident_rejects_spaces():
    with pytest.raises(ValueError):
        _validate_ident("bad name")


def test_validate_ident_rejects_leading_digit():
    with pytest.raises(ValueError):
        _validate_ident("1bad")


def test_validate_ident_rejects_empty_string():
    with pytest.raises(ValueError):
        _validate_ident("")


# --- open_db connection safety ---

def test_open_db_closes_connection_on_exception():
    test_dir = local_tmp_dir()
    db_path = test_dir / f"knowledge-{uuid4().hex}.sqlite3"
    captured_conn = []

    try:
        with open_db(db_path) as conn:
            captured_conn.append(conn)
            raise RuntimeError("simulated failure")
    except RuntimeError:
        pass

    # After the context manager exits (even on exception), the connection should be closed.
    # sqlite3 raises ProgrammingError on operations against a closed connection.
    with pytest.raises(Exception):
        captured_conn[0].execute("SELECT 1")


# --- set_record_topics / decode_topics ---

def test_set_and_decode_topics_roundtrip():
    test_dir = local_tmp_dir()
    export = test_dir / "blackhat-talks.json"
    export.write_text(
        json.dumps({
            "talks": [{
                "session_id": "42",
                "title": "Agentic OAuth Security",
                "speakers": "Author A",
                "abstract": "About OAuth and agentic AI.",
                "url": "https://blackhat.example/schedule/#topic-42",
            }]
        }),
        encoding="utf-8",
    )
    db_path = test_dir / f"knowledge-{uuid4().hex}.sqlite3"
    import_exports([export], db_path=db_path)
    record_id = list_unread_records(db_path, limit=1)[0]["id"]

    topics_to_set = ["Agentic AI security", "OAuth & identity risks"]
    set_record_topics(db_path, record_id, topics_to_set, reader="tester")

    with open_db(db_path) as conn:
        row = conn.execute(
            "SELECT agent_topics, agent_read FROM records WHERE id = ?", (record_id,)
        ).fetchone()

    decoded = decode_topics(row["agent_topics"])
    assert set(decoded) == set(topics_to_set)
    assert row["agent_read"] == 1


def test_decode_topics_handles_empty_and_none():
    assert decode_topics("") == []
    assert decode_topics(None) == []


def test_decode_topics_splits_on_pipe():
    result = decode_topics("Topic A|Topic B|Topic C")
    assert result == ["Topic A", "Topic B", "Topic C"]
