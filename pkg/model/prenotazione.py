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
    data_restituzione = Column(DateTime, nullable=True)  
    giorni_prestito = Column(Integer, nullable=False)
    stato = Column(String(20), default='attiva', nullable=False)
    
    utente = relationship("Utente", backref="prenotazioni")
    libro = relationship("Libro", backref="prenotazioni")
    
""" db_url = create_engine('postgresql+psycopg2://postgres:Its2025!@localhost/biblioteca_db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_url)
Base.metadata.create_all(db_url) 

def get_db_session():
    session = SessionLocal()  # Questo crea una Session SQLAlchemy
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close() """