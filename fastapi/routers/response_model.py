""" https://fastapi.tiangolo.com/tutorial/response-model """

from typing import List, Optional

from fastapi import APIRouter, Response
from fastapi.responses import RedirectResponse, JSONResponse
from pydantic import BaseModel, EmailStr

res_models_router = APIRouter(prefix="/response", tags=["Response model"])


""" Response Model - Return Type """

"""
response_model Parameter

There are some cases where you need or want to return some data that is not exactly what the type declares.
In those cases, you can use the path operation decorator parameter response_model instead of the return type.
Có 2 cách để chỉ ra sẽ trả về gì: 1. sử dụng response_model, 2. function return annotation

"""


class ResponseItem(BaseModel):
    name: str
    price: float


@res_models_router.post("/create/item")
def create_item(item: ResponseItem) -> ResponseItem:
    return item


@res_models_router.get("/get/list_of_items", response_model=List[ResponseItem])
def get_list_of_items():
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]


"""
response_model Priority

If you declare both a return type and a response_model, the response_model will take priority and be used by FastAPI.
"""


class UserNoPassword(BaseModel):
    username: str
    email: EmailStr


class UserWithPassword(UserNoPassword):
    password: str


@res_models_router.post("/create/user")
def create_user(user: UserWithPassword) -> UserNoPassword:
    return user


""" Other Return Type Annotations """


""" Return a Response Directly """


@res_models_router.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})


"""Disable Response Model

Continuing from the example above, you might not want to have the default data validation, documentation, filtering, etc. that is performed by FastAPI.
But you might want to still keep the return type annotation in the function to get the support from tools like editors and type checkers (e.g. mypy).

In this case, you can disable the response model generation by setting response_model=None:
"""


@res_models_router.get("/portal/no_res_model", response_model=None)
def get_portal_no_res_model(teleport: bool = False):
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}


""" Response Model encoding parameters 

For example, if you have models with many optional attributes in a NoSQL database, but you don't want to send very long JSON responses full of default values.
(means ignore all default value, in the Item example below we have description, tax, tags that have default value)

Use the response_model_exclude_unset parameter

You can set the path operation decorator parameter response_model_exclude_unset=True and those default values won't be included in the response, only the values actually set.
"""


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@res_models_router.get(
    "/items/{item_id}",
    response_model=Item,
    response_model_exclude_unset=True,
)
def read_item(item_id: str):
    return items[item_id]


""" response_model_include and response_model_exclude """


"""
Response model exclude mode:

There are 4 exclude options:
    - response_model_exclude: Optional[IncEx] = None, : receive a set of key name, those key name will be exclude from original model
    You can use: ["this", "is", "list"] or {"this", "is", "set"} or set(("set", "accept", "tuple"))

    - response_model_exclude_none: bool = False: exclude all key that has None value, still except 0, "", [], {}

    - response_model_exclude_unset: bool = False, : exclude all key that has not been change since defaults.
    Ex: tax: float = 10.5 (has default 10.5) and then you set tax = 10.5 (still equal to default value, but it's not undirty anymore, it's touched by you). So this tax will not be counted as unset, and it will not be excluded

    - response_model_exclude_defaults: bool = False: exclude all key that has value equal to default value.
    Ex: tax: float = 10.5 (has default 10.5) and then you set tax = 10.5 (still equal to default value). So this tax will not be counted as unset, but it still counted as default value, and it will be excluded

Response model include mode:
There is only 1 include options:
    - response_model_include: Optional[IncEx] = None, : receive a set of key name, those key name will be include from original model
    You can use: ["this", "is", "list"] or {"this", "is", "set"} or set(("set", "accept", "tuple"))

"""

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@res_models_router.get(
    "/items/exclude/{item_id}",
    response_model=Item,
    response_model_exclude=set(("tags",)),
)
def read_item_exclude(item_id: str):
    return items[item_id]


@res_models_router.get(
    "/items/include/{item_id}",
    response_model=Item,
    response_model_include=set(("name", "price", "tax")),
    response_model_exclude_unset=True,
)
def read_item_include(item_id: str):
    return items[item_id]
