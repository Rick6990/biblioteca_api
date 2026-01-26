import uuid
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from pkg.config.database import get_db
from pkg.dto.libro_dto import InsertLibroDto
from pkg.repository.libro_repo import LibroRepository
from pkg.services.libro_service import LibroService


router = APIRouter(
    prefix="/api/internal/books",
    tags=["Libri"],
    responses={404: {"description": "Not found"}}
)
   
    
@router.post("/v1")
def create_book(
    insert_book: InsertLibroDto,
    db: Session = Depends(get_db)  
):
    repository = LibroRepository(session=db)
    service = LibroService(repository=repository)
    return service.create_book(insert_book)


@router.get("/{id}/v1")
def get_book_byId(id:uuid.UUID, db: Session = Depends(get_db)):
    repository = LibroRepository(session=db)
    service = LibroService(repository=repository)
    book = service.find_bookById(id)
    
    if book is None:
        raise HTTPException(status_code = 404,detail = "ID utente non presente")
    return book


@router.delete("/{id}/v1")
def delete_by_book_Id (id: uuid.UUID, db:Session = Depends(get_db)):
    repository = LibroRepository(session=db)
    service = LibroService(repository=repository)
    book_deleted = service.delete_book_by_Id(id)
    
    if book_deleted is None:
        raise HTTPException(status_code = 404,detail = "ID utente non presente")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}/v1")
def update_book_by_Id(id: uuid.UUID, book_updated: InsertLibroDto, db: Session = Depends(get_db)):
    repository = LibroRepository(session=db)
    service = LibroService(repository=repository)
    
    book = service.update_book(id, book_updated)
    
    if book is None:
        raise HTTPException(status_code=404, detail="Libro non trovato!")
    return book