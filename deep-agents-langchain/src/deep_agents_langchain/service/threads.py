from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from deep_agents_langchain.storage.repositories import (
    create_thread,
    get_state,
    get_thread,
    upsert_state,
)


async def ensure_thread(session: AsyncSession, thread_id: str):
    thread = await get_thread(session, thread_id)
    if thread is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="thread not found")
    return thread


async def create_new_thread(session: AsyncSession, metadata: dict | None = None):
    return await create_thread(session, metadata=metadata)


async def read_state(session: AsyncSession, thread_id: str):
    await ensure_thread(session, thread_id)
    return await get_state(session, thread_id)


async def write_state(session: AsyncSession, thread_id: str, kv: dict, replace: bool):
    await ensure_thread(session, thread_id)
    return await upsert_state(session, thread_id, kv, replace)

