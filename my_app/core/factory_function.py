from typing import Any, Sequence

from core.classes.app import CustomFastApi
from core.classes.database import Database
from core.classes.settings import Settings
from core.exception_handlers import exception_handler, http_exception_handler
from core.lifespan import lifespan_func
from fastapi import APIRouter, HTTPException
from fastapi.staticfiles import StaticFiles


def get_app(
    *args: Any,
    settings: Settings,
    routers_sequence: Sequence[APIRouter],
    **kwargs: Any,
) -> CustomFastApi:
    """
    Функция базово настраивает FastAPI и возвращает приложение.

    :param args: Дополнительные аргументы FastAPI.
    :param settings: Настройки приложения.
    :param routers_sequence: Последовательность из подключаемых роутерах.
    :param kwargs: Дополнительные именованные аргументы FastAPI.
    :return: Приложение (CustomFastApi).
    """
    db = Database(db_url=settings.DB_SETTINGS.DATABASE_URL)
    app = CustomFastApi(
        *args, db=db, settings=settings, lifespan=lifespan_func, **kwargs
    )
    app.add_exception_handler(Exception, exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    for router in routers_sequence:
        app.include_router(router=router, prefix="/api")
    if settings.DEBUG:
        app.mount(
            settings.MEDIA_URL,
            StaticFiles(directory=settings.MEDIA_FOLDER_ROOT),
            name="media",
        )
        app.mount(
            settings.STATIC_URL,
            StaticFiles(directory=settings.STATIC_ROOT, html=True),
            name="static",
        )
    return app
