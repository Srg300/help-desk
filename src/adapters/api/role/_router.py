from typing import Annotated

from fastapi import APIRouter, Depends, status

from core.domain.role.command import RoleCommand
from core.domain.role.dto import RoleCreateDto
from core.domain.role.service import RoleService

from ._schemas import RoleCreateSchema, RoleResponse

router = APIRouter(
    tags=["roles"],
    prefix="/roles",
)

command = Annotated[RoleCommand, Depends(RoleCommand)]
service = Annotated[RoleService, Depends(RoleService)]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_role(
    schema: RoleCreateSchema,
    command: command,
) -> RoleResponse:
    role = await command.create(
        dto=RoleCreateDto(
            name=schema.name,
            weight=schema.weight,
        ),
    )
    return RoleResponse.model_validate(role)  # type: ignore[no-any-return]


@router.get("/{id}", status_code=status.HTTP_201_CREATED, response_model=None)
async def get_by_id(id_: int, service: service) -> RoleResponse:
    role = await service.get_by_id(id_=id_)
    return RoleResponse.model_validate(*role)  # type: ignore[no-any-return]
