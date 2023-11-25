from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

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
            id: int | None = None,
            name: str | None = None,
    ) -> Role:
        if id:
            stmt = select(Role).where(Role.id==id)
        if name:
            stmt = select(Role).where(Role.name==name)

        async with self._session as session:
            result = (await session.execute(stmt)).one()
            return result
