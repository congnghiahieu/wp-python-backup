""" https://fastapi.tiangolo.com/tutorial/extra-models/ """

from typing import Annotated, Union

from fastapi import APIRouter, Body
from pydantic import BaseModel, EmailStr

extra_res_models_router = APIRouter(
    prefix="/extra_res_models", tags=["Extra Response Models"]
)

""" This is especially the case for user models, because:

The input model needs to be able to have a password.
The output model should not have a password.
The database model would probably need to have a hashed password. """


class BaseUser(BaseModel):
    username: str
    email: EmailStr


class UserIn(BaseUser):
    password: str


class UserOut(BaseUser):
    pass


class UserInDB(BaseUser):
    hashed_password: str


def fake_hash_pwd(raw_pwd: str):
    return f"salt-{raw_pwd}"


def fake_save_user_in_DB(user: UserIn):
    hashed_pwd = fake_hash_pwd(user.password)
    user_in_db = UserInDB(**user.model_dump(), hashed_password=hashed_pwd)
    return user_in_db


@extra_res_models_router.post("", response_model=UserOut)
def create_user_in_DB(user: Annotated[UserIn, Body()]):
    user_saved = fake_save_user_in_DB(user)
    return user_saved


""" Union and anyOf """


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str = "car"


class PlaneItem(BaseItem):
    type: str = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@extra_res_models_router.get(
    "/items/{item_id}", response_model=Union[PlaneItem, CarItem]
)
async def read_item(item_id: str):
    return items[item_id]
