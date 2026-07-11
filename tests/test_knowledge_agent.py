from pathlib import Path
from uuid import uuid4
import json

from knowledge_agenting import knowledge_agent as ka
from knowledge_indexing import knowledge_index as ki


class _DummyMessages:
    def __init__(self):
        self.system_text = ""
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        self.system_text = kwargs["system"][0]["text"]
        record_id = json.loads(kwargs["messages"][0]["content"].split("\n\n", 1)[1])["id"]

        class Response:
            content = [type("Content", (), {"text": json.dumps({
                "id": record_id,
                "primary_topic": "Application security",
                "secondary_topics": ["Identity, OAuth, and access delegation"],
                "confidence": "high",
                "rationale": "The record primarily concerns application authorization behavior.",
                "new_topic_candidate": "",
            })})()]

        return Response()


class _DummyClient:
    def __init__(self):
        self.messages = _DummyMessages()


class _AnnotationMessages:
    def __init__(self):
        self.calls = []
        self.use_wrapped_output = False

    def create(self, **kwargs):
        self.calls.append(kwargs)
        record_id = json.loads(kwargs["messages"][0]["content"].split("\n\n", 1)[1])[0]["id"]
        item = {
            "id": record_id,
            "summary": "Compact record digest.",
            "keywords": ["authentication", "testing"],
            "tools": ["ExampleTool"],
            "people": ["Example Person"],
            "claims": ["Testing can be automated."],
            "use_cases": ["application audit"],
            "ai_relevance": "none",
            "content_types": ["research"],
            "security_domains": ["application security"],
            "contains_prompt_injection": False,
            "relevance_notes": "Useful for application audit workflows.",
        }
        payload = {"annotations": [item]} if self.use_wrapped_output else [item]

        class Response:
            pass

        response = Response()
        response.content = [
            type("Content", (), {
                "text": json.dumps(payload)
            })()
        ]
        return response


class _AnnotationClient:
    def __init__(self):
        self.messages = _AnnotationMessages()


def _record(record_id: int) -> dict:
    return {
        "id": record_id,
        "source": "test",
        "year": "2026",
        "title": f"Record {record_id}",
        "author": "Researcher",
        "tags": "",
        "event": "TestConf",
        "url": "",
        "agent_topics": "",
        "text": "Evidence text " * 20,
    }


