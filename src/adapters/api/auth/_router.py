from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, status

from core.domain.auth.command import JWTCreateCommand, JWTRefreshCommand
from core.errors import AuthenticationFailed, PermissionCoreError

from ._schemas import JWTAccessSchema, JWTCreateSchema, JWTSchema

router = APIRouter(
    tags=["auth"],
    prefix="/auth",
)


@router.post("/jwt/create", status_code=status.HTTP_201_CREATED)
async def auth_jwt_create(
    schema: JWTCreateSchema,
    command: Annotated[JWTCreateCommand, Depends(JWTCreateCommand)],
) -> JWTSchema:
    tokens = await command.execute(
        dto=schema.to_dto(),
    )
    if isinstance(tokens, AuthenticationFailed):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return JWTSchema(
        access=tokens.access,
        refresh=tokens.refresh,
    )


@router.post("/jwt/refresh", status_code=status.HTTP_200_OK)
async def auth_jwt_refresh(
    refresh: Annotated[str, Body(embed=True)],
    command: Annotated[JWTRefreshCommand, Depends(JWTRefreshCommand)],
) -> JWTAccessSchema:
    result = await command.execute(refresh_token=refresh)
    if isinstance(result, PermissionCoreError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    if isinstance(result, AuthenticationFailed):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return JWTAccessSchema(access=result.access)
