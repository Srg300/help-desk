from pydantic import BaseModel, SecretStr

from adapters.api import BaseSchema
from core.domain.auth.dto import JWTCreateDTO


class JWTCreateSchema(BaseModel):
    email: str
    password: SecretStr

    def to_dto(self) -> JWTCreateDTO:
        return JWTCreateDTO(
            email=self.email,
            password=self.password,
        )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "example@example.com",
                    "password": "1234",
                },
            ],
        },
    }


class JWTSchema(BaseSchema):
    access: str
    refresh: str


class JWTAccessSchema(BaseSchema):
    access: str
