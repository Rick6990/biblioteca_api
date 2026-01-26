from typing import Optional
from sqlalchemy import UUID, text
from sqlalchemy.orm import Session
from pkg.model.libro import Libro


class LibroRepository:
    
    def __init__(self, session: Session):
        self.session = session 
        
    def add(self, book : Libro) -> Libro:
        self.session.add(book)
        self.session.flush()
        self.session.commit()
        return book
    
 
    
    def find_by_id(self, book_id: UUID) -> Optional[Libro]:
        return self.session.query(Libro).filter(Libro.id == book_id).first()
    
    def update_book(self, book: Libro) -> Optional[Libro]:
        self.session.flush()
        self.session.commit()
        return book 
    
    def delete_by_id(self, book_id: UUID) -> Optional[Libro]:
        book_deleted = self.session.query(Libro).filter(Libro.id == book_id).first()
        if book_deleted:
            self.session.delete(book_deleted)
            self.session.commit()
         
        return book_deleted