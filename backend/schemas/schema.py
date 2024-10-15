"""
Type schemas for database models.

Main types for abstract database objects are defined here. This is used for type validation.

Typical usage example:

	from schemas.schema import Book as SchemaBook
    from models.db import Book
    
    def add_book(book: SchemaBook):
		new_book = Book(title=book.title, author_id=book.author_id)
		db.session.add(new_book)
		db.session.commit()
		return new_book
"""

from pydantic import BaseModel
import uuid


class Book(BaseModel):
    title: str
    author_id: uuid.UUID

    class Config:
        orm_mode = True


class Author(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True
