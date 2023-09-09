""" https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies """

from typing import Annotated, Dict


from fastapi import APIRouter, Depends, Query

class_deps_router = APIRouter(
    prefix="/class_deps", tags=["Class as Dependencies Injection"]
)

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(
        self, q: Annotated[str, Query()] = "", skip: int = 0, limit: int = 100
    ) -> None:
        self.q = q
        self.skip = skip
        self.limit = limit


@class_deps_router.get("/items")
def read_items(common_params: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    response = {}
    if common_params.q:
        response.update({"q": common_params.q})
    items = fake_items_db[common_params.skip : common_params.skip + common_params.limit]
    response.update({"items": items})
    return response
