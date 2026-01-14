import uuid
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from pkg.config.database import get_db
from pkg.dto.utente_dto import InsertUtenteDto
#from pkg.plugin.dependencies import ServiceDependencies, get_services
from pkg.repository.utente_repo import UtenteRepository
from pkg.services.utente_service import UtenteService

# Crea il router
router = APIRouter(
    prefix="/utenti",
    tags=["Utenti"],
    responses={404: {"description": "Not found"}}
)


""" @router.post("/v1", response_model=UtenteDto)
def root(insert_user: InsertUtenteDto, deps: ServiceDependencies = Depends(get_services)):
    return deps.user_service.create_user(insert_user) """
    
@router.post("/add")
def create_user(
    insert_user: InsertUtenteDto,
    db: Session = Depends(get_db)  # Inietta automaticamente
):
    repository = UtenteRepository(session=db)
    service = UtenteService(repository=repository)
    return service.create_user(insert_user)


@router.get("/{id}")
def get_byId(id:uuid.UUID, db: Session = Depends(get_db)):
    repository = UtenteRepository(session=db)
    service = UtenteService(repository=repository)
    utente = service.find_userById(id)
    
    if utente is None:
        raise HTTPException(status_code = 404,detail = "ID utente non presente")
    return utente


@router.delete("/delete/{id}")
def delete_by_user_Id (id: uuid.UUID, db:Session = Depends(get_db)):
    repository = UtenteRepository(session=db)
    service = UtenteService(repository=repository)
    utente_deleted = service.delete_user_by_Id(id)
    
    if utente_deleted is None:
        raise HTTPException(status_code = 404,detail = "ID utente non presente")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/update/{id}")
def update_user_by_Id(id: uuid.UUID, user_updated: InsertUtenteDto, db: Session = Depends(get_db)):
    repository = UtenteRepository(session=db)
    service = UtenteService(repository=repository)
    
    utente = service.update_user(id, user_updated)
    
    if utente is None:
        raise HTTPException(status_code=404, detail="Utente non trovato")
    return utente
    