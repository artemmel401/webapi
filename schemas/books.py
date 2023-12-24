from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class BookSchemaBase(BaseModel):
    title: str
    description: str
    publication_date: date
    rating: float = Field(..., ge=0, le=5)
    author_id: int
    genre_id: int


class BookSchemaCreate(BookSchemaBase):
    pass


class BookSchemaUpdate(BookSchemaBase):
    title: Optional[str] = None
    description: Optional[str] = None
    publication_date: Optional[date] = None
    rating: Optional[float] = Field(None, ge=1, le=5)
    author_id: Optional[int] = None
    genre_id: Optional[int] = None


class BookSchema(BookSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
