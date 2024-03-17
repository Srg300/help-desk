from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )


class UserFromToken(BaseModel):
    user_id: int | None = None


class UserRequest(BaseModel):
    id: int
    email: str
    is_superuser: bool
    is_active: bool
