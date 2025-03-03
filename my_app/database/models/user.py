from database.models.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash

MAX_NAME_LENGTH = 50
MAX_EMAIL_LENGTH = 100
MAX_PASSWORD_LENGTH = 512


class User(Base):
    """
    Пользователь.

    **id** ID пользователя. \n
    **first_name** Имя пользователя. \n
    **last_name** Фамилия пользователя. \n
    **email** Email пользователя (уникальный). \n
    **password** Хеш пароля пользователя.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(MAX_NAME_LENGTH), nullable=False)
    last_name: Mapped[str] = mapped_column(String(MAX_NAME_LENGTH), nullable=False)
    email: Mapped[str] = mapped_column(
        String(MAX_EMAIL_LENGTH), unique=True, nullable=False
    )
    password: Mapped[str] = mapped_column(String(MAX_PASSWORD_LENGTH), nullable=False)

    def set_password(self, password: str) -> None:
        """
        Устанавливает хеш пароля для пользователя.
        """
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        Проверяет, совпадает ли переданный пароль с хешем пароля пользователя.
        """
        return check_password_hash(self.password, password)
