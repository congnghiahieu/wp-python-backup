""" https://fastapi.tiangolo.com/tutorial/response-status-code/ """

from fastapi import APIRouter, status

res_status_code_router = APIRouter(
    prefix="/res_status_code", tags=["Response status code"]
)


@res_status_code_router.post("", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
