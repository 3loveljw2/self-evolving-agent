"""Configuration: paths for the sea memory home.

Default: ~/.sea (override with $SEA_HOME).
Memory is just files — this module owns where they live.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path

LEVELS: tuple[str, ...] = ("scratch", "logs", "kb")


@dataclass
class Config:
    home: Path = field(
        default_factory=lambda: Path(
            os.environ.get("SEA_HOME", Path.home() / ".sea")
        )
    )

    @property
    def memory_dir(self) -> Path:
        return self.home / "memory"

    @property
    def skills_dir(self) -> Path:
        return self.home / "skills"

    @property
    def task_log(self) -> Path:
        return self.home / "task-log.md"

    @property
    def config_file(self) -> Path:
        return self.home / "config.json"

    def level_dir(self, level: str) -> Path:
        if level not in LEVELS:
            raise ValueError(f"invalid level: {level!r} (expected one of {LEVELS})")
        return self.memory_dir / level

    def ensure_layout(self) -> None:
        """Create the full directory skeleton (idempotent)."""
        for level in LEVELS:
            self.level_dir(level).mkdir(parents=True, exist_ok=True)
        self.skills_dir.mkdir(parents=True, exist_ok=True)
        if not self.task_log.exists():
            self.task_log.write_text("# Task Log\n\n", encoding="utf-8")
        if not self.config_file.exists():
            self.config_file.write_text(
                json.dumps({"levels": list(LEVELS), "version": 1}, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

    def summary(self) -> dict[str, int]:
        """Count markdown files per level."""
        out: dict[str, int] = {}
        for level in LEVELS:
            d = self.level_dir(level)
            out[level] = sum(1 for p in d.glob("*.md")) if d.exists() else 0
        return out
