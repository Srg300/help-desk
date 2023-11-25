from db.models import Role

from .repository import RoleRepository

from db.base.dependencies import get_session, get_engine


class RoleService:
    def __init__(self) -> None:
        self._session = get_session(get_engine())
        self._repository = RoleRepository(session=self._session)

    async def get_by_id(
        self,
        id: int,
    ) -> Role:
        role = await self._repository.get(id=id)
        return role
