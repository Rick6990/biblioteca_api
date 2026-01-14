import uuid
from sqlalchemy import UUID, create_engine, Column, String
from pkg.config.database import Base
from sqlalchemy.orm import sessionmaker, relationship

class Utente(Base):
    __tablename__ = 'utenti'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String(100))
    cognome = Column(String(100))
    email = Column(String(200))
    
    #prenotazioni = relationship("Prenotazione", back_populates="utente")

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