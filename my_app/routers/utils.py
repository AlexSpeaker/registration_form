from core.classes.app import CustomFastApi
from core.classes.database import Database
from core.classes.settings import Settings
from fastapi import Request


def get_database(request: Request) -> Database:
    """
    Возвращает инструмент работы с ДБ.

    :param request: Request.
    :return: Database.
    """
    app: CustomFastApi = request.app
    return app.get_db()


def get_settings(request: Request) -> Settings:
    """
    Возвращает настройки приложения.

    :param request: Request.
    :return: Settings.
    """
    app: CustomFastApi = request.app
    return app.get_settings()
