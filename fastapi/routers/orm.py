from typing import Annotated, List

from fastapi import APIRouter, HTTPException, Depends, Body, Query, Path, status
from sqlalchemy.orm import Session

from sql import crud, models, schemas
from sql.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


orm_router = APIRouter(prefix="/orm", tags=["SQLAlchemy ORM"])


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Type alias for Database session dependencies
dbDeps = Annotated[Session, Depends(get_db)]


@orm_router.post("/users", response_model=schemas.UserSchema)
def create_users(
    db: dbDeps,
    user: Annotated[schemas.UserCreateSchema, Body()],
):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email already regiesterd"
        )
    new_user = crud.create_user(db, user)
    return new_user


@orm_router.get("/users", response_model=List[schemas.UserSchema])
def read_users(
    db: dbDeps,
    skip: Annotated[int, Query()] = 0,
    limit: Annotated[int, Query()] = 100,
):
    users = crud.get_users(db, skip, limit)
    return users


@orm_router.get("/user/{user_id}", response_model=schemas.UserSchema)
def read_user(db: dbDeps, user_id: Annotated[int, Path()]):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return db_user


@orm_router.post("/user/{user_id}/items", response_model=schemas.ItemSchema)
def create_item_for_user(
    db: dbDeps,
    user_id: Annotated[int, Path()],
    item: Annotated[schemas.ItemCreateSchema, Body()],
):
    return crud.create_user_item(db, item, user_id)


@orm_router.get("/items", response_model=List[schemas.ItemSchema])
def read_items(
    db: dbDeps,
    skip: Annotated[int, Query()] = 0,
    limit: Annotated[int, Query()] = 100,
):
    items = crud.get_items(db, skip, limit)
    return items
