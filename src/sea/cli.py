"""sea CLI entry (Typer). Commands: init / add / status / read."""
from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console

from sea import __version__
from sea.config import Config, LEVELS
from sea.memory import store

app = typer.Typer(help="self-evolving-agent memory CLI — local-first Markdown memory.")
console = Console()
err = Console(stderr=True)


def _cfg() -> Config:
    return Config()


@app.command()
def init() -> None:
    """Create the memory directory layout under ~/.sea."""
    cfg = _cfg()
    cfg.ensure_layout()
    console.print(f"[green]✓[/] sea home ready at [bold]{cfg.home}[/]")
    console.print("  memory/scratch  L1 working memory")
    console.print("  memory/logs     L2 episodic logs")
    console.print("  memory/kb       L3 semantic knowledge")
    console.print("  skills/         skill files")
    console.print("  task-log.md     distillation source")


@app.command()
def add(text: str = typer.Argument(..., help="Memory entry to store"),
        level: str = typer.Option(None, "--level", "-l", help="Force level: scratch|logs|kb"),
        show: bool = typer.Option(False, "--show", help="Print the detected level")) -> None:
    """Append a memory entry (auto-classified into L1/L2/L3)."""
    try:
        path = store.add(_cfg(), text, level)
    except ValueError as e:
        err.print(f"[red]✗ {e}[/]")
        raise typer.Exit(code=2)
    detected = Path(path).parent.name
    if show:
        console.print(f"[blue]level[/] {detected}")
    console.print(f"[green]✓[/] saved → [bold]{path}[/]")


@app.command()
def status() -> None:
    """Show memory statistics per level."""
    cfg = _cfg()
    if not cfg.home.exists():
        err.print("[yellow]not initialized — run: sea init[/]")
        raise typer.Exit(code=1)
    summary = cfg.summary()
    console.print(f"[bold]{cfg.home}[/]")
    for level in LEVELS:
        n = summary[level]
        label = {"scratch": "L1 scratch", "logs": "L2 logs", "kb": "L3 kb"}[level]
        console.print(f"  {label:<12} {n} file(s)")


@app.command()
def read(level: str = typer.Argument(..., help="Level to read: scratch|logs|kb")) -> None:
    """Print all entries of a memory level."""
    try:
        content = store.read(_cfg(), level)
    except ValueError as e:
        err.print(f"[red]✗ {e}[/]")
        raise typer.Exit(code=2)
    if not content:
        console.print(f"[yellow](empty)[/] {level}")
    else:
        console.print(content)


@app.command()
def version() -> None:
    """Print sea version."""
    console.print(f"sea {__version__}")


if __name__ == "__main__":
    app()
