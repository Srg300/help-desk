from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.errors import ModelAlreadyExistsError
from db.base.dependencies import get_session
from db.models import User

from .dto import UserCreateDto
from .repository import UserRepository


class UserCreateCommand:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]) -> None:
        self._session = session
        self._repository = UserRepository(session=self._session)

    async def execute(
        self,
        dto: UserCreateDto,
    ) -> User | ModelAlreadyExistsError:
        user = await self._repository.get(
            email=dto.email,
        )
        if user:
            return ModelAlreadyExistsError(
                identifier=str(user.id),
            )
        user = await self._repository.create(
            dto=dto,
        )
        self._session.add(user)
        await self._session.commit()
        return user
