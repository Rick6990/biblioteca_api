from dataclasses import dataclass, field
from sqlalchemy import UUID


@dataclass
class LibroDto:
    id: UUID
    titolo: str
    autore: str
    isbn: str
    citazioni : list[str]    
    
    
    
@dataclass
class InsertLibroDto:
    titolo: str
    autore: str
    isbn: str
    citazioni : list[str]    


