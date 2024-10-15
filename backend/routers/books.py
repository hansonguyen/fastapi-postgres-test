from fastapi import APIRouter
from fastapi_sqlalchemy import db
from models.db import Book
from schemas.schema import Book as SchemaBook

router = APIRouter(
    prefix="/books", tags=["books"], responses={404: {"description": "Not found"}}
)


@router.get("/")
def get_books():
    return db.session.query(Book).all()


@router.post("/", response_model=SchemaBook)
def add_book(book: SchemaBook):
    new_book = Book(title=book.title, author_id=book.author_id)
    db.session.add(new_book)
    db.session.commit()
    return new_book
