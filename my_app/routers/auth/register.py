from logging import Logger
from typing import Annotated

from core.classes.database import Database
from database.models import User
from fastapi import Body, Depends
from routers.auth.route import auth_router
from routers.schemas.base import BaseSchema
from routers.schemas.user import InUser
from routers.utils import get_database, get_loger


@auth_router.post(
    "/auth/register",
    response_model=BaseSchema,
    description="Регистрация нового пользователя.",
    name="Регистрация пользователя.",
)
async def user_registration(
    data: Annotated[InUser, Body(...)],
    db: Annotated[Database, Depends(get_database)],
    loger: Annotated[Logger, Depends(get_loger("user_registration"))],
) -> BaseSchema:
    """
    Регистрация нового пользователя.

    :param data: Данные пользователя.
    :param db: Инструмент для работы с БД.
    :param loger: Логер функции user_registration.
    :return: BaseSchema.
    """
    loger.info(
        f"Попытка создать нового пользователя: Имя: {data.firstName}, Фамилия: {data.lastName}"
    )
    user = User(
        first_name=data.firstName,
        last_name=data.lastName,
        email=data.email,
    )
    user.set_password(data.password)
    async with db.get_session() as session:
        session.add(user)
        await session.commit()
    loger.info(
        f"Пользователь: Имя: {data.firstName}, Фамилия: {data.lastName} - успешно создан. Его id: {user.id}"
    )
    return BaseSchema()
