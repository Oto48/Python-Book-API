from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

# Input model (no ID required)
class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    genre: Optional[str] = None

# Full model (includes ID)
class Book(BookCreate):
    id: UUID = Field(default_factory=uuid4)
