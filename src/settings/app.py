from collections.abc import Sequence

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="app_")

    allow_origins: Sequence[str] = []
    allow_origin_regex: str | None = None
