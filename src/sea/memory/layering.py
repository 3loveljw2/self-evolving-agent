"""Layering heuristics: classify a memory entry into L1/L2/L3.

P0 uses lightweight rules (keyword + structure hints). The boundary is
deliberately simple — a human or the main agent confirms before anything
is promoted into kb (auditable distillation).
"""
from __future__ import annotations

import re
from datetime import date

_DATE_RE = re.compile(r"(19|20)\d{2}[-/.]\d{1,2}([-/.]\d{1,2})?")
_RULE_HINTS = ("# ", "## ", "规则", "原则", "方法论", "铁律", "sop", "SOP", "必须", "禁止", "永远")


def classify(text: str) -> str:
    """Return 'scratch' | 'logs' | 'kb' for a memory entry."""
    t = text.strip()
    if not t:
        return "scratch"
    # L3 kb: rule-like content (headings, normative words) and long enough
    if len(t) >= 30 and any(h in t for h in _RULE_HINTS):
        return "kb"
    # L2 logs: dated entries or task-like records
    if _DATE_RE.search(t) or "任务" in t or "记录" in t or "完成" in t:
        return "logs"
    # L1 scratch: everything else (low retention)
    return "scratch"


def _safe_name(text: str) -> str:
    """First line → file name slug (max 40 chars, safe chars only)."""
    first = text.strip().splitlines()[0] if text.strip() else "entry"
    slug = re.sub(r"[^\w\u4e00-\u9fff-]", "", first)[:40]
    return slug or "entry"
