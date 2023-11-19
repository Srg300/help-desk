from collections.abc import Sequence
from typing import Any, Self

from pydantic import BaseModel, ConfigDict


class BaseDto(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )

    @classmethod
    def model_validate_list(cls, objs: Sequence[Any]) -> list[Self]:
        return [cls.model_validate(obj) for obj in objs]
