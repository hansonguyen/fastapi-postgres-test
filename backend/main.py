from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from routers.books import router as books_router
from routers.authors import router as authors_router

import os

# Initialize FastAPI client
description = """
Example API to show base functionality of FastAPI. 🚀
"""

app = FastAPI(
    title="Example API",
    description=description,
    summary="FastAPI Showcase",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Hanson Nguyen",
        "url": "https://hansonn.com/",
    },
)

# Connect to database
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

# All routes are included here
app.include_router(books_router)
app.include_router(authors_router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
