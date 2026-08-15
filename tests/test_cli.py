"""CLI integration tests (Typer CliRunner) — covers cli.py entry points."""
from __future__ import annotations

import os

import pytest
from typer.testing import CliRunner

from sea.cli import app
from sea.config import Config

runner = CliRunner()


@pytest.fixture()
def cfg(tmp_path) -> Config:
    old = os.environ.get("SEA_HOME")
    os.environ["SEA_HOME"] = str(tmp_path)
    c = Config()
    c.ensure_layout()
    yield c
    if old is None:
        os.environ.pop("SEA_HOME", None)
    else:
        os.environ["SEA_HOME"] = old


def test_cli_init(cfg) -> None:
    result = runner.invoke(app, ["init"])
    assert result.exit_code == 0
    assert "sea home ready" in result.stdout


def test_cli_add_auto(cfg) -> None:
    runner.invoke(app, ["init"])
    result = runner.invoke(app, ["add", "2026-08-15 完成 CLI 测试任务", "--show"])
    assert result.exit_code == 0
    assert "logs" in result.stdout


def test_cli_add_invalid_level(cfg) -> None:
    runner.invoke(app, ["init"])
    result = runner.invoke(app, ["add", "x", "--level", "bogus"])
    assert result.exit_code == 2


def test_cli_add_empty(cfg) -> None:
    runner.invoke(app, ["init"])
    result = runner.invoke(app, ["add", "   "])
    assert result.exit_code == 2


def test_cli_status(cfg) -> None:
    runner.invoke(app, ["init"])
    runner.invoke(app, ["add", "随手记一条"])
    result = runner.invoke(app, ["status"])
    assert result.exit_code == 0
    assert "L1 scratch" in result.stdout


def test_cli_read_logs(cfg) -> None:
    runner.invoke(app, ["init"])
    runner.invoke(app, ["add", "2026-08-15 读取测试"])
    result = runner.invoke(app, ["read", "logs"])
    assert result.exit_code == 0
    assert "读取测试" in result.stdout


def test_cli_read_invalid_level(cfg) -> None:
    runner.invoke(app, ["init"])
    result = runner.invoke(app, ["read", "bogus"])
    assert result.exit_code == 2


def test_cli_version() -> None:
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.stdout


def test_cli_status_not_initialized(tmp_path, monkeypatch) -> None:
    import os
    monkeypatch.setenv("SEA_HOME", str(tmp_path / "nope"))
    result = runner.invoke(app, ["status"])
    assert result.exit_code == 1
