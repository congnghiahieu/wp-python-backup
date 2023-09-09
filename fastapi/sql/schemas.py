""" https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-pydantic-models """

""" Pydantic models. Sometimes we can call Pydantic models as schemas because it's much more like a validation schemas (like Zod of TS) """

from typing import Optional, List

from pydantic import BaseModel, ConfigDict


class ItemBaseSchema(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreateSchema(ItemBaseSchema):
    pass


class ItemSchema(ItemBaseSchema):
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)


class UserBaseSchema(BaseModel):
    email: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: int
    is_active: bool
    items: List[ItemSchema] = []

    model_config = ConfigDict(from_attributes=True)
