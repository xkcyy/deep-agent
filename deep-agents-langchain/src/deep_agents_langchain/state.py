"""Thread state management for the LangChain backend."""

from __future__ import annotations

from contextvars import ContextVar
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List
from uuid import uuid4

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage, ToolMessage

CURRENT_THREAD_ID: ContextVar[str | None] = ContextVar("current_thread_id", default=None)


@dataclass
class ThreadState:
    """Per-thread runtime state."""

    thread_id: str
    history: InMemoryChatMessageHistory = field(default_factory=InMemoryChatMessageHistory)
    todos: List[str] = field(default_factory=list)
    files: Dict[str, str] = field(default_factory=dict)
    status: str = "open"
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def touch(self) -> None:
        """Update last modified timestamp."""
        self.updated_at = datetime.now(timezone.utc)


class ThreadStore:
    """In-memory thread store for state, todos, and message history."""

    def __init__(self) -> None:
        self._threads: Dict[str, ThreadState] = {}

    def create_thread(self) -> ThreadState:
        thread_id = str(uuid4())
        state = ThreadState(thread_id=thread_id)
        self._threads[thread_id] = state
        return state

    def get(self, thread_id: str) -> ThreadState | None:
        return self._threads.get(thread_id)

    def ensure(self, thread_id: str) -> ThreadState:
        if thread_id not in self._threads:
            self._threads[thread_id] = ThreadState(thread_id=thread_id)
        return self._threads[thread_id]

    def list(self) -> List[ThreadState]:
        return list(self._threads.values())

    def update_todos(self, thread_id: str, todos: List[str]) -> List[str]:
        state = self.ensure(thread_id)
        state.todos = todos
        state.touch()
        return state.todos

    def update_files(self, thread_id: str, files: Dict[str, str]) -> Dict[str, str]:
        state = self.ensure(thread_id)
        state.files = files
        state.touch()
        return state.files

    def _serialize_message(self, message: BaseMessage) -> Dict[str, str]:
        if isinstance(message, HumanMessage):
            role = "human"
        elif isinstance(message, AIMessage):
            role = "ai"
        elif isinstance(message, ToolMessage):
            role = "tool"
        elif isinstance(message, SystemMessage):
            role = "system"
        else:
            role = message.type
        return {
            "id": getattr(message, "id", None) or str(uuid4()),
            "type": role,
            "content": message.content,
        }

    def _serialize_history(self, history: InMemoryChatMessageHistory) -> List[Dict[str, str]]:
        return [self._serialize_message(msg) for msg in history.messages]

    def as_public_state(self, thread_id: str) -> Dict:
        state = self.ensure(thread_id)
        return {
            "thread_id": state.thread_id,
            "status": state.status,
            "updated_at": state.updated_at.isoformat(),
            "values": {
                "messages": self._serialize_history(state.history),
                "todos": state.todos,
                "files": state.files,
            },
        }


_STORE = ThreadStore()


def get_store() -> ThreadStore:
    """Return singleton thread store."""
    return _STORE

