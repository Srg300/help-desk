from adapters.api import BaseSchema


class RoleCreateSchema(BaseSchema):
    name: str
    weight: int


class RoleResponse(BaseSchema):
    id: int
    name: str
    weight: int
