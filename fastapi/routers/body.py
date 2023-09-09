"""
https://fastapi.tiangolo.com/tutorial/body/

https://fastapi.tiangolo.com/tutorial/body-multiple-params/

https://fastapi.tiangolo.com/tutorial/body-fields/

https://fastapi.tiangolo.com/tutorial/body-nested-models/
"""

from typing import Annotated, Set, List, Optional
from fastapi import APIRouter, Body, Path, Query

from pydantic import BaseModel, Field, HttpUrl

body_router = APIRouter(prefix="/body", tags=["Body"])


class Item(BaseModel):
    name: str
    desc: str = ""
    price: float
    tax: float = 10.0


class User(BaseModel):
    username: str
    age: Optional[int] = None


""" To use Request Body as JSON, use Annotated + Body """


@body_router.post("/create/items")
def create_item(new_item: Annotated[Item, Body()]):
    return new_item


""" Can combine Path + Query + Body (use with Annotated to explicit which kind) """


@body_router.put("/items/{item_id}")
def update_item_combine_path_query_body(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=100_000)],
    q: Annotated[str, Query()] = "",
    item: Annotated[Optional[Item], Body()] = None,
):
    result = {"item_id": item_id, **(item.model_dump() if item is not None else {})}

    if q:
        result.update({"q": q})

    return result


@body_router.patch("/items/{item_id}")
def patch_item(
    item_id: int, item: Annotated[Item, Body()], user: Annotated[User, Body()]
):
    """Multi body request, we will expect a body like this:

    {
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "dave",
            "full_name": "Dave Grohl"
        }
    }

    NOTE: Basically, it still 1 JSON body but contains 2 object
    """

    result = {"item_id": item_id, **item.model_dump(), **user.model_dump()}

    return result


@body_router.patch("/items/singular/{item_id}")
def patch_singular_value_body(
    item_id: int,
    item: Annotated[Item, Body()],
    user: Annotated[User, Body()],
    importance: Annotated[int, Body()],
):
    """In this case, we have Multi body request + singular value body, we will expect a body like this:

    {
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "dave",
            "full_name": "Dave Grohl"
        },
        "importance": 5
    }

    NOTE: Basically, it still 1 JSON body but contains 2 object and 1 key
    """

    result = {
        "item_id": item_id,
        **item.model_dump(),
        **user.model_dump(),
        "importance": importance,
    }

    return result


@body_router.patch("/items/embed/{item_id}")
def patch_embed_body(item_id: int, item: Annotated[Item, Body(embed=True)]):
    """In this case (embed=True), we will have RequestBody as the root object and item as children object, we will expect a request body like this:

    {
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2
        }
    }

    instead of:
    {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }


    NOTE: Basically, it still 1 JSON object but contains another object
    """

    result = {
        "item_id": item_id,
        **item.model_dump(),
    }

    return result


class ItemWithTag(BaseModel):
    """All string in tags will be unique

    With this, even if you receive a request with duplicate data, it will be converted to a set of unique items.

    And whenever you output that data, even if the source had duplicates, it will be output as a set of unique items.
    """

    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: Set[str] = set()


class Image(BaseModel):
    url: str
    name: str


class ItemWithNestedModel(BaseModel):
    """This would mean that FastAPI would expect a body similar to:

    {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2,
        "tags": ["rock", "metal", "bar"],
        "image": {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        }
    }

    """

    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[Image] = None


class ImageWithURL(BaseModel):
    """User Pyndatic HttpURL Validation"""

    url: HttpUrl
    name: str


class ItemWithImageURL(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[ImageWithURL] = None


@body_router.put("/items/single_image_url/{item_id}")
def update_item_single_image(item_id: int, item: ItemWithImageURL):
    results = {"item_id": item_id, "item": item}
    return results


class ItemWithListImageURL(BaseModel):
    """This will expect (convert, validate, document, etc) a JSON body like:

    {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2,
        "tags": [
            "rock",
            "metal",
            "bar"
        ],
        "images": [
            {
                "url": "http://example.com/baz.jpg",
                "name": "The Foo live"
            },
            {
                "url": "http://example.com/dave.jpg",
                "name": "The Baz"
            }
        ]
    }
    """

    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[List[ImageWithURL]] = None


@body_router.put("/items/multi_image_url/{item_id}")
def update_item_list_image(item_id: int, item: ItemWithListImageURL):
    results = {"item_id": item_id, "item": item}
    return results
