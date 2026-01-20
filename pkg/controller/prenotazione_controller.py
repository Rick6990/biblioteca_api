import uuid
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from pkg.config.database import get_db
from pkg.dto.prenotazione_dto import InsertPrenotazioneDto
from pkg.repository.prenotazione_repo import PrenotazioneRepository
from pkg.repository.utente_repo import UtenteRepository
from pkg.services.prenotazione_service import PrenotazioneService
from pkg.services.email_sender import EmailSender
from pkg.services.utente_service import UtenteService


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
    repository_user = UtenteRepository(session = db)
    service_user = UtenteService(repository=repository_user)   
    send_email.send(service_user.find_userById(user_id=insert_reservation.utente_id))
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
    reservation_id = service.get_reservation_byId(id)
    
    if reservation_id is None:
        raise HTTPException(status_code = 404,detail = "ID Prenotazione non trovata")
    return reservation_id


@router.patch("/update/{id}")
def update_reservation_by_Id(id: uuid.UUID, user_updated: InsertPrenotazioneDto, db: Session = Depends(get_db)):
    repository = PrenotazioneRepository(session=db)
    service = PrenotazioneService(repository=repository)
    
    update_reservation = service.update_reservation(id, user_updated)
    
    if update_reservation is None:
        raise HTTPException(status_code=404, detail="ID Prenotazione non trovata")
    return update_reservation

@router.delete("/delete/{id}")
def delete_by_reservation_Id (id: uuid.UUID, db:Session = Depends(get_db)):
    repository = PrenotazioneRepository(session=db)
    service = PrenotazioneService(repository=repository)
    reservation_deleted = service.delete_reservation_by_Id(id)
    
    if reservation_deleted is None:
        raise HTTPException(status_code = 404,detail = "ID Prenotazione non trovata")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
