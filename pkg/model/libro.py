import uuid
from sqlalchemy import UUID, create_engine, Column, String
from sqlalchemy.orm import sessionmaker, relationship
from pkg.config.database import Base

class Libro(Base):
    __tablename__ = 'libri'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titolo = Column(String(255))
    autore = Column(String(255))
    isbn = Column(String(20))
    
    #prenotazioni = relationship("Prenotazione", back_populates="libro")

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