from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase


class Database:
    """
    Класс работы с БД.
    Инициализирует асинхронный движок SQLAlchemy и фабрику сессий.
    """

    def __init__(self, db_url: str) -> None:
        self.__engine = create_async_engine(db_url)
        self.__async_sessionmaker = async_sessionmaker(
            self.__engine, expire_on_commit=False
        )

    def get_engine(self) -> AsyncEngine:
        """
        Возвращает объект движка базы данных.

        :return: AsyncEngine.
        """
        return self.__engine

    def get_session(self) -> AsyncSession:
        """
        Свойство, возвращающее сессию для работы с БД.

        :return: Сессию для работы с БД.
        """
        return self.__async_sessionmaker()


class Base(DeclarativeBase):
    """
    Базовый класс, от которого наследуются все модели данных.
    """
