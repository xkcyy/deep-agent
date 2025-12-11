from deep_agents_langchain.config.settings import get_settings


def test_settings_defaults():
    settings = get_settings()
    assert settings.default_model
    assert settings.workspace_root

