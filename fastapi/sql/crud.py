from sqlalchemy.orm import Session
from sql import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.UserModel).filter(models.UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.UserModel).filter(models.UserModel.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreateSchema):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.UserModel(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ItemModel).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreateSchema, user_id: int):
    db_item = models.ItemModel(**item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
