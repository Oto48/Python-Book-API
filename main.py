from fastapi import FastAPI
from typing import List
from models import Book, BookCreate
from uuid import UUID
from fastapi import HTTPException
from sample_data import sample_books

app = FastAPI()

# Starting data
db: List[Book] = sample_books

# Get Book by ID
@app.get("/api/books/{book_id}", response_model=Book)
async def get_book_by_id(book_id: UUID):
    for book in db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail=f"Book with id: {book_id} not found")

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

# Update Book by id
@app.put("/api/books/{book_id}", response_model=Book)
async def update_book(book_id: UUID, updated_data: BookCreate):
    for index, book in enumerate(db):
        if book.id == book_id:
            updated_book = Book(id=book_id, **updated_data.model_dump())
            db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail=f"Book with id: {book_id} not found")
