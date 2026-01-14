from typing import Optional
from sqlalchemy import UUID
from pkg.dto.utente_dto import InsertUtenteDto, UtenteDto
from pkg.factory.user_factory import insert_to_model, model_to_dto
from pkg.repository.utente_repo import UtenteRepository

class UtenteService:
    def __init__(self, repository: UtenteRepository) -> UtenteDto:
        self.repository=repository
        
    def create_user (self, insert_user: InsertUtenteDto): 
        user = insert_to_model(insert_user)
        self.repository.add(user)
        return model_to_dto(user)
    
    def find_userById (self,  user_id: UUID) -> UtenteDto:
        user = self.repository.find_by_id(user_id)
        if user is None:
            return None
        return model_to_dto(user)
    
    def update_user(self, user_id : UUID, user_updated : InsertUtenteDto) -> Optional[UtenteDto]:
        user = self.repository.find_by_id(user_id)
        
        if not user:
            return None
        
        user.nome = user_updated.nome
        user.cognome = user_updated.cognome
        user.email = user_updated.email
        
        self.repository.update(user)
        return model_to_dto(user)
         
    
    def delete_user_by_Id(self , user_id: UUID) -> UtenteDto:
        user_id_deleted  = self.repository.delete_by_id(user_id)
        if user_id_deleted is None:
            return None
        return model_to_dto(user_id_deleted) 
        
            
            