from fastapi import APIRouter, status

from core.domain.role.dto import RoleCreateDto
from core.domain.role.repository import RoleRepository
from db.base.engine import db_helper

from ._schemas import RoleCreateSchema, RoleResponse

router = APIRouter(
    tags=["roles"],
    prefix="/roles",
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_role(
    schema: RoleCreateSchema,
) -> RoleResponse:
    session = db_helper.async_session_factory()
    repository = RoleRepository(session=session)

    obj = await repository.create(
        dto=RoleCreateDto(
            name=schema.name,
            weight=schema.weight,
        ),
    )
    return RoleResponse.model_validate(obj)  # type: ignore[no-any-return]
