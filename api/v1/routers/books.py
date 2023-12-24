from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud.models.books as crud
from api.utils.sockets import notify_clients
from database import get_db
from schemas.books import BookSchema, BookSchemaCreate, BookSchemaUpdate

router = APIRouter(prefix="/books", tags=["books"])


@router.post("/", response_model=BookSchema)
async def create_book(book_schema: BookSchemaCreate, db: Session = Depends(get_db)):
    book = crud.create_book(db=db, schema=book_schema)
    await notify_clients(f"Book '{book.title} (ID: {book.id}; Genre: {book.genre.name}, Author: {book.author.name})' "
                         f"was created.")
    return book


@router.get("/", response_model=List[BookSchema])
async def read_books(db: Session = Depends(get_db)):
    book = crud.read_books(db=db)
    return book


@router.get("/", response_model=BookSchema)
async def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.read_book(db=db, book_id=book_id)
    return book


@router.patch("/", response_model=BookSchema)
async def update_book(book_id: int, book_schema: BookSchemaUpdate, db: Session = Depends(get_db)):
    book = crud.update_book(db=db, book_id=book_id, schema=book_schema)
    await notify_clients(f"Book '{book.title} (ID: {book.id}; Genre: {book.genre.name}, Author: {book.author.name})' "
                         f"was updated.")
    return book


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db=db, book_id=book_id)
    await notify_clients(f"Book '(ID: {book_id})' was deleted.")
    return book

