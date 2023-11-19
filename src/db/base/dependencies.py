import contextlib
from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from .engine import db_helper


@contextlib.asynccontextmanager
async def get_engine() -> AsyncIterator[AsyncEngine]:
    yield db_helper.async_engine
    await db_helper.async_engine.dispose()


@contextlib.asynccontextmanager
async def get_session(
    engine: AsyncEngine,  # noqa: ARG001
) -> AsyncIterator[AsyncSession]:
    async with db_helper.async_session_factory.begin() as session:
        yield session
