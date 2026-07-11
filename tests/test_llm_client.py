import json
import os

import llm_client


class _FakeResponses:
    def __init__(self, output):
        self.output = output
        self.requests = []

    def create(self, **kwargs):
        self.requests.append(kwargs)

        class Response:
            pass

        response = Response()
        response.output = self.output
        return response


class _FakeOpenAI:
    def __init__(self, output):
        self.responses = _FakeResponses(output)


def test_openai_adapter_normalizes_text_response():
    client = _FakeOpenAI([
        {
            "type": "message",
            "content": [{"type": "output_text", "text": "answer"}],
        }
    ])
    messages = llm_client.OpenAIMessagesAdapter(client)

    response = messages.create(
        model="gpt-5.5",
        max_tokens=100,
        system="system prompt",
        messages=[{"role": "user", "content": "question"}],
    )

    assert response.stop_reason == "end_turn"
    assert response.content[0].text == "answer"
    assert client.responses.requests[0]["instructions"] == "system prompt"
    assert client.responses.requests[0]["max_output_tokens"] == 100


def test_openai_adapter_normalizes_function_call_and_tool_result_roundtrip():
    client = _FakeOpenAI([
        {
            "type": "function_call",
            "call_id": "call_1",
            "name": "search_records",
            "arguments": json.dumps({"query": "authentication"}),
        }
    ])
    messages = llm_client.OpenAIMessagesAdapter(client)

    response = messages.create(
        model="gpt-5.5",
        max_tokens=100,
        system=[{"type": "text", "text": "agent system", "cache_control": {"type": "ephemeral"}}],
        tools=[
            {
                "name": "search_records",
                "description": "Search records",
                "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}},
            }
        ],
        messages=[
            {"role": "user", "content": "find auth"},
            {
                "role": "assistant",
                "content": [
                    llm_client.ToolUseBlock(
                        id="call_0",
                        name="search_records",
                        input={"query": "auth"},
                    )
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": "call_0",
                        "content": "result",
                    }
                ],
            },
        ],
    )

    request = client.responses.requests[0]
    assert response.stop_reason == "tool_use"
    assert response.content[0].id == "call_1"
    assert response.content[0].name == "search_records"
    assert response.content[0].input == {"query": "authentication"}
    assert request["instructions"] == "agent system"
    assert request["tools"][0]["type"] == "function"
    assert {"type": "function_call_output", "call_id": "call_0", "output": "result"} in request["input"]


def test_load_project_env_reads_explicit_file_without_overriding_environment(tmp_path, monkeypatch):
    env_path = tmp_path / ".env"
    env_path.write_text(
        "OPENAI_API_KEY=from-file\nANTHROPIC_API_KEY=anthropic-from-file\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("OPENAI_API_KEY", "already-set")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)

    llm_client.load_project_env(env_path)

    assert os.environ["OPENAI_API_KEY"] == "already-set"
    assert os.environ["ANTHROPIC_API_KEY"] == "anthropic-from-file"
