from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from models import Book
from models import Author
from schema import Book as SchemaBook
from schema import Author as SchemaAuthor

import os

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/books")
def get_books():
    return db.session.query(Book).all()

@app.get("/authors")
def get_authors():
    return db.session.query(Author).all()

@app.post("/books", response_model=SchemaBook)
def add_book(book: SchemaBook):
    new_book = Book(title=book.title, author_id=book.author_id)
    db.session.add(new_book)
    db.session.commit()
    return new_book


@app.post("/authors", response_model=SchemaAuthor)
def add_author(author: SchemaAuthor):
    new_author = Author(name=author.name, age=author.age)
    db.session.add(new_author)
    db.session.commit()
    return new_author
