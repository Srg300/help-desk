from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Role

from .dto import RoleCreateDto, RoleUpdateDto


class RoleRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(
        self,
        dto: RoleCreateDto,
    ) -> Role:
        return Role(
            name=dto.name,
            weight=dto.weight,
        )

    async def get(
        self,
        id_: int | None = None,
        name: str | None = None,
    ) -> Role:
        if id_:
            stmt = select(Role).where(Role.id == id_)
        if name:
            stmt = select(Role).where(Role.name == name)

        return (await self._session.execute(stmt)).scalar_one_or_none()

    async def update(
        self,
        id_: int,
        dto: RoleUpdateDto,
    ) -> Role:
        stmt = (
            update(Role)
            .values(**dto.model_dump(exclude_unset=True))
            .where(Role.id == id_)
            .returning(Role)
        )
        return (await self._session.execute(stmt)).scalar_one()

    def update_stmt(
        self,
        id_: int,
        dto: RoleUpdateDto,
    ) -> Role:
        return (
            update(Role)
            .values(**dto.model_dump(exclude_unset=True))
            .where(Role.id == id_)
            .returning(Role)
        )
