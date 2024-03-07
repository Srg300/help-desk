from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
