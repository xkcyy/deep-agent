"""Main Deep Agent implementation."""

from pathlib import Path
from typing import Any

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend, StateBackend
from langchain_openai import ChatOpenAI

from src.agent.prompts import MAIN_AGENT_PROMPT
from src.config import get_settings
from src.tools import internet_search
from src.subagents import code_subagent, research_subagent


def _create_backend() -> Any:
    """Create the configured backend (filesystem or state)."""
    settings = get_settings()

    if settings.backend_type == "filesystem":
        root_dir = Path(settings.filesystem_root_dir).resolve()
        root_dir.mkdir(parents=True, exist_ok=True)
        return FilesystemBackend(root_dir=str(root_dir), virtual_mode=True)

    return lambda rt: StateBackend(rt)


def _create_model() -> Any:
    """Create chat model instance with optional custom OpenAI base URL."""
    settings = get_settings()

    if settings.model_provider == "openai":
        model_kwargs: dict[str, Any] = {
            "model": settings.model_name,
            "api_key": settings.openai_api_key,
        }
        if settings.openai_api_base:
            model_kwargs["base_url"] = settings.openai_api_base
        return ChatOpenAI(**model_kwargs)

    # Fallback to provider string if other providers are introduced later
    return settings.default_model


def create_agent():
    """Create and configure the deep agent."""
    # Tools that the agent can use
    tools = [
        internet_search,
    ]

    # Subagents for delegation
    subagents = [
        research_subagent,
        code_subagent,
    ]

    agent = create_deep_agent(
        model=_create_model(),
        tools=tools,
        system_prompt=MAIN_AGENT_PROMPT,
        subagents=subagents,
        backend=_create_backend(),
    )

    return agent


# Create the graph instance for LangGraph server
graph = create_agent()

