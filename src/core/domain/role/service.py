from db.base.dependencies import get_session
from db.models import Role

from .repository import RoleRepository


class RoleService:
    def __init__(self) -> None:
        self._session = get_session()
        self._repository = RoleRepository(session=self._session)

    async def get_by_id(
        self,
        id_: int,
    ) -> Role:
        return await self._repository.get(id_=id_)
