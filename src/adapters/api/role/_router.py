from typing import Annotated

from fastapi import APIRouter, Depends, status

from ._schemas import RoleCreateSchema, RoleResponse
from core.domain.role.repository import RoleRepository
from core.domain.role.dto import RoleCreateDto
from db.base.engine import db_helper


router = APIRouter(
    tags=["roles"],
    prefix="/roles",
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_role(
    schema: RoleCreateSchema,
) -> RoleResponse:
    #FIXME  временно прокидываем сессию в api
    session = db_helper.async_session_factory()
    #FIXME  объявляем репозиторий и прокидываем туда сессию
    repository = RoleRepository(session=session)
    
    obj = await repository.create(
        dto=RoleCreateDto(
            name=schema.name,
            weight=schema.weight,
        )
    )
    return RoleResponse.model_validate(obj)
