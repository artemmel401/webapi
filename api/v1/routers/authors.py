from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud.models.authors as crud
from api.utils.sockets import notify_clients
from database import get_db
from schemas.authors import AuthorSchema, AuthorSchemaCreate, AuthorSchemaUpdate

router = APIRouter(prefix="/authors", tags=["authors"])


@router.post("/", response_model=AuthorSchema)
async def create_author(author_schema: AuthorSchemaCreate, db: Session = Depends(get_db)):
    author = crud.create_author(db=db, schema=author_schema)
    await notify_clients(f"Author '{author.name}' was created.")
    return author


@router.get("/", response_model=List[AuthorSchema])
async def read_authors(db: Session = Depends(get_db)):
    author = crud.read_authors(db=db)
    return author


@router.get("/", response_model=AuthorSchema)
async def read_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.read_author(db=db, author_id=author_id)
    return author


@router.patch("/", response_model=AuthorSchema)
async def update_author(author_id: int, author_schema: AuthorSchemaUpdate, db: Session = Depends(get_db)):
    author = crud.update_author(db=db, author_id=author_id, schema=author_schema)
    await notify_clients(f"Author '{author.name}' was updated.")
    return author


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.delete_author(db=db, author_id=author_id)
    await notify_clients(f"Author '(ID: {author_id})' was deleted.")
    return author

