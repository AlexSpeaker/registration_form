from pydantic import BaseModel, ConfigDict


class BaseUser(BaseModel):
    pass


class InUser(BaseUser):
    pass


class OutUser(BaseUser):
    id: int

    model_config = ConfigDict(from_attributes=True)
