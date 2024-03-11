from pydantic import SecretStr

from adapters.api import BaseSchema
from core.domain.auth.dto import JWTCreateDTO


class JWTCreateSchema(BaseSchema):
    email: str
    password: SecretStr

    def to_dto(self) -> JWTCreateDTO:
        return JWTCreateDTO(
            email=self.email,
            password=self.password,
        )


class JWTSchema(BaseSchema):
    access: str
    refresh: str


class JWTAccessSchema(BaseSchema):
    access: str
