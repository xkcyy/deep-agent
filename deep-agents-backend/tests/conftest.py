"""Pytest configuration and fixtures."""

import os
import sys

import pytest

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture(autouse=True)
def setup_test_env(monkeypatch):
    """Set up test environment variables."""
    # Set dummy API keys for testing
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("TAVILY_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    monkeypatch.setenv("DEFAULT_MODEL", "openai:gpt-4o-mini")

