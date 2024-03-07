from pydantic import BaseModel

from core.domain.role.dto import RoleCreateDto, RoleUpdateDto


class RoleCreateSchema(RoleCreateDto):
    ...


class RoleUpdateSchema(RoleUpdateDto):
    ...


class RoleResponse(BaseModel):
    id: int
    name: str
    weight: int
