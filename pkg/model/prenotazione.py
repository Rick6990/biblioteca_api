import uuid
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID  
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from pkg.config.database import Base


class Prenotazione(Base):
    __tablename__ = 'prenotazioni'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    utente_id = Column(UUID(as_uuid=True), ForeignKey('utenti.id'), nullable=False)
    libro_id = Column(UUID(as_uuid=True), ForeignKey('libri.id'), nullable=False)
    data_prenotazione = Column(DateTime, server_default= func.now(), nullable=False)  
    giorni_prestito = Column(Integer, nullable=False)
    stato = Column(String(20), default='RESERVE', nullable=False)
    
    utente = relationship("Utente", backref="prenotazioni")
    libro = relationship("Libro", backref="prenotazioni")