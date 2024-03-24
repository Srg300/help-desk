from typing import Annotated

from fastapi import Depends

from core.errors import ModelAlreadyExistsError
from db.models import User

from .dto import UserCreateDto
from .repository import UserRepository


class UserCreateCommand:
    def __init__(
        self,
        repository: Annotated[UserRepository, Depends(UserRepository)],
    ) -> None:
        self._repository = repository

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
        return await self._repository.create(
            dto=dto,
        )
