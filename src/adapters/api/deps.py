from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from sqlalchemy.ext.asyncio import AsyncSession

from core.domain.user.repository import UserRepository
from db.base.dependencies import get_session
from db.models import User
from settings import AuthSettings, get_settings

from . import UserFromToken, UserRequest
from .exception import (
    credentials_exception,
    user_active_exception,
    user_not_found_exception,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

auth_settings = get_settings(AuthSettings)


async def get_current_user(
    session: Annotated[AsyncSession, Depends(get_session)],
    token: str = Depends(oauth2_scheme),
) -> UserRequest | HTTPException:
    repository = UserRepository(session=session)

    try:
        payload = jwt.decode(
            jwt=token,
            key=auth_settings.secret_key,
            algorithms=[
                auth_settings.algorithm,
            ],
        )

        user_id = payload.get("user_id")

        if user_id is None:
            raise credentials_exception

        token_data = UserFromToken(user_id=user_id)

    except PyJWTError as err:
        raise credentials_exception from err

    user = await repository.get(id_=token_data.user_id)

    if user is None:
        raise user_not_found_exception

    if not user.is_active:
        raise user_active_exception

    return UserRequest(
        id=user.id,
        email=user.email,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
    )


CurrentUser = Annotated[User, Depends(get_current_user)]


def get_superuser(current_user: CurrentUser) -> User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400,
            detail="The user doesn't have enough privileges",
        )
    return current_user
