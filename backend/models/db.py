"""
Database models that are used to query the database or create objects.

Typical usage example:

	from models.db import Book
    
    def get_books():
    	return db.session.query(Book).all()

	def add_book(book: SchemaBook):
		new_book = Book(title=book.title, author_id=book.author_id)
		db.session.add(new_book)
		db.session.commit()
		return new_book
"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

Base = declarative_base()


class Book(Base):
    __tablename__ = "book"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    author_id = Column(UUID, ForeignKey("author.id"))

    author = relationship("Author")


class Author(Base):
    __tablename__ = "author"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    age = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
