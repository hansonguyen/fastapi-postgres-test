from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from routers.books import router as books_router
from routers.authors import router as authors_router

import os

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

app.include_router(books_router)
app.include_router(authors_router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
