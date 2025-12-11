import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from deep_agents_langchain.agent.builder import build_agent
from deep_agents_langchain.api.routes import router
from deep_agents_langchain.config.settings import get_settings
from deep_agents_langchain.storage.db import build_engine, build_sessionmaker, init_db


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title="deep-agents-langchain", version="0.1.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    engine = build_engine(settings)
    sessionmaker = build_sessionmaker(engine)
    agent = build_agent(settings)

    app.state.settings = settings
    app.state.engine = engine
    app.state.sessionmaker = sessionmaker
    app.state.agent = agent

    @app.on_event("startup")
    async def _startup():
        await init_db(engine)

    app.include_router(router)
    return app


app = create_app()


def main():
    import uvicorn

    uvicorn.run("deep_agents_langchain.main:app", host="0.0.0.0", port=8123, reload=True)


if __name__ == "__main__":
    main()

