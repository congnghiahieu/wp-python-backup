""" https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/ """

from typing import Annotated

from fastapi import APIRouter, Depends, Query, Cookie

sub_deps_router = APIRouter(
    prefix="/sub_deps",
    tags=["Sub-dependencies Injection"],
)


def query_extractor(q: Annotated[str, Query()] = ""):
    print(f"Query Extractor: {q}")
    return q


def cookie_extractor(ssid: Annotated[str, Cookie()]):
    print(f"Cookie Extractor: {ssid}")
    return ssid


def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    ssid: Annotated[str, Depends(cookie_extractor)],
):
    if not q:
        return ssid
    return q


@sub_deps_router.get("/items")
def read_query_or_cookie(q_o_c: Annotated[str, Depends(query_or_cookie_extractor)]):
    return {"query_or_cookie": q_o_c}
