"""
https://fastapi.tiangolo.com/tutorial/path-params/

https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
"""

from typing import Annotated
from enum import Enum

from fastapi import APIRouter, Path, Query


path_router = APIRouter(prefix="/path", tags=["Path"])


@path_router.get("/users/{user_id}")
def read_user(user_id: str):
    """Example of path parameter"""
    return {"user_id": user_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@path_router.get("/models/{model_name}")
def get_model(model_name: ModelName):
    """Use enum value

    To use Enum value for path, query, body (singular value body), declare to class inherit str and Enum:

    class Example(str, Enum):
        ...

    Will receive an enum instance

    """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@path_router.get("/files/{file_path:path}")
def read_file(file_path: str):
    """To define * wild/card path (a path contains multiple path). Ex: file_path = '/home/user/dataverse/...'"""
    return {"file_path": file_path}


""" Path + Query, use Annotated """


@path_router.get("/items/{item_id}")
def read_item(
    item_id: Annotated[
        int,
        Path(
            gt=0,
            lt=100_000,
            title="Item ID to get",
            description="Item ID need to be an integer",
        ),
    ],
    size: Annotated[float, Query(gt=1.5, lt=10.5)],
    q: str = "",
    short: bool = False,
):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "size": size,
                "description": "This is an amazing item that has a long description",
            }
        )
    return item


"""Multiple path parameter"""


@path_router.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: str, q: str = "", short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
