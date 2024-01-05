from typing import Annotated

from fastapi import APIRouter, Depends, status

from core.domain.role.command import RoleCommand, role_command
from core.domain.role.service import RoleService, role_service

from ._exception import role_not_found
from ._schemas import RoleCreateSchema, RoleResponse, RoleUpdateSchema

router = APIRouter(
    tags=["roles"],
    prefix="/roles",
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_role(
    schema: RoleCreateSchema,
    command: Annotated[RoleCommand, Depends(role_command)],
) -> RoleResponse:
    role = await command.create(dto=schema)
    return RoleResponse(
        id=role.id,
        name=role.name,
        weight=role.weight,
    )


@router.get("/{role_id}", status_code=status.HTTP_200_OK)
async def get_by_id(
    role_id: int,
    service: Annotated[RoleService, Depends(role_service)],
) -> RoleResponse:
    role = await service.get_by_id(id_=role_id)
    if role is None:
        raise role_not_found
    return RoleResponse(
        id=role.id,
        name=role.name,
        weight=role.weight,
    )


@router.patch("/{role_id}", status_code=status.HTTP_200_OK)
async def update(
    role_id: int,
    schema: RoleUpdateSchema,
    command: Annotated[RoleCommand, Depends(role_command)],
) -> RoleResponse:
    role = await command.update(
        id_=role_id,
        dto=schema,
    )
    if role is None:
        raise role_not_found
    return RoleResponse(
        id=role.id,
        name=role.name,
        weight=role.weight,
    )


@router.delete("/{role_id}", status_code=status.HTTP_200_OK)
async def delete_by_id(
    role_id: int,
    command: Annotated[RoleCommand, Depends(role_command)],
) -> dict[str, str]:
    role = await command.delete(id_=role_id)
    if role is None:
        raise role_not_found
    return {"message": f"role by id {role_id} is deleted"}
