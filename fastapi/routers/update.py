""" https://fastapi.tiangolo.com/tutorial/body-updates """

from typing import Optional, List, Annotated

from fastapi import APIRouter, Path, Body, status
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

update_router = APIRouter(prefix="/update", tags=["Body updates"])

""" Update replacing with PUT """


class Item(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: float = 10.5
    tags: List[str] = []


class CreateItem(Item):
    name: str
    description: str
    price: float


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@update_router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: Annotated[str, Path()]):
    if item_id not in items.keys():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found"
        )

    return items[item_id]


@update_router.post("/items", response_model=Item)
def create_item(item: Annotated[CreateItem, Body()]):
    items["dummy"] = jsonable_encoder(item)
    return item


@update_router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: Annotated[str, Path()], item: Annotated[Item, Body()]):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


""" Partial updates with PATCH """

""" Using Pydantic's exclude_unset parameter & Using Pydantic's update parameter """


@update_router.patch("/items/{item_id}", response_model=Item)
async def patch_item(item_id: Annotated[str, Path()], item: Annotated[Item, Body()]):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)

    update_data = item.model_dump(exclude_unset=True)
    updated_item = stored_item_model.model_copy(update=update_data)

    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
