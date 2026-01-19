import uuid
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from pkg.config.database import get_db
from pkg.dto.prenotazione_dto import InsertPrenotazioneDto
from pkg.repository.prenotazione_repo import PrenotazioneRepository
from pkg.services.prenotazione_service import PrenotazioneService
from pkg.services.email_sender import EmailSender


router = APIRouter(
    prefix="/prenotazioni",
    tags=["Prenotazioni"],
    responses={404: {"description": "Not found"}}
)

send_email = EmailSender()

@router.post("/add_reservation")
def create_reservation(
    insert_reservation: InsertPrenotazioneDto,
    db: Session = Depends(get_db) 
):    
    repository = PrenotazioneRepository(session=db)
    service = PrenotazioneService(repository=repository)
    send_email.send()
    return service.create_reservation(insert_reservation)


@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    repository = PrenotazioneRepository(session=db)
    service = PrenotazioneService(repository=repository)
    return service.get_all_reservation()

@router.get("/{id}")
def get_reservation_byId(id:uuid.UUID, db: Session = Depends(get_db)):
    repository = PrenotazioneRepository(session=db)
    service = PrenotazioneService(repository=repository)
    utente = service.get_reservation_byId(id)
    
    if utente is None:
        raise HTTPException(status_code = 404,detail = "ID utente non presente")
    return utente


@router.patch("/update/{id}")
def update_reservation_by_Id(id: uuid.UUID, user_updated: InsertPrenotazioneDto, db: Session = Depends(get_db)):
    repository = PrenotazioneRepository(session=db)
    service = PrenotazioneService(repository=repository)
    
    utente = service.update_reservation(id, user_updated)
    
    if utente is None:
        raise HTTPException(status_code=404, detail="Prenotazzione non trovata")
    return utente

@router.delete("/delete/{id}")
def delete_by_reservation_Id (id: uuid.UUID, db:Session = Depends(get_db)):
    repository = PrenotazioneRepository(session=db)
    service = PrenotazioneService(repository=repository)
    utente_deleted = service.delete_reservation_by_Id(id)
    
    if utente_deleted is None:
        raise HTTPException(status_code = 404,detail = "ID utente non presente")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
