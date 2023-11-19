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
        model_db = Role(
            name=dto.name,
            weight=dto.weight,
        )
        self._session.add(model_db)
        await self._session.commit()
        await self._session.flush()
        return model_db
