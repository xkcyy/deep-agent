"""Filesystem tools scoped to a sandbox root."""

from __future__ import annotations

from pathlib import Path

from langchain_core.tools import tool

from deep_agents_langchain.config import get_settings

settings = get_settings()
ROOT_DIR = Path(settings.filesystem_root_dir).resolve()
ROOT_DIR.mkdir(parents=True, exist_ok=True)


def _resolve_path(path: str) -> Path:
    candidate = (ROOT_DIR / path).resolve()
    try:
        candidate.relative_to(ROOT_DIR)
    except ValueError:
        raise ValueError(f"Path {path} escapes sandbox root {ROOT_DIR}")
    return candidate


@tool
def ls(path: str = ".") -> list[str]:
    """List files and directories under the sandbox root."""
    target = _resolve_path(path)
    if not target.exists():
        return []
    if target.is_file():
        return [target.name]
    return sorted(
        [f.name + ("/" if f.is_dir() else "") for f in target.iterdir()],
        key=str.lower,
    )


@tool
def read_file(path: str, offset: int = 0, limit: int = 2000) -> str:
    """Read a file with optional offset/limit."""
    target = _resolve_path(path)
    if not target.exists():
        return f"Error: File '{path}' not found"
    if target.is_dir():
        return f"Error: '{path}' is a directory"
    text = target.read_text(encoding="utf-8")
    return text[offset : offset + limit]


@tool
def write_file(path: str, content: str, overwrite: bool = False) -> str:
    """Write content to a file under the sandbox root."""
    target = _resolve_path(path)
    if target.exists() and not overwrite:
        return f"Error: File '{path}' already exists (set overwrite=True to replace)"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return f"Wrote {len(content)} bytes to {path}"


@tool
def edit_file(path: str, old_string: str, new_string: str, replace_all: bool = False) -> str:
    """Edit file content by replacing text."""
    target = _resolve_path(path)
    if not target.exists():
        return f"Error: File '{path}' not found"
    content = target.read_text(encoding="utf-8")
    if old_string not in content:
        return f"Error: '{old_string}' not found in '{path}'"
    if replace_all:
        updated = content.replace(old_string, new_string)
        occurrences = content.count(old_string)
    else:
        updated = content.replace(old_string, new_string, 1)
        occurrences = 1
    target.write_text(updated, encoding="utf-8")
    return (
        f"Updated '{path}' with {occurrences} replacements; new length {len(updated)} bytes"
    )

