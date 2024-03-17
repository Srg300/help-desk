from pydantic import BaseModel

from core.domain.role.dto import RoleCreateDto, RoleUpdateDto


class RoleCreateSchema(RoleCreateDto):
    name: str
    weight: int


class RoleUpdateSchema(RoleUpdateDto):
    name: str
    weight: int


class RoleResponse(BaseModel):
    id: int
    name: str
    weight: int
