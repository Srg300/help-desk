from collections.abc import Sequence
from datetime import timedelta
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class AuthSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="auth_")

    secret_key: str
    algorithm: Literal["HS256"] = "HS256"

    jwt_access_lifetime: timedelta = timedelta(minutes=30)
    jwt_refresh_lifetime: timedelta = timedelta(days=30)


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="app_")

    allow_origins: Sequence[str] = []
    allow_origin_regex: str | None = None
