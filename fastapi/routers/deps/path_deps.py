""" https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/ """

from typing import Annotated

from fastapi import APIRouter, Depends, Cookie, Header, status
from fastapi.exceptions import HTTPException

path_deps_router = APIRouter(
    prefix="/path_deps",
    tags=["Dependencies in path operation decorators"],
)

""" In some cases you don't really need the return value of a dependency inside your path operation function.

Or the dependency doesn't return a value.

But you still need it to be executed/solved.

For those cases, instead of declaring a path operation function parameter with Depends, you can add a list of dependencies to the path operation decorator. """

""" Add dependencies to the path operation decorator """


def verify_ssid(ssid: Annotated[str, Cookie()] = ""):
    if not ssid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized session"
        )


def verify_header(authorization: Annotated[str, Header()] = ""):
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized token"
        )


@path_deps_router.get(
    "/items", dependencies=[Depends(verify_ssid), Depends(verify_header)]
)
def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
