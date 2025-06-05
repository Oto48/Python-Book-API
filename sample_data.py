from uuid import uuid4
from models import Book
from typing import List

sample_books: List[Book] = [
    Book(
        id=uuid4(),
        title="1984",
        author="George Orwell",
        year=1949,
        genre="Dystopian"
    ),
    Book(
        id=uuid4(),
        title="To Kill a Mockingbird",
        author="Harper Lee",
        year=1960,
        genre="Fiction"
    )
]
