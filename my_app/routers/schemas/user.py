from database.models.user import MAX_EMAIL_LENGTH, MAX_NAME_LENGTH, MAX_PASSWORD_LENGTH
from pydantic import BaseModel, ConfigDict, EmailStr, Field, computed_field


class InUser(BaseModel):
    firstName: str = Field(..., max_length=MAX_NAME_LENGTH, exclude=True)
    lastName: str = Field(..., max_length=MAX_NAME_LENGTH, exclude=True)
    email: EmailStr = Field(..., max_length=MAX_EMAIL_LENGTH, exclude=True)
    password: str = Field(..., max_length=MAX_PASSWORD_LENGTH, exclude=True)


class OutUser(BaseModel):
    id: int
    first_name: str = Field(..., exclude=True)
    last_name: str = Field(..., exclude=True)
    email: EmailStr

    @computed_field
    def firstName(self) -> str:
        return self.first_name

    @computed_field
    def lastName(self) -> str:
        return self.last_name

    model_config = ConfigDict(from_attributes=True)
