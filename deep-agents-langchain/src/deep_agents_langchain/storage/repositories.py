from datetime import datetime
from typing import Any
from uuid import uuid4
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from deep_agents_langchain.storage.models import Message, Run, State, Thread


async def create_thread(session: AsyncSession, metadata: dict | None = None) -> Thread:
    thread = Thread(id=str(uuid4()), metadata=metadata or {}, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
    session.add(thread)
    await session.commit()
    await session.refresh(thread)
    return thread


async def get_thread(session: AsyncSession, thread_id: str) -> Thread | None:
    result = await session.execute(select(Thread).where(Thread.id == thread_id))
    return result.scalars().first()


async def upsert_state(session: AsyncSession, thread_id: str, kv: dict, replace: bool) -> State:
    existing = await session.execute(select(State).where(State.thread_id == thread_id))
    state = existing.scalars().first()
    now = datetime.utcnow()
    if state is None:
        state = State(thread_id=thread_id, kv=kv, updated_at=now)
        session.add(state)
    else:
        merged = kv if replace else {**(state.kv or {}), **kv}
        await session.execute(
            update(State)
            .where(State.thread_id == thread_id)
            .values(kv=merged, updated_at=now)
        )
    await session.commit()
    await session.refresh(state)
    return state


async def get_state(session: AsyncSession, thread_id: str) -> State | None:
    result = await session.execute(select(State).where(State.thread_id == thread_id))
    return result.scalars().first()


async def create_run(session: AsyncSession, thread_id: str, payload: Any) -> Run:
    run = Run(
        id=str(uuid4()),
        thread_id=thread_id,
        input=payload,
        status="running",
        started_at=datetime.utcnow(),
    )
    session.add(run)
    await session.commit()
    await session.refresh(run)
    return run


async def finish_run(session: AsyncSession, run_id: str, status: str, output: Any | None = None, error: str | None = None) -> Run:
    result = await session.execute(select(Run).where(Run.id == run_id))
    run = result.scalars().first()
    if run is None:
        raise ValueError(f"Run {run_id} not found")
    run.status = status
    run.output = output
    run.error = error
    run.ended_at = datetime.utcnow()
    await session.commit()
    await session.refresh(run)
    return run


async def append_message(session: AsyncSession, thread_id: str, role: str, content: Any, order_num: int) -> Message:
    message = Message(
        id=str(uuid4()),
        thread_id=thread_id,
        role=role,
        content=content,
        order_num=order_num,
        created_at=datetime.utcnow(),
    )
    session.add(message)
    await session.commit()
    await session.refresh(message)
    return message

