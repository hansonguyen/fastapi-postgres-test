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
