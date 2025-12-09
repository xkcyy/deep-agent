"""Todo planning tool."""

from __future__ import annotations

from typing import Iterable, List

from langchain_core.tools import tool

from deep_agents_langchain.state import CURRENT_THREAD_ID, get_store


def _normalize_items(items: str | Iterable[str]) -> List[str]:
    if isinstance(items, str):
        candidates = [part.strip() for part in items.split("\n")]
    else:
        candidates = [str(item).strip() for item in items]
    return [item for item in candidates if item]


@tool
def write_todos(items: str | list[str]) -> dict:
    """Create or replace the todo list for the current thread."""
    thread_id = CURRENT_THREAD_ID.get()
    if not thread_id:
        return {"error": "No active thread; cannot persist todos"}
    todos = _normalize_items(items)
    store = get_store()
    updated = store.update_todos(thread_id, todos)
    return {"todos": updated}

