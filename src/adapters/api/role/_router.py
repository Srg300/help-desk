from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.domain.role.command import RoleCommand
from core.domain.role.exception import RoleAlreadyExistsError
from core.domain.role.service import RoleService
from db.base.dependencies import get_session

from ._exception import role_exist, role_not_found
from ._schemas import RoleCreateSchema, RoleResponse, RoleUpdateSchema

router = APIRouter(
    tags=["roles"],
    prefix="/roles",
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_role(
    schema: RoleCreateSchema,
    session: Annotated[AsyncSession, Depends(get_session)],
) -> RoleResponse:
    command = RoleCommand(session=session)
    role = await command.create(dto=schema)
    if isinstance(role, RoleAlreadyExistsError):
        raise role_exist

    return RoleResponse(
        id=role.id,
        name=role.name,
        weight=role.weight,
    )


@router.get("/{role_id}", status_code=status.HTTP_200_OK)
async def get_by_id(
    role_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
) -> RoleResponse:
    service = RoleService(session=session)
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
    session: Annotated[AsyncSession, Depends(get_session)],
) -> RoleResponse:
    command = RoleCommand(session=session)
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
    session: Annotated[AsyncSession, Depends(get_session)],
) -> dict[str, str]:
    command = RoleCommand(session=session)
    role = await command.delete(id_=role_id)
    if role is None:
        raise role_not_found
    return {"message": f"role by id {role_id} is deleted"}
