import time

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from typing_extensions import deprecated

from routers.query import query_router
from routers.path import path_router
from routers.body import body_router
from routers.extra_data_types import extra_dt_router
from routers.req_example_data import req_ex_data_router
from routers.header import header_router
from routers.response_model import res_models_router
from routers.extra_response_models import extra_res_models_router
from routers.response_status_code import res_status_code_router
from routers.normal_form import normal_form_router
from routers.multipart_form import multipart_form_router
from routers.http_exc import http_exc_router
from routers.update import update_router
from routers.deps.basic_deps import basic_deps_router
from routers.deps.class_deps import class_deps_router
from routers.deps.sub_deps import sub_deps_router
from routers.deps.path_deps import path_deps_router
from routers.deps.yield_deps import yield_deps_router
from routers.security import security_router
from routers.orm import orm_router

app = FastAPI()

""" Middleware: https://fastapi.tiangolo.com/tutorial/middleware """


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response: Response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-time"] = str(process_time)
    return response


""" CORS (Cross-Origin Resource Sharing): https://fastapi.tiangolo.com/tutorial/cors """
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:4173",
        "http://localhost:5173",
        "https://www.google.com",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/")
def root():
    return {"message": "Hello"}


@app.get("/users/me")
def read_user_me():
    return {"user_id": "The current user"}


app.include_router(query_router)
app.include_router(path_router)
app.include_router(body_router)
app.include_router(extra_dt_router)
app.include_router(req_ex_data_router)
app.include_router(header_router)
app.include_router(res_models_router)
app.include_router(extra_res_models_router)
app.include_router(res_status_code_router)
app.include_router(normal_form_router)
app.include_router(multipart_form_router)
app.include_router(http_exc_router)
app.include_router(update_router)
app.include_router(basic_deps_router)
app.include_router(class_deps_router)
app.include_router(sub_deps_router)
app.include_router(path_deps_router)
app.include_router(yield_deps_router)
app.include_router(security_router)
app.include_router(orm_router)
