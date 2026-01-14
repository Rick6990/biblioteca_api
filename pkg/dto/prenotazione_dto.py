from dataclasses import  dataclass
import datetime
import uuid


@dataclass
class InsertPrenotazioneDto:
    utente_id : uuid.UUID
    libro_id: uuid.UUID
    giorni_prestito: int

@dataclass  
class UpdatePrenotazioneDto:
    data_prenotazione : datetime
    data_restituzione: datetime
    stato: str
    
@dataclass
class PrenotazioneDto:
    id: uuid.UUID
    utente_id: uuid.UUID
    libro_id: uuid.UUID
    data_prenotazione : datetime
    data_restituzione: datetime
    giorni_prestito: int
    stato: str