""" https://fastapi.tiangolo.com/tutorial/schema-extra-example/ """

from typing import Optional, Annotated

from fastapi import APIRouter, Body
from pydantic import BaseModel, Field

req_ex_data_router = APIRouter(
    prefix="/req_ex_data", tags=["Request with example data"]
)

""" Declare Request Example Data """


class ItemWithJSONSchemaExtra(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


class ItemWithFieldExtra(BaseModel):
    name: str = Field(examples=["Foo"])
    description: Optional[str] = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: Optional[float] = Field(default=None, examples=[3.2])


@req_ex_data_router.post("")
def request_with_example_data(
    item: Annotated[ItemWithFieldExtra, Body()]
) -> ItemWithFieldExtra:
    return item
