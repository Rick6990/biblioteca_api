import uuid
from pkg.dto.utente_dto import InsertUtenteDto, UtenteDto
from pkg.model.utente import Utente

#Conversione da InsertUtenteDTO ad Entità
def insert_to_model(insert_user: InsertUtenteDto) -> Utente:
    return Utente(
            id = uuid.uuid4(),
            nome= insert_user.nome, 
            cognome = insert_user.cognome, 
            email = insert_user.email
            )

#Conversione da Entità a DTO    
def model_to_dto(user: Utente) -> UtenteDto:
    return UtenteDto(
        id = user.id,
        nome = user.nome,
        cognome = user.cognome,
        email = user.email
    )