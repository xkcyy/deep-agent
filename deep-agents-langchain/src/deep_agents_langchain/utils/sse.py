from typing import AsyncIterator


def format_sse(event: str, data: str) -> str:
    """构造 SSE 字符串，保持最小化依赖。"""
    return f"event: {event}\ndata: {data}\n\n"


async def sse_stream(generator: AsyncIterator[dict]) -> AsyncIterator[bytes]:
    """将事件 dict 序列化为 SSE 字节流。"""
    import json

    async for item in generator:
        yield format_sse(item["event"], json.dumps(item["data"], ensure_ascii=False)).encode("utf-8")

