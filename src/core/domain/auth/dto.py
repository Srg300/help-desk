import dataclasses
from typing import Literal

from pydantic import BaseModel, SecretStr


class JWTCreateDTO(BaseModel):
    email: str
    password: SecretStr


@dataclasses.dataclass(slots=True, frozen=True)
class AuthTokensDTO:
    access: str
    refresh: str


class _TokenBase(BaseModel):
    exp: int
    user_id: int
    email: str
    username: str


class AccessTokenDTO(_TokenBase):
    token_type: Literal["access"]


class RefreshTokenDTO(_TokenBase):
    token_type: Literal["refresh"]
