from logging import Logger
from typing import Callable

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


def get_loger(name: str) -> Callable[[Request], Logger]:
    """
    Функция принимает имя логера и вернёт функцию ожидающую Request.

    :param name: Имя.
    :return: Callable[[Request], Logger].
    """

    def wrapper(request: Request) -> Logger:
        """
        Функция вернёт логер по заранее заданному имени.

        :param request: Request.
        :return: Logger.
        """
        app: CustomFastApi = request.app
        return app.get_logger(name)

    return wrapper
