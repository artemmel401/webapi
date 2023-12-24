import crud.base as crud
from sqlalchemy.orm import Session
from models import Author
from schemas.authors import AuthorSchemaBase


def create_author(db: Session, schema: AuthorSchemaBase):
    author = crud.create_object(db=db, model=Author, schema=schema)
    return author


def read_author(db: Session, author_id: int):
    author = crud.get_object_by_id(db=db, model=Author, obj_id=author_id)
    return author


def read_authors(db: Session, offset: int = 0, limit: int = 10):
    authors = crud.get_all_objects(db=db, model=Author, offset=offset, limit=limit)
    return authors


def update_author(db: Session, author_id: int, schema: AuthorSchemaBase):
    author = crud.update_object(db=db, obj_id=author_id, model=Author, schema=schema)
    return author


def delete_author(db: Session, author_id: int):
    crud.delete_object(db=db, obj_id=author_id, model=Author)
    return True
