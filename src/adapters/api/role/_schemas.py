from pydantic import BaseModel


class RoleCreateSchema(BaseModel):
    name: str
    weight: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Some role name",
                    "weight": 100,
                },
            ],
        },
    }


class RoleUpdateSchema(BaseModel):
    name: str
    weight: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Some role name",
                    "weight": 100,
                },
            ],
        },
    }


class RoleResponse(BaseModel):
    id: int
    name: str
    weight: int
