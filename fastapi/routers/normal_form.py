"""
https://fastapi.tiangolo.com/tutorial/request-forms/
"""

from typing import Annotated

from fastapi import APIRouter, Form, status

normal_form_router = APIRouter(
    prefix="/normal_form",
    tags=["Form application/x-www-form-urlencoded"],
)


"""
Với Body JSON thông thường, ta chỉ cần định nghĩa 1 Model, rồi sử dụng duy nhất 1 biến (biến là object)
Với Form application/x-www-form-urlencoded, từng trường trong Form là ta phải định nghĩa là 1 biến
"""


@normal_form_router.post(
    "/login",
    status_code=status.HTTP_201_CREATED,
    description="application/x-www-form-urlencoded",
)
def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username, "password": password}
