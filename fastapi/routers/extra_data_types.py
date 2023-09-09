""" https://fastapi.tiangolo.com/tutorial/extra-data-types """

from uuid import UUID
from datetime import datetime, date, time, timedelta
from typing import Annotated, Union, Optional

from fastapi import APIRouter, Body

extra_dt_router = APIRouter(prefix="/extra_dt", tags=["Extra data types"])


""" Extra Data Types """


@extra_dt_router.put("/items/datetime/{item_id}")
def read_items_datetime(
    item_id: UUID,
    start_datetime: Annotated[Optional[datetime], Body()] = None,
    end_datetime: Annotated[Optional[datetime], Body()] = None,
    repeat_at: Annotated[Optional[time], Body()] = None,
    process_after: Annotated[Optional[timedelta], Body()] = None,
):
    start_process = None
    if start_datetime is not None and process_after is not None:
        start_process = start_datetime + process_after
    duration = None
    if end_datetime is not None and start_process is not None:
        duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
