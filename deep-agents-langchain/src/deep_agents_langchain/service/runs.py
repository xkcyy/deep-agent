import asyncio
from typing import Any, AsyncIterator
from fastapi import HTTPException, status
from langchain_core.messages import BaseMessage
from sqlalchemy.ext.asyncio import AsyncSession

from deep_agents_langchain.storage.repositories import append_message, create_run, finish_run, get_thread


async def _extract_last_content(result: Any):
    """从 deep agent 结果中取出最后一条消息内容。"""
    if isinstance(result, dict):
        messages = result.get("messages")
        if isinstance(messages, list) and messages:
            last = messages[-1]
            if isinstance(last, BaseMessage):
                return last.content
            return getattr(last, "content", last)
    return result


async def run_and_stream(agent, session: AsyncSession, thread_id: str, payload: dict) -> AsyncIterator[dict]:
    thread = await get_thread(session, thread_id)
    if thread is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="thread not found")

    run = await create_run(session, thread_id, payload)
    messages = payload.get("messages") or []
    try:
        # 存储用户消息
        for idx, msg in enumerate(messages):
            role = msg.get("role", "user")
            content = msg.get("content")
            await append_message(session, thread_id, role, content, order_num=idx)

        if hasattr(agent, "ainvoke"):
            result = await agent.ainvoke({"messages": messages})  # deepagents 返回 dict 含 messages
        else:  # pragma: no cover - 同步实现兜底
            result = await asyncio.get_event_loop().run_in_executor(None, agent.invoke, {"messages": messages})
        content = await _extract_last_content(result)
        await append_message(session, thread_id, "assistant", content, order_num=len(messages))
        await finish_run(session, run.id, status="completed", output=result)

        async def generator():
            yield {
                "event": "message",
                "data": {
                    "message_id": f"{run.id}-assistant",
                    "thread_id": thread_id,
                    "role": "assistant",
                    "content": content,
                    "tool_calls": [],
                },
            }
            yield {"event": "end", "data": {"run_id": run.id, "status": "completed", "error": None}}

        async for item in generator():
            yield item
    except Exception as exc:  # noqa: BLE001
        await finish_run(session, run.id, status="error", error=str(exc))

        async def error_generator():
            yield {"event": "error", "data": {"message": str(exc), "code": "RUN_FAILED"}}
            yield {"event": "end", "data": {"run_id": run.id, "status": "error", "error": str(exc)}}

        async for item in error_generator():
            yield item

