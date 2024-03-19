from pydantic import BaseModel

from core.domain.role.dto import RoleCreateDto, RoleUpdateDto


class RoleCreateSchema(RoleCreateDto):
    name: str
    weight: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Some role name",
                    "weight": 100,
                }
            ]
        }
    }

class RoleUpdateSchema(RoleUpdateDto):
    name: str
    weight: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Some role name",
                    "weight": 100,
                }
            ]
        }
    }

class RoleResponse(BaseModel):
    id: int
    name: str
    weight: int
