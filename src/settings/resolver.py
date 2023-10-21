import functools
from typing import TypeVar

from pydantic_settings import BaseSettings

TSettings = TypeVar("TSettings", bound=BaseSettings)


def get_settings(cls: type[TSettings]) -> TSettings:
    return cls()


get_settings = functools.cache(get_settings)  # Mypy moment
