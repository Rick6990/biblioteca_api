from dataclasses import dataclass
import uuid


@dataclass
class UtenteDto:
    id: uuid.UUID
    nome: str
    cognome: str
    email: str
    
    
@dataclass
class InsertUtenteDto:
    nome: str
    cognome: str
    email: str
