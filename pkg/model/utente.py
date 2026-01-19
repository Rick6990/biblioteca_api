from datetime import date
import uuid
from sqlalchemy import UUID, Column, String
from pkg.config.database import Base

class Utente(Base):
    __tablename__ = 'utenti'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String(100))
    cognome = Column(String(100))
    email = Column(String(200))
