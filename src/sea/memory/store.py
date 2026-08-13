"""Memory store: append/read Markdown memory files per level."""
from __future__ import annotations

from datetime import datetime

from sea.config import Config, LEVELS
from sea.memory.layering import classify


class LevelError(ValueError):
    """Raised when an unknown memory level is used."""


def add(cfg: Config, text: str, level: str | None = None) -> str:
    """Append a memory entry. Auto-classifies when level is None.

    Returns the absolute path of the written file.
    """
    text = text.strip()
    if not text:
        raise ValueError("empty memory entry")
    if level is None:
        level = classify(text)
    if level not in LEVELS:
        raise LevelError(f"invalid level: {level!r} (expected one of {LEVELS})")

    d = cfg.level_dir(level)
    d.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n## {stamp}\n\n{text}\n"
    fname = f"memory-{datetime.now().strftime('%Y-%m-%d')}.md"
    path = d / fname
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(entry)
    return str(path)


def read(cfg: Config, level: str) -> str:
    """Read all entries of a level, newest file first."""
    if level not in LEVELS:
        raise LevelError(f"invalid level: {level!r} (expected one of {LEVELS})")
    d = cfg.level_dir(level)
    if not d.exists():
        return ""
    parts: list[str] = []
    for p in sorted(d.glob("*.md"), reverse=True):
        parts.append(f"--- {p.name} ---\n{p.read_text(encoding='utf-8')}")
    return "\n".join(parts)
