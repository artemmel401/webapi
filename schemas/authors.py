from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AuthorSchemaBase(BaseModel):
    name: str


class AuthorSchemaCreate(AuthorSchemaBase):
    pass


class AuthorSchemaUpdate(AuthorSchemaBase):
    name: Optional[str] = None


class AuthorSchema(AuthorSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
