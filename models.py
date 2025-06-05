from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

# Model used when creating a book
class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=70)
    author: str = Field(..., min_length=1, max_length=70)
    year: int = Field(..., ge=0, le=2100)
    genre: Optional[str] = Field(None, max_length=50)

# Model that represents a book in the db
class Book(BookCreate):
    id: UUID = Field(default_factory=uuid4)
