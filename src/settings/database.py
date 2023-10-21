from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="database_")

    driver: str = "postgresql+asyncpg"
    name: str
    username: str
    password: SecretStr
    host: str
    port: int = 5432

    echo: bool = False

    @property
    def url(self) -> str:
        return URL.create(
            drivername=self.driver,
            username=self.username,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.name,
        ).render_as_string(hide_password=False)
