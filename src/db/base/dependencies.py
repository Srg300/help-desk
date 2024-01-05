import contextlib
from collections.abc import AsyncGenerator, AsyncIterator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from .engine import async_engine, async_session_factory


@contextlib.asynccontextmanager
async def get_engine() -> AsyncIterator[AsyncEngine]:
    yield async_engine
    await async_engine.dispose()


@contextlib.asynccontextmanager
async def get_context_session() -> AsyncIterator[AsyncSession]:
    async with async_session_factory.begin() as session:
        yield session
        await session.close()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory.begin() as session:
        yield session
        await session.close()
