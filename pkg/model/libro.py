from sqlalchemy.orm import relationship
import uuid
from sqlalchemy import UUID, Column, String
from pkg.config.database import Base

class Libro(Base):
    __tablename__ = 'libri'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titolo = Column(String(255))
    autore = Column(String(255))
    isbn = Column(String(20))
    
    
    citazioni = relationship("Citazioni", back_populates="libro")
