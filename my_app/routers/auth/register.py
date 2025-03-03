from logging import Logger
from typing import Annotated

from core.classes.database import Database
from database.models import User
from fastapi import Body, Depends, HTTPException
from routers.auth.route import auth_router
from routers.schemas.base import BaseSchema
from routers.schemas.user import InUser
from routers.utils import get_database, get_loger
from sqlalchemy import select


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
        f"Попытка создать нового пользователя: "
        f"Имя: {data.firstName}, Фамилия: {data.lastName}, email: {data.email}"
    )

    async with db.get_session() as session:
        user_q = await session.execute(select(User).where(User.email == data.email))
        user_in_bd = user_q.scalars().one_or_none()
        if user_in_bd:
            raise HTTPException(
                status_code=400,
                detail=f"Пользователь c email = {data.email} уже существует",
            )

        user = User(
            first_name=data.firstName,
            last_name=data.lastName,
            email=data.email,
        )
        user.set_password(data.password)
        session.add(user)
        await session.commit()
    loger.info(
        f"Пользователь: Имя: {data.firstName}, Фамилия: {data.lastName}, email: {data.email} - "
        f"успешно создан. Его id: {user.id}"
    )
    return BaseSchema()
