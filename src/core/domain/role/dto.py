from core.dto import BaseDto


class RoleCreateDto(BaseDto):
    name: str
    weight: int
