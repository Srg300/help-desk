from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.base.dependencies import get_session
from db.models import Role

from .dto import RoleCreateDto, RoleUpdateDto
from .repository import RoleRepository


class RoleCommand:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._repository = RoleRepository(session=self._session)

    async def create(
        self,
        dto: RoleCreateDto,
    ) -> Role:
        role = await self._repository.create(
            dto=dto,
        )
        self._session.add(role)
        await self._session.commit()
        return role

    async def update(
        self,
        id_: int,
        dto: RoleUpdateDto,
    ) -> Role:
        stmt = self._repository.update_stmt(
            id_=id_,
            dto=dto,
        )

        return (await self._session.execute(stmt)).scalar_one()

    async def delete(
        self,
        id_: int,
    ) -> int | None:
        role = await self._repository.get(id_=id_)
        if role is None:
            return None
        await self._session.delete(role)
        await self._session.commit()
        return id_


async def role_command(session: AsyncSession = Depends(get_session)) -> RoleCommand:
    return RoleCommand(session=session)
