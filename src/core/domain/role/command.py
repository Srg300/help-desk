from db.base.dependencies import get_session
from db.models import Role

from .dto import RoleCreateDto
from .repository import RoleRepository


class RoleCommand:
    def __init__(self) -> None:
        self._session = get_session()
        self._repository = RoleRepository(session=self._session)

    async def create(
        self,
        dto: RoleCreateDto,
    ) -> Role:
        role = await self._repository.create(
            dto=dto,
        )
        async with self._session as session:
            session.add(role)
            await session.commit()
            return role
