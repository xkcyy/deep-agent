"""Web search tool using Tavily API."""

from typing import Literal

from langchain_core.tools import tool

from deep_agents_langchain.config import get_settings


@tool
def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
) -> dict:
    """
    Search the internet for information using Tavily.

    Args:
        query: The search query string
        max_results: Maximum number of results to return (default: 5)
        topic: The topic category - 'general', 'news', or 'finance'
        include_raw_content: Whether to include raw page content in results

    Returns:
        Search results containing titles, URLs, and content snippets
    """
    settings = get_settings()

    if not settings.tavily_api_key:
        return {"error": "Tavily API key not configured"}

    try:
        from tavily import TavilyClient

        client = TavilyClient(api_key=settings.tavily_api_key)
        results = client.search(
            query=query,
            max_results=max_results,
            topic=topic,
            include_raw_content=include_raw_content,
        )
        return results
    except Exception as exc:  # pragma: no cover - defensive path
        return {"error": f"Search failed: {exc}"}

