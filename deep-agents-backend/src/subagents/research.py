"""Research subagent - Specialized for in-depth research tasks."""

from src.agent.prompts import RESEARCH_AGENT_PROMPT
from src.tools.search import internet_search

research_subagent = {
    "name": "research-agent",
    "description": (
        "Conducts in-depth research on specific topics using web search. "
        "Use when you need detailed information that requires multiple searches "
        "and synthesis of findings. Returns structured research reports."
    ),
    "system_prompt": RESEARCH_AGENT_PROMPT,
    "tools": [internet_search],
}

