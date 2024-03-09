from pydantic import EmailStr, computed_field

from core.dto import BaseDto
from core.security import get_password_hash


class UserCreateDto(BaseDto):
    email: EmailStr
    password: str
    username: str

    @property
    @computed_field
    def hashed_password(self) -> str:
        return get_password_hash(password=self.password)  # type: ignore[no-any-return]


class UserSimpleOutDto(BaseDto):
    id: int
    email: str
    username: str
