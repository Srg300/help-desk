from core.dto import BaseDto


class RoleCreateDto(BaseDto):
    name: str
    weight: int


class RoleUpdateDto(BaseDto):
    name: str | None = None
    weight: int | None = None
