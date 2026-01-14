from typing import Optional
import uuid
from sqlalchemy import UUID
from sqlalchemy.orm import Session
from pkg.model.prenotazione import Prenotazione

class PrenotazioneRepository:

    def __init__(self, session: Session):
        self.session = session 
        
    def add(self, reservetion: Prenotazione) -> Prenotazione:
        self.session.add(reservetion)
        self.session.flush()
        self.session.commit()
        return reservetion
    
    def find_by_id(self, reservation_id: uuid.UUID) -> Optional[Prenotazione]:
        return self.session.query(Prenotazione).filter(Prenotazione.id == reservation_id).first()
    
    def find_all_reservation(self) -> list[Prenotazione]:
        return self.session.query(Prenotazione).all()
    
    def find_by_utente(self, utente_id: uuid.UUID) -> list[Prenotazione]:
        return self.session.query(Prenotazione).filter(Prenotazione.utente_id == utente_id)
    
    def update_reservation(self, reservation: Prenotazione) -> Prenotazione:
        self.session.flush()
        self.session.commit()
        return reservation 
    
    def delete_reservation_byId(self, reservetion_id: uuid.UUID) -> Optional[Prenotazione]:
        reservation_deleted = self.find_by_id(reservetion_id)
        if reservetion_id:
            self.session.delete(reservation_deleted)
            self.session.commit()
            
            return reservation_deleted