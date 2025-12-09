"""Basic tests for LangChain Deep Agent backend."""

from fastapi.testclient import TestClient

from deep_agents_langchain.agent import AgentService
from deep_agents_langchain.server import create_app


def test_agent_service_initializes():
    service = AgentService()
    assert service.tools, "Tools should be registered"
    assert service.llm is not None


def test_assistants_endpoint():
    app = create_app()
    client = TestClient(app)
    resp = client.get("/assistants")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert data[0]["assistant_id"] == "deep_agent"

