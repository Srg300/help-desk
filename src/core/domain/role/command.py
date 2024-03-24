from typing import Annotated

from fastapi import Depends

from db.models import Role

from .dto import RoleCreateDto, RoleUpdateDto
from .exception import RoleAlreadyExistsError
from .repository import RoleRepository


class RoleCommandCreate:
    def __init__(
        self,
        repository: Annotated[RoleRepository, Depends(RoleRepository)],
    ) -> None:
        self._repository = repository

    async def execute(
        self,
        dto: RoleCreateDto,
    ) -> Role | RoleAlreadyExistsError:
        db_role = await self._repository.get(
            name=dto.name,
        )
        if db_role:
            return RoleAlreadyExistsError(
                identifier=db_role.name,
            )

        return await self._repository.create(
            dto=dto,
        )


class RoleCommandUpdate:
    def __init__(
        self,
        repository: Annotated[RoleRepository, Depends(RoleRepository)],
    ) -> None:
        self._repository = repository

    async def execute(
        self,
        id_: int,
        dto: RoleUpdateDto,
    ) -> Role:
        return await self._repository.update(
            id_=id_,
            dto=dto,
        )


class RoleCommandDelete:
    def __init__(
        self,
        repository: Annotated[RoleRepository, Depends(RoleRepository)],
    ) -> None:
        self._repository = repository

    async def execute(
        self,
        id_: int,
    ) -> int | None:
        role = await self._repository.get(id_=id_)
        if role is None:
            return None
        await self._repository.delete(role)
        return id_
