#!/usr/bin/env python3
"""
Shared LLM client adapter for knowledge agents and scripts.

The rest of the codebase uses a small Anthropic-like interface:
    client.messages.create(model=..., max_tokens=..., system=..., messages=..., tools=...)

This module centralizes provider-specific API calls and normalizes OpenAI
Responses API outputs into that shape.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from config import llm_settings

APP_DIR = Path(__file__).resolve().parent


def load_project_env(path: Path | None = None) -> bool:
    try:
        from dotenv import load_dotenv
    except ImportError as exc:
        raise RuntimeError(
            "The python-dotenv package is not installed. Install dependencies "
            "with `python -m pip install -r requirements.txt`."
        ) from exc
    return bool(load_dotenv(dotenv_path=path or APP_DIR / ".env", override=False))


@dataclass
class TextBlock:
    text: str
    type: str = "text"


@dataclass
class ToolUseBlock:
    id: str
    name: str
    input: dict[str, Any]
    type: str = "tool_use"


@dataclass
class LLMResponse:
    content: list[TextBlock | ToolUseBlock]
    stop_reason: str
    raw: Any = None


def _get(obj: Any, key: str, default: Any = None) -> Any:
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _system_to_text(system: str | list[dict[str, Any]] | None) -> str:
    if not system:
        return ""
    if isinstance(system, str):
        return system
    parts: list[str] = []
    for item in system:
        if isinstance(item, dict):
            text = item.get("text", "")
            if text:
                parts.append(str(text))
    return "\n\n".join(parts)


def _anthropic_tools_to_openai(tools: list[dict[str, Any]] | None) -> list[dict[str, Any]] | None:
    if not tools:
        return None
    converted = []
    for tool in tools:
        if tool.get("type") == "function":
            converted.append(tool)
            continue
        converted.append({
            "type": "function",
            "name": tool["name"],
            "description": tool.get("description", ""),
            "parameters": tool.get("input_schema", {"type": "object", "properties": {}}),
        })
    return converted


def _anthropic_messages_to_openai_input(messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    converted: list[dict[str, Any]] = []
    for message in messages:
        role = message.get("role", "user")
        content = message.get("content", "")

        if isinstance(content, str):
            converted.append({"role": role, "content": content})
            continue

        if role == "assistant" and isinstance(content, list):
            text_parts = []
            for block in content:
                block_type = _get(block, "type")
                if block_type == "text":
                    text = _get(block, "text", "")
                    if text:
                        text_parts.append(str(text))
                elif block_type == "tool_use":
                    converted.append({
                        "type": "function_call",
                        "call_id": _get(block, "id"),
                        "name": _get(block, "name"),
                        "arguments": json.dumps(_get(block, "input", {})),
                    })
            if text_parts:
                converted.append({"role": "assistant", "content": "\n\n".join(text_parts)})
            continue

        if role == "user" and isinstance(content, list):
            for block in content:
                block_type = _get(block, "type")
                if block_type == "tool_result":
                    converted.append({
                        "type": "function_call_output",
                        "call_id": _get(block, "tool_use_id"),
                        "output": str(_get(block, "content", "")),
                    })
            continue

        converted.append({"role": role, "content": str(content)})
    return converted


def _normalize_openai_response(response: Any) -> LLMResponse:
    blocks: list[TextBlock | ToolUseBlock] = []
    output = _get(response, "output", []) or []

    for item in output:
        item_type = _get(item, "type")
        if item_type == "message":
            for content in _get(item, "content", []) or []:
                text = _get(content, "text", "")
                if text:
                    blocks.append(TextBlock(str(text)))
        elif item_type == "function_call":
            raw_args = _get(item, "arguments", "{}") or "{}"
            try:
                parsed_args = json.loads(raw_args)
            except json.JSONDecodeError:
                parsed_args = {}
            blocks.append(ToolUseBlock(
                id=str(_get(item, "call_id", _get(item, "id", ""))),
                name=str(_get(item, "name", "")),
                input=parsed_args,
            ))

    if not blocks:
        output_text = _get(response, "output_text", "")
        if output_text:
            blocks.append(TextBlock(str(output_text)))

    has_tool = any(getattr(block, "type", "") == "tool_use" for block in blocks)
    return LLMResponse(
        content=blocks,
        stop_reason="tool_use" if has_tool else "end_turn",
        raw=response,
    )


class OpenAIMessagesAdapter:
    def __init__(self, client: Any):
        self._client = client

    def create(
        self,
        *,
        model: str,
        max_tokens: int,
        system: str | list[dict[str, Any]] | None = None,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> LLMResponse:
        request: dict[str, Any] = {
            "model": model,
            "input": _anthropic_messages_to_openai_input(messages),
            "max_output_tokens": max_tokens,
        }
        instructions = _system_to_text(system)
        if instructions:
            request["instructions"] = instructions
        openai_tools = _anthropic_tools_to_openai(tools)
        if openai_tools:
            request["tools"] = openai_tools
        if "tool_choice" in kwargs:
            request["tool_choice"] = kwargs["tool_choice"]
        if "text" in kwargs:
            request["text"] = kwargs["text"]

        return _normalize_openai_response(self._client.responses.create(**request))


class OpenAIChatGPTClient:
    provider = "openai"

    def __init__(self, **kwargs: Any):
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise RuntimeError(
                "The OpenAI Python package is not installed. Install it with "
                "`python -m pip install openai` and set OPENAI_API_KEY."
            ) from exc
        self._client = OpenAI(**kwargs)
        self.messages = OpenAIMessagesAdapter(self._client)


def create_client(provider: str | None = None) -> Any:
    load_project_env()
    provider_name = llm_settings.get_provider(provider)
    if provider_name in {"openai", "chatgpt", "gpt"}:
        return OpenAIChatGPTClient()
    if provider_name in {"anthropic", "claude"}:
        try:
            import anthropic
        except ImportError as exc:
            raise RuntimeError(
                "The Anthropic Python package is not installed. Install it with "
                "`python -m pip install anthropic` and set ANTHROPIC_API_KEY."
            ) from exc
        return anthropic.Anthropic()
    raise ValueError(f"unknown LLM_PROVIDER: {provider_name!r}")
