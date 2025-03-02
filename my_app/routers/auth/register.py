from typing import Annotated

from core.classes.database import Database
from core.classes.settings import Settings
from fastapi import Body, Depends
from routers.auth.route import auth_router
from routers.schemas.base import BaseSchema
from routers.schemas.user import InUser
from routers.utils import get_database, get_settings


@auth_router.post(
    "/auth/register",
    response_model=BaseSchema,
    description="Регистрация пользователя.",
    name="Регистрация пользователя.",
)
async def user_registration(
    data: Annotated[InUser, Body(...)],
    db: Annotated[Database, Depends(get_database)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> BaseSchema:
    pass