def test_classify_record_uses_curated_topics_full_text_and_annotation():
    test_dir = Path("data") / "test-tmp" / f"knowledge-agent-{uuid4().hex}"
    test_dir.mkdir(parents=True, exist_ok=True)
    db_path = test_dir / "knowledge.sqlite3"
    with ki.open_db(db_path):
        pass
    ki.seed_topics(db_path)
    ki.store_topic_candidates(
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

    topics = ka.get_classification_topics(db_path)
    client = _DummyClient()
    record = _record(1)
    record["source"] = "blackhat"
    record["title"] = "OAuth Abuse"
    record["text"] = "Browser extension attack surface. " + ("Full record evidence. " * 200)
    annotation = {
        "short_summary": "OAuth authorization risk in an application integration.",
        "keywords_json": json.dumps(["oauth", "authorization"]),
        "tools_json": json.dumps([]),
        "people_json": json.dumps([]),
        "claims_json": json.dumps(["authorization state can be abused"]),
        "use_cases_json": json.dumps(["application security review"]),
        "ai_relevance": "none",
        "content_types_json": json.dumps(["research"]),
        "security_domains_json": json.dumps(["application security", "identity security"]),
        "contains_prompt_injection": 0,
        "relevance_notes": "Useful for application and identity review.",
    }

    result = ka.classify_record(client, record, annotation=annotation, topics=topics)
    content = client.messages.calls[0]["messages"][0]["content"]

    assert "browser extension" not in topics
    assert "Keyword hints:" not in client.messages.system_text
    assert "Definition:" in client.messages.system_text
    assert "prompt injection" in client.messages.system_text
    assert "Full record evidence" in content
    assert "OAuth authorization risk" in content
    assert client.messages.calls[0]["text"]["format"]["type"] == "json_schema"
    assert client.messages.calls[0]["text"]["format"]["strict"] is True
    assert result["primary_topic"] == "Application security"
    assert result["secondary_topics"] == ["Identity, OAuth, and access delegation"]
    assert result["confidence"] == "high"


def test_build_classification_request_errors_before_api_when_input_exceeds_budget(monkeypatch):
    client = _DummyClient()
    record = _record(11)
    record["text"] = "A" * 3000
    monkeypatch.setattr("knowledge_agenting.classify.CLASSIFICATION_MAX_INPUT_TOKENS", 10)

    try:
        ka.classify_record(client, record)
    except ValueError as exc:
        assert "classification input exceeds max token budget" in str(exc)
        assert "record_id=11" in str(exc)
    else:
        raise AssertionError("expected max token budget error")
    assert client.messages.calls == []


def test_annotate_batch_returns_structured_record_digest():
    client = _AnnotationClient()

    result = ka.annotate_batch(client, [_record(7)])

    assert result[0]["id"] == 7
    assert result[0]["summary"] == "Compact record digest."
    assert "authentication" in result[0]["keywords"]
    assert client.messages.calls[0]["system"][0]["text"] == ka.ANNOTATE_SYSTEM
    assert client.messages.calls[0]["max_tokens"] == ka.ANNOTATION_MAX_OUTPUT_TOKENS
    assert client.messages.calls[0]["text"]["format"]["type"] == "json_schema"
    assert client.messages.calls[0]["text"]["format"]["strict"] is True
    assert "50-60 words max" in ka.ANNOTATE_SYSTEM
    assert "ai_relevance" in ka.ANNOTATE_SYSTEM
    assert "contains_prompt_injection" in ka.ANNOTATE_SYSTEM
    assert "untrusted source material" in ka.ANNOTATE_SYSTEM
    assert "source_quality" not in ka.ANNOTATE_SYSTEM
    assert "0-5 items" in ka.ANNOTATE_SYSTEM


def test_annotate_batch_accepts_structured_output_wrapper():
    client = _AnnotationClient()
    client.messages.use_wrapped_output = True

    result = ka.annotate_batch(client, [_record(12)])

    assert result[0]["id"] == 12
    assert result[0]["summary"] == "Compact record digest."


def test_annotate_batch_uses_full_record_text():
    client = _AnnotationClient()
    record = _record(8)
    record["text"] = "A" * 3000

    ka.annotate_batch(client, [record])

    payload = json.loads(client.messages.calls[0]["messages"][0]["content"].split("\n\n", 1)[1])
    assert len(payload[0]["text"]) == 3000


def test_annotate_batch_errors_before_api_when_input_exceeds_budget(monkeypatch):
    client = _AnnotationClient()
    record = _record(9)
    record["text"] = "A" * 3000
    monkeypatch.setattr("knowledge_agenting.annotate.ANNOTATION_MAX_INPUT_TOKENS", 10)

    try:
        ka.annotate_batch(client, [record])
    except ValueError as exc:
        assert "annotation input exceeds max token budget" in str(exc)
        assert "record_ids=[9]" in str(exc)
    else:
        raise AssertionError("expected max token budget error")
    assert client.messages.calls == []


def test_parse_args_supports_reannotate_all():
    args = ka.parse_args(["annotate", "--reannotate-all", "--start-id", "2464"])

    assert args.command == "annotate"
    assert args.reannotate_all is True
    assert args.start_id == 2464


def test_parse_args_supports_classify_start_id():
    args = ka.parse_args(["classify", "--start-id", "2464"])

    assert args.command == "classify"
    assert args.start_id == 2464


def test_format_provider_error_includes_structured_fields():
    class _Response:
        status_code = 403
        headers = {"x-request-id": "req_123"}
        text = '{"error":{"message":"Response text details"}}'

        @staticmethod
        def json():
            return {"error": {"message": "Response JSON details"}}

    class _ProviderError(Exception):
        status_code = 403
        code = "model_not_allowed"
        type = "permission_error"
        request_id = "req_attr"
        response = _Response()
        body = {"error": {"message": "Model access denied"}}

    message = ka.format_provider_error(_ProviderError("forbidden"))

    assert "403" in message
    assert "model_not_allowed" in message
    assert "permission_error" in message
    assert "req_123" in message
    assert "Model access denied" in message
    assert "Response JSON details" in message


def test_discover_record_topics_uses_annotation_and_full_text():
    record = _record(10)
    record["title"] = "MCP Tool Abuse"
    record["text"] = "Full text about malicious MCP servers and agent sandboxing." * 20
    annotation = {
        "short_summary": "MCP tool abuse against AI agents.",
        "keywords_json": json.dumps(["mcp security", "agent sandboxing"]),
        "tools_json": json.dumps(["MCP"]),
        "people_json": json.dumps([]),
        "claims_json": json.dumps(["malicious tools can abuse agent permissions"]),
        "use_cases_json": json.dumps(["agent security review"]),
        "ai_relevance": "about_ai_security",
        "content_types_json": json.dumps(["research"]),
        "security_domains_json": json.dumps(["AI security"]),
        "contains_prompt_injection": 1,
        "relevance_notes": "Useful for agent security taxonomy.",
    }

    content, input_tokens = ka.build_open_topic_request(record, annotation)
    result = ka.discover_record_topics(_DummyClient(), record, annotation, dry_run=True)

    assert "MCP tool abuse against AI agents" in content
    assert "about_ai_security" in content
    assert "Full text about malicious MCP servers" in content
    assert input_tokens > 0
    assert result["id"] == 10
    assert result["dry_run"] is True
    assert result["estimated_input_tokens"] == input_tokens


def test_write_open_topic_report_aggregates_jsonl(tmp_path):
    jsonl_path = tmp_path / "open-topics.jsonl"
    report_path = tmp_path / "open-topics.md"
    jsonl_path.write_text(
        "\n".join([
            json.dumps({
                "id": 1,
                "suggested_topics": ["AI agent security", "MCP security"],
                "ai_relevance": "about_ai_security",
                "content_types": ["research"],
            }),
            json.dumps({
                "id": 2,
                "suggested_topics": ["AI agent security"],
                "ai_relevance": "ai_tooling_for_security",
                "content_types": ["tooling"],
            }),
        ]),
        encoding="utf-8",
    )

    result = ka.write_open_topic_report(jsonl_path, report_path)

    text = result.read_text(encoding="utf-8")
    assert "AI agent security (2)" in text
    assert "MCP security (1)" in text
    assert "about_ai_security: 1" in text
    assert "tooling: 1" in text


