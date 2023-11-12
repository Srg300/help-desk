from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from settings import DatabaseSettings, get_settings

_settings = get_settings(DatabaseSettings)


class DBHelper:
    def __init__(self, *, url: str, echo: bool = False) -> None:
        self.async_engine = create_async_engine(
            url=url,
            future=True,
            pool_size=20,
            pool_pre_ping=True,
            pool_use_lifo=True,
            echo=echo,
        )

        self.async_session_factory = async_sessionmaker(
            bind=self.async_engine,
            expire_on_commit=False,
        )


db_helper = DBHelper(
    url=_settings.url,
    echo=_settings.echo,
)
