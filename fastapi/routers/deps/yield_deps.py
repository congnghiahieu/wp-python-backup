""" https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/ """

from typing import Annotated

from fastapi import APIRouter, Depends, Query, Cookie

yield_deps_router = APIRouter(
    prefix="/yield_deps",
    tags=["Dependencies Injection with yield"],
)

""" A database dependency with yield """
