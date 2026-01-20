from dataclasses import dataclass
from datetime import date
import uuid
from pydantic import EmailStr


@dataclass
class UtenteDto:
    id: uuid.UUID
    nome: str
    cognome: str
    email: EmailStr
    
    
@dataclass
class InsertUtenteDto:
    nome: str
    cognome: str
    email: EmailStr
    
