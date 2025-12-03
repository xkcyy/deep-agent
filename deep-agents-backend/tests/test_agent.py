"""Tests for the Deep Agent."""

import pytest


class TestDeepAgent:
    """Test cases for the Deep Agent."""

    def test_agent_creation(self):
        """Test that the agent can be created successfully."""
        from src.agent import create_agent

        agent = create_agent()
        assert agent is not None

    def test_agent_has_tools(self):
        """Test that the agent has the expected tools."""
        from src.agent import create_agent

        agent = create_agent()
        # The agent should be a compiled graph
        assert hasattr(agent, "invoke")
        assert hasattr(agent, "stream")

    @pytest.mark.skip(reason="Requires real OpenAI credentials for integration testing")
    @pytest.mark.asyncio
    async def test_agent_invoke(self):
        """Integration test for agent invocation (skipped by default)."""
        from src.agent import create_agent

        agent = create_agent()
        config = {"configurable": {"thread_id": "test-thread"}}

        result = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "Hello!"}]},
            config=config,
        )

        assert "messages" in result
        assert len(result["messages"]) > 0


class TestTools:
    """Test cases for agent tools."""

    def test_search_tool_definition(self):
        """Test that the search tool is properly defined."""
        from src.tools import internet_search

        assert internet_search.name == "internet_search"
        assert internet_search.description is not None


class TestSubagents:
    """Test cases for subagents."""

    def test_research_subagent_config(self):
        """Test research subagent configuration."""
        from src.subagents import research_subagent

        assert research_subagent["name"] == "research-agent"
        assert "description" in research_subagent
        assert "system_prompt" in research_subagent
        assert "tools" in research_subagent

    def test_code_subagent_config(self):
        """Test code subagent configuration."""
        from src.subagents import code_subagent

        assert code_subagent["name"] == "code-agent"
        assert "description" in code_subagent
        assert "system_prompt" in code_subagent

