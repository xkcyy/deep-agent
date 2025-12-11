from pathlib import Path
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from deep_agents_langchain.config.settings import Settings
from deep_agents_langchain.storage.models import Base


def build_engine(settings: Settings) -> AsyncEngine:
    """构建异步 SQLite 引擎，保证目录存在。"""
    db_path = Path(settings.sqlite_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return create_async_engine(f"sqlite+aiosqlite:///{db_path}", future=True)


def build_sessionmaker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    """创建异步 Session 工厂。"""
    return async_sessionmaker(engine, expire_on_commit=False)


async def init_db(engine: AsyncEngine) -> None:
    """初始化数据库表。"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

