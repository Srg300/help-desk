from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.base.dependencies import get_session
from db.models import User

from .repository import UserRepository


class UserService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]) -> None:
        self._session = session
        self._repository = UserRepository(session=self._session)

    async def get_by_id(
        self,
        id_: int,
    ) -> User:
        return await self._repository.get(id_=id_)

    async def get_by_email(
        self,
        email: str,
    ) -> User:
        return await self._repository.get(email=email)
