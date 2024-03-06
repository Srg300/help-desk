from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.base.dependencies import get_session
from db.models import Role

from .dto import RoleCreateDto, RoleUpdateDto
from .exception import RoleAlreadyExistsError
from .repository import RoleRepository


class RoleCommandCreate:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]) -> None:
        self._session = session
        self._repository = RoleRepository(session=self._session)

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

        role = await self._repository.create(
            dto=dto,
        )
        self._session.add(role)
        await self._session.commit()
        return role


class RoleCommandUpdate:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]) -> None:
        self._session = session
        self._repository = RoleRepository(session=self._session)

    async def execute(
        self,
        id_: int,
        dto: RoleUpdateDto,
    ) -> Role:
        stmt = self._repository.update_stmt(
            id_=id_,
            dto=dto,
        )

        return (await self._session.execute(stmt)).scalar_one()


class RoleCommandDelete:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]) -> None:
        self._session = session
        self._repository = RoleRepository(session=self._session)

    async def execute(
        self,
        id_: int,
    ) -> int | None:
        role = await self._repository.get(id_=id_)
        if role is None:
            return None
        await self._session.delete(role)
        await self._session.commit()
        return id_
