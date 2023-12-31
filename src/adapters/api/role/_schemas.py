from adapters.api import BaseSchema
from core.domain.role.dto import RoleCreateDto, RoleUpdateDto


class RoleCreateSchema(RoleCreateDto):
    ...


class RoleUpdateSchema(RoleUpdateDto):
    ...


class RoleResponse(BaseSchema):
    id: int
    name: str
    weight: int
