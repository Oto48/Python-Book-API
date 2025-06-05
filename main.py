from fastapi import FastAPI
from typing import List
from models import Book, BookCreate

app = FastAPI()

db: List[Book] = [
    Book(
        title="1984",
        author="George Orwell",
        year=1949,
        genre="Dystopian"
    ),
    Book(
        title="To Kill a Mockingbird",
        author="Harper Lee",
        year=1960,
        genre="Fiction"
    )
]

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Book Library API!"}

@app.get("/api/books", response_model=List[Book])
async def fetch_books():
    return db

@app.post("/api/books", response_model=Book)
async def add_book(book_data: BookCreate):
    new_book = Book(**book_data.model_dump())
    db.append(new_book)
    return new_book
