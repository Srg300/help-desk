from db.base.dependencies import get_session
from db.models import Role

from .dto import RoleCreateDto, RoleUpdateDto
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

    async def update(
        self,
        id_: int,
        dto: RoleUpdateDto,
    ) -> Role:
        stmt = self._repository.update_stmt(
            id_=id_,
            dto=dto,
        )

        async with self._session as session:
            return (await session.execute(stmt)).scalar_one()

    async def delete(
        self,
        id_: int,
    ) -> int | None:
        async with self._session as session:
            role = await session.get(ident=id_, entity=Role)
            if role is None:
                return None

            await session.delete(role)
            await session.commit()
            return id_
