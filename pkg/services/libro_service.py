from typing import Optional
from sqlalchemy import UUID
from pkg.dto.libro_dto import InsertLibroDto, LibroDto
from pkg.repository.libro_repo import LibroRepository
from pkg.factory.book_factory import insert_to_model, model_to_dto



class LibroService:
    def __init__(self, repository: LibroRepository) -> LibroDto:
        self.repository=repository
        
    def create_book (self, insert_book: InsertLibroDto): 
        book = insert_to_model(insert_book)
        self.repository.add(book)
        return model_to_dto(book)
    
    def find_bookById (self,  book_id: UUID) -> LibroDto:
        book = self.repository.find_by_id(book_id)
        if book is None:
            return None
        return model_to_dto(book)
    
    def update_book(self, book_id : UUID, book_updated : InsertLibroDto) -> Optional[LibroDto]:
        book = self.repository.find_by_id(book_id)
        
        if not book:
            return None
        
        book.titolo = book_updated.titolo
        book.autore = book_updated.autore
        book.isbn = book_updated.isbn
        self.repository.update_book(book)
        return model_to_dto(book)
         
    
    def delete_book_by_Id(self , book_id: UUID) -> LibroDto:
        book_id_deleted  = self.repository.delete_by_id(book_id)
        if book_id_deleted is None:
            return None
        return model_to_dto(book_id_deleted) 