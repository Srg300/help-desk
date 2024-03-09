from pydantic import BaseModel

from core.domain.user.dto import UserCreateDto


class UserCreateSchema(BaseModel):
    email: str
    password: str

    def to_dto(self) -> UserCreateDto:
        return UserCreateDto(
            email=self.email,
            password=self.password,
            username=self.email.split("@")[0],
        )


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
