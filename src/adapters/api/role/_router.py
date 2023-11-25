from fastapi import APIRouter, status

from core.domain.role.command import RoleCommand
from core.domain.role.service import RoleService
from core.domain.role.dto import RoleCreateDto

from ._schemas import RoleCreateSchema, RoleResponse

router = APIRouter(
    tags=["roles"],
    prefix="/roles",
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_role(
    schema: RoleCreateSchema,
) -> RoleResponse:
    command = RoleCommand()

    role = await command.create(
        dto=RoleCreateDto(
            name=schema.name,
            weight=schema.weight,
        ),
    )
    return RoleResponse.model_validate(role)  # type: ignore[no-any-return]


@router.get("/{id}", status_code=status.HTTP_201_CREATED, response_model=None)
async def get_by_id(id: int) -> RoleResponse:
    service = RoleService()
    role = await service.get_by_id(id=id)
    return RoleResponse.model_validate(*role)  # type: ignore[no-any-return]
