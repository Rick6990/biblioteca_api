from dataclasses import dataclass
from sqlalchemy import UUID


@dataclass
class LibroDto:
    id: UUID
    titolo: str
    autore: str
    isbn: str
    
    
@dataclass
class InsertLibroDto:
    titolo: str
    autore: str
    isbn: str
