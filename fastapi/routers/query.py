"""
https://fastapi.tiangolo.com/tutorial/query-params/

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
"""

from typing import Annotated, List

from fastapi import APIRouter, Query

query_router = APIRouter(prefix="/query", tags=["Query"])


"""To define a query, shoud explicitly use Query + Annotated"""


@query_router.get("/items")
def read_items(
    q: Annotated[
        str,
        Query(min_length=3, max_length=50, pattern="^fixedquery$"),
    ] = "fixedquery"
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


"""
Use Query to define additional metadata for OpenAPI, or sign alias

Can accept 1 query field with multiple values like ?q=1&q=2&q=3 by using List
"""


@query_router.get("/multi_items")
def read_multi_items(
    q: Annotated[
        List[str],
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            alias="query-item-alias",
        ),
    ]
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


"""
We can use Query to mark some query variable as deprecated (but still response if user request), or to make that query hidden in OpenAPI
"""


@query_router.get("/deprecated_query")
def deprecated_query(
    q: Annotated[
        str,
        Query(
            include_in_schema=False,
            deprecated=True,
            alias="deprecated-query",
        ),
    ] = ""
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
