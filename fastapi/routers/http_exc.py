""" https://fastapi.tiangolo.com/tutorial/handling-errors """

from typing import Annotated

from fastapi import APIRouter, HTTPException, Request, Path, status
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import (
    request_validation_exception_handler,
    http_exception_handler,
)

http_exc_router = APIRouter(prefix="/http_exc", tags=["HTTP Exception"])


@http_exc_router.get("/items/{item_id}")
def read_item(item_id: Annotated[str, Path()]):
    items = {"foo": "The Foo Wrestlers"}
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
            headers={"X-Error-Header": "Response Header"},
        )

    return {"item": items[item_id]}


"""
Install custom exception handlers

See for more details: https://fastapi.tiangolo.com/tutorial/handling-errors/#install-custom-exception-handlers
"""

"""
Override the default exception handlers

See for more details: https://fastapi.tiangolo.com/tutorial/handling-errors/#override-the-default-exception-handlers
"""
