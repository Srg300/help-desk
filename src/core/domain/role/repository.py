from sqlalchemy import delete, select, update
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

        async with self._session as session:
            return (await session.execute(stmt)).scalar_one()

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

        async with self._session as session:
            return (await session.execute(stmt)).scalar_one()

    async def delete(
        self,
        id_: int,
    ) -> None:
        stmt = delete(Role).where(Role.id == id_)

        async with self._session as session:
            await session.execute(stmt)
