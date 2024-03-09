from typing import Annotated

from fastapi import APIRouter, Depends, status

from core.domain.user.command import (
    UserCreateCommand,
)
from core.domain.user.service import UserService
from core.exception import ModelAlreadyExistsError

from ._exception import user_exist, user_not_found
from ._schemas import UserCreateSchema, UserResponse

router = APIRouter(
    tags=["auth"],
    prefix="/auth",
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    schema: UserCreateSchema,
    command: Annotated[UserCreateCommand, Depends(UserCreateCommand)],
) -> UserResponse:
    user = await command.execute(dto=schema.to_dto())

    if isinstance(user, ModelAlreadyExistsError):
        raise user_exist

    return UserResponse(
        id=user.id,
        email=user.email,
        username=user.username,
    )


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_by_id(
    user_id: int,
    service: Annotated[UserService, Depends(UserService)],
) -> UserResponse:
    user = await service.get_by_id(id_=user_id)
    if user is None:
        raise user_not_found
    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
    )
