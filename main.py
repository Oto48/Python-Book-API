from fastapi import FastAPI
from typing import List
from models import Book, BookCreate
from uuid import UUID
from fastapi import HTTPException

app = FastAPI()

# Starting data
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

# Home page
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Book Library API!"}

# Get the list of Books
@app.get("/api/books", response_model=List[Book])
async def fetch_books():
    return db

# Add a new Book
@app.post("/api/books", response_model=Book)
async def add_book(book_data: BookCreate):
    new_book = Book(**book_data.model_dump())
    db.append(new_book)
    return new_book

# Delete a Book
@app.delete("/api/books/{book_id}")
async def delete_book(book_id: UUID):
    for index, book in enumerate(db):
        if book.id == book_id:
            del db[index]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Book with id: {book_id} not found")
