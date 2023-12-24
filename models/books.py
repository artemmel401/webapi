from datetime import datetime, date
from sqlalchemy import ForeignKey, DateTime, func, String, Integer, Float, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True, unique=True)
    description: Mapped[str] = mapped_column(String)

    publication_date: Mapped[date] = mapped_column(Date)
    rating: Mapped[float] = mapped_column(Float)

    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="books", lazy="selectin")

    genre_id: Mapped[int] = mapped_column(Integer, ForeignKey("genres.id"))
    genre: Mapped["Genre"] = relationship(back_populates="books", lazy="selectin")

    created_at = mapped_column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())
