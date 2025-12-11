from typing import Callable, Literal

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from deep_agents_langchain.agent.prompts import SYSTEM_PROMPT
from deep_agents_langchain.config.settings import Settings

try:
    from tavily import TavilyClient
except ImportError:  # pragma: no cover - 可选依赖
    TavilyClient = None  # type: ignore


def _build_search_tool(settings: Settings):
    """构建 internet_search 工具；缺少 Key 时返回占位实现。"""
    if settings.tavily_api_key and TavilyClient is not None:
        client = TavilyClient(api_key=settings.tavily_api_key)

        def internet_search(
            query: str,
            max_results: int = 5,
            topic: Literal["general", "news", "finance"] = "general",
            include_raw_content: bool = False,
        ):
            return client.search(
                query=query,
                max_results=max_results,
                include_raw_content=include_raw_content,
                topic=topic,
            )

        internet_search.__doc__ = "Run a web search via Tavily."
        return internet_search

    def internet_search(
        query: str,
        max_results: int = 5,
        topic: Literal["general", "news", "finance"] = "general",
        include_raw_content: bool = False,
    ):
        return "搜索未启用"

    internet_search.__doc__ = "Search placeholder when TAVILY_API_KEY is missing."
    return internet_search


def build_agent(settings: Settings):
    """按设计文档创建 deep agent。"""
    tools: list[Callable] = [_build_search_tool(settings)]
    backend = FilesystemBackend(root_dir=settings.workspace_root, virtual_mode=True)
    agent = create_deep_agent(
        tools=tools,
        backend=backend,
        system_prompt=SYSTEM_PROMPT,
        model=settings.default_model,
    )
    return agent

