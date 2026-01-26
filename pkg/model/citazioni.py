from sqlalchemy.orm import relationship
import uuid
from sqlalchemy import UUID, Column, ForeignKey, String
from pkg.config.database import Base


class Citazioni(Base):
    __tablename__ = 'citazioni'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    libro_id = Column(UUID(as_uuid=True), ForeignKey('libri.id'), nullable=False)
    testo_citazione = Column(String(255))
    

    libro = relationship("Libro", back_populates="citazioni")