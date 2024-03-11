from datetime import datetime, timezone
from typing import Annotated, Any, TypeVar

import jwt
import pydantic
from fastapi import Depends
from pydantic import BaseModel

from core.domain.auth.dto import AccessTokenDTO, AuthTokensDTO
from core.domain.user.service import UserService
from core.errors import AuthenticationFailed
from core.security import verify_password
from db.models import User
from settings import AuthSettings, get_settings

_settings = get_settings(AuthSettings)

_TBaseModel = TypeVar("_TBaseModel", bound=BaseModel)


class JWTService:
    def encode(self, payload: dict[str, Any]) -> str:
        return jwt.encode(
            payload=payload,
            key=_settings.secret_key,
            algorithm=_settings.algorithm,
        )

    def decode(
        self,
        token: str,
        model: type[_TBaseModel],
    ) -> _TBaseModel | AuthenticationFailed:
        try:
            payload = jwt.decode(
                jwt=token,
                key=_settings.secret_key,
                algorithms=[_settings.algorithm],
            )
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return AuthenticationFailed()

        try:
            dto = model.model_validate(payload)
        except pydantic.ValidationError:
            return AuthenticationFailed()

        return dto


class AuthService:
    def __init__(
        self,
        service: Annotated[UserService, Depends(UserService)],
        jwt_service: Annotated[JWTService, Depends(JWTService)],
    ) -> None:
        self._service = service
        self._jwt_service = jwt_service

    async def authenticate(
        self,
        email: str,
        password: str,
    ) -> User | AuthenticationFailed:
        user = await self._service.get_by_email(email=email)

        if user is None:
            return AuthenticationFailed()

        verify = verify_password(
            plain_password=password,
            hashed_password=user.hashed_password,
        )
        if not verify:
            return AuthenticationFailed()

        return user

    def _access_token_dto(
        self,
        user: User,
        now: datetime,
    ) -> AccessTokenDTO:
        return AccessTokenDTO(
            token_type="access",  # noqa: S106
            exp=int((now + _settings.jwt_access_lifetime).timestamp()),
            user_id=user.id,
            email=user.email,
            username=user.username,
        )

    async def tokens(self, user: User) -> AuthTokensDTO:
        now = datetime.now(tz=timezone.utc)
        access_dto = self._access_token_dto(user=user, now=now)

        payload = access_dto.model_dump()

        return AuthTokensDTO(
            access=self._jwt_service.encode(payload=payload),
            refresh=self._jwt_service.encode(
                payload=payload
                | {
                    "token_type": "refresh",
                    "exp": int((now + _settings.jwt_refresh_lifetime).timestamp()),
                },
            ),
        )
