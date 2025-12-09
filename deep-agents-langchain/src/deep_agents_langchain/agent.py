"""Agent construction for LangChain-based Deep Agent."""

from __future__ import annotations

from contextlib import contextmanager
from typing import Iterable

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

from deep_agents_langchain import prompts
from deep_agents_langchain.config import get_settings
from deep_agents_langchain.state import CURRENT_THREAD_ID, get_store
from deep_agents_langchain.tools import (
    edit_file,
    internet_search,
    ls,
    read_file,
    write_file,
    write_todos,
)


class AgentService:
    """Build and run the single-agent LangChain executor."""

    def __init__(self) -> None:
        self.settings = get_settings()
        self.store = get_store()
        self.tools = [
            internet_search,
            ls,
            read_file,
            write_file,
            edit_file,
            write_todos,
        ]
        self.llm = self._create_model()
        self.executor = self._create_agent_executor()
        self.runnable = self._attach_history(self.executor)

    def _create_model(self) -> ChatOpenAI:
        model_kwargs: dict[str, str] = {"model": self.settings.model_name}
        if self.settings.openai_api_key:
            model_kwargs["api_key"] = self.settings.openai_api_key
        if self.settings.openai_api_base:
            model_kwargs["base_url"] = self.settings.openai_api_base
        return ChatOpenAI(streaming=True, **model_kwargs)

    def _create_agent_executor(self) -> AgentExecutor:
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", prompts.MAIN_AGENT_PROMPT),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )
        agent = create_tool_calling_agent(self.llm, self.tools, prompt)
        return AgentExecutor(agent=agent, tools=self.tools, stream_runnable=True)

    def _attach_history(self, executor: AgentExecutor) -> RunnableWithMessageHistory:
        def get_history(config: dict):
            thread_id = config.get("configurable", {}).get("thread_id")
            if not thread_id:
                raise ValueError("thread_id missing in config")
            state = self.store.ensure(thread_id)
            return state.history

        return RunnableWithMessageHistory(
            executor,
            get_history,
            input_messages_key="input",
            history_messages_key="history",
        )

    @contextmanager
    def _thread_context(self, thread_id: str):
        token = CURRENT_THREAD_ID.set(thread_id)
        try:
            state = self.store.ensure(thread_id)
            state.touch()
            yield
        finally:
            CURRENT_THREAD_ID.reset(token)

    def invoke(self, thread_id: str, message: str) -> dict:
        """Run a single turn and return the final state."""
        with self._thread_context(thread_id):
            result = self.runnable.invoke(
                {"input": message},
                config={
                    "configurable": {"thread_id": thread_id},
                },
            )
        return result  # AgentExecutor returns dict with output key

    def stream(self, thread_id: str, message: str) -> Iterable:
        """Stream a single turn; yields LangChain stream events."""
        with self._thread_context(thread_id):
            yield from self.runnable.stream(
                {"input": message},
                config={
                    "configurable": {"thread_id": thread_id},
                },
            )

