"""Browser agent stub — real Playwright loop in Lessons 09–10.

Colab can mock tools; local machine runs the real browser.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class AgentAction:
    tool: str
    args: dict[str, Any]


@dataclass
class AgentResult:
    ok: bool
    observation: str
    data: dict[str, Any] = field(default_factory=dict)


ToolFn = Callable[..., AgentResult]


class BrowserAgent:
    """observe → think → act loop (tools registered gradually)."""

    def __init__(self) -> None:
        self.tools: dict[str, ToolFn] = {
            "goto": self._goto_stub,
            "extract_text": self._extract_stub,
        }
        self.history: list[str] = []

    def _goto_stub(self, url: str) -> AgentResult:
        self.history.append(f"goto {url}")
        return AgentResult(ok=True, observation=f"Opened (stub): {url}", data={"url": url})

    def _extract_stub(self) -> AgentResult:
        text = "Stub page text — replace with Playwright in Lesson 09."
        return AgentResult(ok=True, observation=text, data={"text": text})

    def run_tool(self, action: AgentAction) -> AgentResult:
        fn = self.tools.get(action.tool)
        if not fn:
            return AgentResult(ok=False, observation=f"Unknown tool: {action.tool}")
        return fn(**action.args)
