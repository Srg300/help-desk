from core.dto import BaseDto


class UserCreateDto(BaseDto):
    email: str
    password: str


class UserSimpleOutDto(BaseDto):
    id: int
    email: str
    username: str
