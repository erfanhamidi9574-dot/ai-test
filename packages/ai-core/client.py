"""Minimal AI client stub — real HF/API wiring in Lessons 01–07."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AIMessage:
    role: str
    content: str


@dataclass
class AIResponse:
    content: str
    model: str = "stub"


class AIClient:
    """Replace stub with Hugging Face / OpenAI-compatible client as lessons progress."""

    def __init__(self, model: str = "stub") -> None:
        self.model = model

    def complete(self, messages: list[AIMessage], *, temperature: float = 0.2) -> AIResponse:
        _ = temperature
        last_user = next((m.content for m in reversed(messages) if m.role == "user"), "")
        return AIResponse(
            content=f"[stub:{self.model}] Echo: {last_user[:200]}",
            model=self.model,
        )
