import crud.base as crud
from sqlalchemy.orm import Session
from models import Book
from schemas.books import BookSchemaBase


def create_book(db: Session, schema: BookSchemaBase):
    book = crud.create_object(db=db, model=Book, schema=schema)
    return book


def read_book(db: Session, book_id: int):
    book = crud.get_object_by_id(db=db, model=Book, obj_id=book_id)
    return book


def read_books(db: Session, offset: int = 0, limit: int = 10):
    books = crud.get_all_objects(db=db, model=Book, offset=offset, limit=limit)
    return books


def update_book(db: Session, book_id: int, schema: BookSchemaBase):
    book = crud.update_object(db=db, obj_id=book_id, model=Book, schema=schema)
    return book


def delete_book(db: Session, book_id: int):
    crud.delete_object(db=db, obj_id=book_id, model=Book)
    return True
