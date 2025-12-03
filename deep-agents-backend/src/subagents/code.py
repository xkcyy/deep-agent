"""Code subagent - Specialized for code analysis and generation tasks."""

from src.agent.prompts import CODE_AGENT_PROMPT

code_subagent = {
    "name": "code-agent",
    "description": (
        "Specialized agent for code analysis, generation, and refactoring tasks. "
        "Use when you need to write, review, or modify code. "
        "Follows best practices and provides high-quality, maintainable code."
    ),
    "system_prompt": CODE_AGENT_PROMPT,
    "tools": [],  # Uses filesystem tools from main agent
}

