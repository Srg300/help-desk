from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.base.dependencies import get_session
from db.models import Role

from .repository import RoleRepository


class RoleService:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._repository = RoleRepository(session=self._session)

    async def get_by_id(
        self,
        id_: int,
    ) -> Role:
        return await self._repository.get(id_=id_)


async def role_service(session: AsyncSession = Depends(get_session)) -> RoleService:
    return RoleService(session=session)
