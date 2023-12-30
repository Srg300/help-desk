from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Role

from .dto import RoleCreateDto


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
            return (await session.execute(stmt)).one()
