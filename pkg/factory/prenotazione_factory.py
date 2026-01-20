import uuid
from pkg.dto.prenotazione_dto import InsertPrenotazioneDto, PrenotazioneDto
from pkg.model.prenotazione import Prenotazione

#Conversione da InsertPrenotazioneDTO ad Entità
def insert_to_model(insert_reservation: InsertPrenotazioneDto) -> Prenotazione:
    return Prenotazione(
        utente_id=insert_reservation.utente_id,
        libro_id=insert_reservation.libro_id,
        giorni_prestito=insert_reservation.giorni_prestito,
    )

#Conversione da Entità a DTO    
def model_to_dto(reservation: Prenotazione) -> PrenotazioneDto:
    return PrenotazioneDto(
        id = reservation.id,
        utente_id = reservation.utente_id,
        libro_id = reservation.libro_id,
        data_prenotazione = reservation.data_prenotazione,
        giorni_prestito=reservation.giorni_prestito,
        stato = reservation.stato
    )