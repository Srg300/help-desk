from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class KeycloakSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="keycloak_")

    redirect_uri: str
    server_url: str
    realm_name: str
    client_id: str
    client_secret_key: str
    encoding_algorithm: Literal["RS256"] = "RS256"
