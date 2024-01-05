from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.domain.role.command import RoleCommand
from core.domain.role.service import RoleService
from db.base.dependencies import get_session

session = Annotated[AsyncSession, Depends(get_session)]


async def role_service(session: session) -> RoleService:
    return RoleService(session=session)


async def role_command(session: session) -> RoleCommand:
    return RoleCommand(session=session)
