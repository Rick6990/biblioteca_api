from sqlalchemy import UUID
from sqlalchemy.orm import Session
from typing import Optional
from pkg.model.utente import Utente


class UtenteRepository:
    
    def __init__(self, session: Session):
        self.session = session 
        
    def add(self, user: Utente) -> Utente:
        self.session.add(user)
        self.session.flush()
        self.session.commit()
        return user
    
    def find_by_id(self, user_id: UUID) -> Optional[Utente]:
        return self.session.query(Utente).filter(Utente.id == user_id).first()
    
    def update(self, user: Utente) -> Optional[Utente]:
        self.session.flush()
        self.session.commit()
        return user 
        
        
    def delete_by_id(self, user_id: UUID) -> Optional[Utente]:
        user_deleted = self.session.query(Utente).filter(Utente.id == user_id).first()
        if user_deleted:
            self.session.delete(user_deleted)
            self.session.commit()
         
        return user_deleted
    
    
        
     