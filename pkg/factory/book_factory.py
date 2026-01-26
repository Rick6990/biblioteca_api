import uuid
from pkg.dto.libro_dto import InsertLibroDto, LibroDto
from pkg.model.citazioni import Citazioni
from pkg.model.libro import Libro

#Conversione da InsertLibroDTO ad Entità
def insert_to_model(insert_book: InsertLibroDto) -> Libro:
    libro = Libro(
        id=uuid.uuid4(),
        titolo=insert_book.titolo, 
        autore=insert_book.autore, 
        isbn=insert_book.isbn,
        citazioni=[
            Citazioni(testo_citazione=citazione) for citazione in insert_book.citazioni
        ]
    )
    return libro

#Conversione da Entità a DTO    
def model_to_dto(book: Libro) -> LibroDto:
    return LibroDto(
        id = book.id,
        titolo = book.titolo,
        autore = book.autore,
        isbn = book.isbn,
        citazioni= [
            citazione.testo_citazione for citazione in book.citazioni
        ] 
    )