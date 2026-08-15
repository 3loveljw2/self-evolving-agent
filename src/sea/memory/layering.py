"""Layering heuristics: classify a memory entry into L1/L2/L3.

P0 uses lightweight rules (keyword + structure hints). The boundary is
deliberately simple — a human or the main agent confirms before anything
is promoted into kb (auditable distillation).

Bilingual rules: Chinese and English keywords are both supported so that
English memories don't all fall into L1 scratch.
"""
from __future__ import annotations

import re

_DATE_RE = re.compile(r"(19|20)\d{2}[-/.]\d{1,2}([-/.]\d{1,2})?")
# L3 kb rule-like hints (normative / policy language), bilingual
_RULE_HINTS = (
    "# ", "## ",
    "规则", "原则", "方法论", "铁律", "sop", "SOP", "必须", "禁止", "永远",
    "rule", "rules", "principle", "principles", "method", "methodology",
    "always", "never", "must", "important", "essential", "policy", "do not",
)
# L2 logs hints (task / record language), bilingual
_LOG_HINTS = (
    "任务", "记录", "完成",
    "task", "tasks", "log", "logs", "completed", "finished", "done",
    "record", "records", "session",
)


def classify(text: str) -> str:
    """Return 'scratch' | 'logs' | 'kb' for a memory entry."""
    t = text.strip()
    low = t.lower()
    if not t:
        return "scratch"
    # L3 kb: rule-like content (headings, normative words) and long enough
    if len(t) >= 30 and any(h in low for h in _RULE_HINTS):
        return "kb"
    # L2 logs: dated entries or task-like records
    if _DATE_RE.search(t) or any(h in low for h in _LOG_HINTS):
        return "logs"
    # L1 scratch: everything else (low retention)
    return "scratch"
