from typing import Any, Literal
from fastapi import APIRouter, Depends, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from deep_agents_langchain.config.settings import Settings
from deep_agents_langchain.service.runs import run_and_stream
from deep_agents_langchain.service.threads import create_new_thread, read_state, write_state
from deep_agents_langchain.utils.sse import sse_stream


router = APIRouter()


class MessagePayload(BaseModel):
    role: Literal["user", "assistant", "system", "tool"]
    content: Any


class RunInput(BaseModel):
    messages: list[MessagePayload]


class RunRequest(BaseModel):
    input: RunInput
    stream: bool = True


class ThreadCreateRequest(BaseModel):
    metadata: dict | None = None
    initial_state: dict | None = None


class StateUpdateRequest(BaseModel):
    state: dict = Field(default_factory=dict)
    replace: bool = False


async def get_session(request: Request) -> AsyncSession:
    sessionmaker = request.app.state.sessionmaker
    async with sessionmaker() as session:
        yield session


def get_agent(request: Request):
    return request.app.state.agent


def get_settings_dep(request: Request) -> Settings:
    return request.app.state.settings


@router.get("/assistants")
async def list_assistants(settings: Settings = Depends(get_settings_dep)):
    return [
        {
            "assistant_id": "deep_agent",
            "name": "Deep Agent",
            "description": "单智能体，含文件/搜索/待办工具",
            "model": settings.default_model,
            "tools": ["ls", "read_file", "write_file", "edit_file", "glob", "grep", "write_todos", "task", "internet_search"],
        }
    ]


@router.post("/threads")
async def create_thread(req: ThreadCreateRequest, session: AsyncSession = Depends(get_session)):
    thread = await create_new_thread(session, metadata=req.metadata)
    if req.initial_state:
        await write_state(session, thread.id, req.initial_state, replace=True)
    return {"thread_id": thread.id}


@router.post("/threads/{thread_id}/runs/stream")
async def stream_run(
    thread_id: str,
    req: RunRequest,
    session: AsyncSession = Depends(get_session),
    agent=Depends(get_agent),
):
    run_payload = req.input.model_dump()
    generator = run_and_stream(agent, session, thread_id, run_payload)
    return StreamingResponse(sse_stream(generator), media_type="text/event-stream")


@router.get("/threads/{thread_id}/state")
async def get_state(thread_id: str, session: AsyncSession = Depends(get_session)):
    state = await read_state(session, thread_id)
    return {
        "thread_id": thread_id,
        "state": state.kv if state else {},
        "updated_at": state.updated_at if state else None,
    }


@router.put("/threads/{thread_id}/state")
async def update_state(thread_id: str, req: StateUpdateRequest, session: AsyncSession = Depends(get_session)):
    state = await write_state(session, thread_id, kv=req.state, replace=req.replace)
    return {
        "thread_id": thread_id,
        "state": state.kv,
        "updated_at": state.updated_at,
    }

