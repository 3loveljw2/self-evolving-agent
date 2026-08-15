"""P0 tests for sea memory store + layering (independent of implementation)."""
from __future__ import annotations

import os
import tempfile

import pytest

from sea.config import Config
from sea.memory import store
from sea.memory.layering import classify


@pytest.fixture()
def cfg(tmp_path: tempfile.TemporaryDirectory) -> Config:
    old = os.environ.get("SEA_HOME")
    os.environ["SEA_HOME"] = str(tmp_path)
    c = Config()
    c.ensure_layout()
    yield c
    if old is None:
        os.environ.pop("SEA_HOME", None)
    else:
        os.environ["SEA_HOME"] = old


def test_layering_rules() -> None:
    assert classify("随手记一下：今天天气不错") == "scratch"
    assert classify("2026-08-13 完成任务记录") == "logs"
    assert classify("规则：所有发布物先存档后发布，这是铁律。本地优先，蒸馏可审计，边界守护。") == "kb"


def test_add_auto_classify(cfg: Config) -> None:
    path = store.add(cfg, "2026-08-13 完成官网多页版发布任务")
    assert "logs" in path
    assert os.path.exists(path)


def test_add_forced_level(cfg: Config) -> None:
    path = store.add(cfg, "随便一句话", level="kb")
    assert "kb" in path


def test_add_invalid_level(cfg: Config) -> None:
    with pytest.raises(store.LevelError, match="invalid level"):
        store.add(cfg, "x", level="bogus")


def test_add_empty_rejected(cfg: Config) -> None:
    with pytest.raises(ValueError, match="empty"):
        store.add(cfg, "   ")


def test_read_roundtrip(cfg: Config) -> None:
    store.add(cfg, "2026-08-13 一次记忆测试")
    content = store.read(cfg, "logs")
    assert "一次记忆测试" in content


def test_status_counts(cfg: Config) -> None:
    store.add(cfg, "随手记")
    s = cfg.summary()
    assert s["scratch"] == 1


def test_layering_english_rule_hint() -> None:
    # English rule-like content should go to kb (not scratch)
    assert classify("Always keep memory local and never upload raw data. This is the core policy of the framework.") == "kb"


def test_layering_english_log_hint() -> None:
    # English task record should go to logs
    assert classify("2026-08-15 completed the exam paper task") == "logs"


def test_layering_english_scratch() -> None:
    # Short English note stays scratch
    assert classify("just a quick thought") == "scratch"
