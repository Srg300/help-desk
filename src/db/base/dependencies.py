import contextlib
from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from .engine import async_engine, async_session_factory


@contextlib.asynccontextmanager
async def get_engine() -> AsyncIterator[AsyncEngine]:
    yield async_engine
    await async_engine.dispose()


@contextlib.asynccontextmanager
async def get_session() -> AsyncIterator[AsyncSession]:
    async with async_session_factory.begin() as session:
        yield session
