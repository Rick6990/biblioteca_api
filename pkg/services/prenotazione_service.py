from typing import Optional
from sqlalchemy import UUID
from pkg.dto.prenotazione_dto import InsertPrenotazioneDto, PrenotazioneDto, UpdatePrenotazioneDto
from pkg.factory.prenotazione_factory import insert_to_model, model_to_dto
from pkg.repository.prenotazione_repo import PrenotazioneRepository


class PrenotazioneService:
    def __init__(self, repository: PrenotazioneRepository) -> PrenotazioneDto:
        self.repository=repository
        
    def create_reservation(self, insert_reservation: InsertPrenotazioneDto): 
        reservation = insert_to_model(insert_reservation)
        self.repository.add(reservation)
        return model_to_dto(reservation)
        
    
    def get_reservation_byId(self, reservation_id: UUID ) -> Optional[PrenotazioneDto]:
        reservation = self.repository.find_by_id(reservation_id)
        if reservation is None:
            return None
        
        return reservation
    
    def get_all_reservation(self) -> list[PrenotazioneDto]:
        reservation = self.repository.find_all_reservation().sort()
        return reservation
    
    def update_reservation(self, reservation_id : UUID, reservation_updated : UpdatePrenotazioneDto) -> Optional[PrenotazioneDto]:
        reservation = self.repository.find_by_id(reservation_id)
        
        if not reservation:
            return None
        
        reservation.data_prenotazione = reservation_updated.data_prenotazione
        reservation.stato = reservation_updated.stato
        
        self.repository.update_reservation(reservation)
        return model_to_dto(reservation)
    
    def delete_reservation_by_Id(self , reservation_id: UUID) -> PrenotazioneDto:
        reservation_id_deleted  = self.repository.delete_reservation_byId(reservation_id)
        if reservation_id_deleted is None:
            return None
        return model_to_dto(reservation_id_deleted) 
    
    