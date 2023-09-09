""" https://fastapi.tiangolo.com/tutorial/dependencies """

from typing import Annotated, Dict


from fastapi import APIRouter, Depends, Query

basic_deps_router = APIRouter(
    prefix="/basic_deps", tags=["Basic Dependencies Injection"]
)


def common_params(
    q: Annotated[str, Query(min_length=1, alias="query")],
    skip: int = 0,
    limit: int = 100,
):
    return {"q": q, "skip": skip, "limit": limit}


# type alias
CommonDeps = Annotated[Dict[str, str | int], Depends(common_params)]


@basic_deps_router.get("/items")
def read_items(common_params: CommonDeps):
    return common_params


@basic_deps_router.get("/users")
def read_users(common_params: CommonDeps):
    return common_params
