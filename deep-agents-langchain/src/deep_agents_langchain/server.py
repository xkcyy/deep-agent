"""FastAPI server exposing LangGraph-compatible endpoints."""

from __future__ import annotations

import json
from typing import Any, Dict, Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from deep_agents_langchain.agent import AgentService
from deep_agents_langchain.config import get_settings
from deep_agents_langchain.state import get_store


class ThreadCreateResponse(BaseModel):
    thread_id: str
    status: str
    updated_at: str
    values: Dict[str, Any] = {}


class ThreadStateRequest(BaseModel):
    values: Dict[str, Any]


class RunInput(BaseModel):
    messages: list[dict] | None = None
    content: str | None = None


def extract_user_content(payload: Dict[str, Any]) -> str:
    """Extract user text from LangGraph-style input payload."""
    if "messages" in payload and isinstance(payload["messages"], list):
        # Pick the last human message content
        for msg in reversed(payload["messages"]):
            if msg.get("role") in {"user", "human"} and "content" in msg:
                return msg["content"]
    if "content" in payload and isinstance(payload["content"], str):
        return payload["content"]
    raise ValueError("No user content found in request input")


def create_app() -> FastAPI:
    app = FastAPI(title="Deep Agents LangChain Backend")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    settings = get_settings()
    store = get_store()
    agent = AgentService()

    def _assistant_payload() -> Dict[str, Any]:
        return {
            "assistant_id": "deep_agent",
            "graph_id": "deep_agent",
            "name": "Deep Agent (LangChain)",
            "description": "Single-agent LangChain backend compatible with DeepAgent UI",
            "config": {"recursion_limit": settings.max_recursion_limit},
            "metadata": {"created_by": "system"},
            "version": 1,
            "created_at": "1970-01-01T00:00:00Z",
            "updated_at": "1970-01-01T00:00:00Z",
            "context": {},
        }

    @app.get("/assistants")
    async def list_assistants():
        return JSONResponse([_assistant_payload()])

    @app.post("/assistants/search")
    async def search_assistants(payload: Dict[str, Any] = None):
        graph_id = (payload or {}).get("graphId")
        if graph_id and graph_id != "deep_agent":
            return JSONResponse([])
        return JSONResponse([_assistant_payload()])

    @app.get("/assistants/{assistant_id}")
    async def get_assistant(assistant_id: str):
        if assistant_id != "deep_agent":
            raise HTTPException(status_code=404, detail="Assistant not found")
        return JSONResponse(_assistant_payload())

    @app.get("/assistants/search")
    async def search_assistants(graphId: Optional[str] = None, limit: int = 100):
        # 简化实现：无多 assistant 场景，始终返回单个 deep_agent
        return JSONResponse(
            [
                {
                    "assistant_id": "deep_agent",
                    "graph_id": graphId or "deep_agent",
                    "name": "Deep Agent (LangChain)",
                    "description": "Single-agent LangChain backend compatible with DeepAgent UI",
                    "config": {"recursion_limit": settings.max_recursion_limit},
                    "metadata": {"created_by": "system"},
                    "created_at": "",
                    "updated_at": "",
                    "version": 1,
                    "context": {},
                }
            ]
        )

    @app.post("/threads", response_model=ThreadCreateResponse)
    async def create_thread():
        state = store.create_thread()
        return ThreadCreateResponse(
            thread_id=state.thread_id,
            status=state.status,
            updated_at=state.updated_at.isoformat(),
            values={"messages": [], "todos": [], "files": {}},
        )

    @app.get("/threads/{thread_id}/state")
    async def get_thread_state(thread_id: str):
        state = store.get(thread_id)
        if not state:
            raise HTTPException(status_code=404, detail="Thread not found")
        return store.as_public_state(thread_id)

    @app.put("/threads/{thread_id}/state")
    async def update_thread_state(thread_id: str, payload: ThreadStateRequest):
        state = store.get(thread_id)
        if not state:
            raise HTTPException(status_code=404, detail="Thread not found")
        values = payload.values or {}
        if "todos" in values:
            store.update_todos(thread_id, list(values["todos"]))
        if "files" in values:
            store.update_files(thread_id, dict(values["files"]))
        return store.as_public_state(thread_id)

    @app.post("/threads/{thread_id}/runs/stream")
    async def stream_run(
        request: Request,
        thread_id: str,
        assistant_id: Optional[str] = None,
    ):
        # Parse body
        body = await request.json()
        input_payload = body.get("input") if isinstance(body, dict) else None
        if not input_payload:
            raise HTTPException(status_code=400, detail="Missing input")

        try:
            user_content = extract_user_content(input_payload)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc))

        async def event_stream():
            try:
                for chunk in agent.stream(thread_id, user_content):
                    payload = {"event": "message", "data": chunk}
                    yield f"data: {json.dumps(payload, default=str)}\n\n"
                # Emit final state snapshot for UI sync
                yield f"data: {json.dumps({'event': 'state', 'data': store.as_public_state(thread_id)}, default=str)}\n\n"
                yield "data: [DONE]\n\n"
            except Exception as exc:  # pragma: no cover - defensive path
                error_payload = {"event": "error", "message": str(exc)}
                yield f"data: {json.dumps(error_payload)}\n\n"

        return StreamingResponse(event_stream(), media_type="text/event-stream")

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app


app = create_app()

