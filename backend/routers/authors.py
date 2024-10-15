"""
Router that contains all routes with prefix `/authors`.
"""

from fastapi import APIRouter
from fastapi_sqlalchemy import db
from models.db import Author
from schemas.schema import Author as SchemaAuthor

router = APIRouter(
    prefix="/authors", tags=["authors"], responses={404: {"description": "Not found"}}
)


@router.get("/")
def get_authors():
    return db.session.query(Author).all()


@router.post("/", response_model=SchemaAuthor)
def add_author(author: SchemaAuthor):
    new_author = Author(name=author.name, age=author.age)
    db.session.add(new_author)
    db.session.commit()
    return new_author
