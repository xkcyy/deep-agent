"""Application settings using Pydantic Settings."""

from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # LLM Provider Configuration
    openai_api_key: str
    openai_api_base: str | None = None

    # Search Tool API Key
    tavily_api_key: str | None = None

    # Agent Configuration
    default_model: str = "openai:gpt-4o-mini"
    max_recursion_limit: int = 100

    # Backend Configuration
    backend_type: Literal["state", "filesystem"] = "filesystem"
    filesystem_root_dir: str = "./workspace"

    @property
    def model_provider(self) -> str:
        """Extract model provider from default_model string."""
        if ":" in self.default_model:
            return self.default_model.split(":")[0]
        return "openai"

    @property
    def model_name(self) -> str:
        """Extract model name from default_model string."""
        if ":" in self.default_model:
            return self.default_model.split(":", 1)[1]
        return self.default_model


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()

