from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.domain.auth.dto import AuthTokensDTO, JWTCreateDTO, RefreshTokenDTO
from core.domain.auth.service import AuthService, JWTService
from core.domain.user.repository import UserRepository
from core.errors import AuthenticationFailed, PermissionCoreError
from db.base.dependencies import get_session


class JWTCreateCommand:
    def __init__(
        self,
        auth_service: Annotated[AuthService, Depends(AuthService)],
    ) -> None:
        self._auth_service = auth_service

    async def execute(
        self,
        dto: JWTCreateDTO,
    ) -> AuthTokensDTO | AuthenticationFailed:
        user = await self._auth_service.authenticate(
            email=dto.email,
            password=dto.password.get_secret_value(),
        )
        if isinstance(user, AuthenticationFailed):
            return user
        return await self._auth_service.tokens(user=user)


class JWTRefreshCommand:
    def __init__(
        self,
        session: Annotated[AsyncSession, Depends(get_session)],
        auth_service: Annotated[AuthService, Depends(AuthService)],
        jwt_service: Annotated[JWTService, Depends(JWTService)],
    ) -> None:
        self._session = session
        self._repository = UserRepository(session=self._session)
        self._auth_service = auth_service
        self._jwt_service = jwt_service

    async def execute(
        self,
        refresh_token: str,
    ) -> AuthTokensDTO | AuthenticationFailed | PermissionCoreError:
        claims = self._jwt_service.decode(token=refresh_token, model=RefreshTokenDTO)
        if isinstance(claims, AuthenticationFailed):
            return AuthenticationFailed()

        user = await self._repository.get(id_=claims.user_id)
        if not user:
            return PermissionCoreError()
        return await self._auth_service.tokens(user=user)
