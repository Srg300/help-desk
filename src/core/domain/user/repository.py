from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.base.dependencies import get_session
from db.models import User

from .dto import UserCreateDto


class UserRepository:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]) -> None:
        self._session = session

    async def create(
        self,
        dto: UserCreateDto,
    ) -> User:
        user = User(
            username=dto.username,
            hashed_password=dto.hashed_password,
            email=dto.email,
        )
        self._session.add(user)
        await self._session.commit()
        return user

    async def get(
        self,
        id_: int | None = None,
        email: str | None = None,
        username: str | None = None,
    ) -> User:
        if id_:
            stmt = select(User).where(User.id == id_)
        if email:
            stmt = select(User).where(User.email == email)
        if username:
            stmt = select(User).where(User.username == username)

        return (await self._session.execute(stmt)).scalar_one_or_none()
