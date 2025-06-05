from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

# Model used when creating a book
class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    genre: Optional[str] = None

# Model that represents a book in the db
class Book(BookCreate):
    id: UUID = Field(default_factory=uuid4)
