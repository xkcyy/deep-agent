from functools import lru_cache
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """应用基础配置，所有环境变量集中在这里读取。"""

    openai_api_key: str | None = Field(default=None, alias="OPENAI_API_KEY")
    openai_api_base: str = Field(default="https://api.openai.com/v1", alias="OPENAI_API_BASE")
    default_model: str = Field(default="openai:gpt-4o-mini", alias="DEFAULT_MODEL")
    tavily_api_key: str | None = Field(default=None, alias="TAVILY_API_KEY")
    workspace_root: str = Field(default="./workspace", alias="WORKSPACE_ROOT")
    sqlite_path: str = Field(default="./workspace/state.db", alias="SQLITE_PATH")
    timeout_seconds: int = Field(default=60, alias="TIMEOUT_SECONDS")
    max_tokens_result_to_file: int = Field(default=20000, alias="MAX_TOKENS_RESULT_TO_FILE")

    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """缓存 Settings，避免重复解析环境变量。"""
    return Settings()  # type: ignore[arg-type]

