from dataclasses import dataclass
from functools import lru_cache
from pkg.config.database import get_postgres_connection
from pkg.repository.libro_repo import LibroRepository
from pkg.repository.prenotazione_repo import PrenotazioneRepository
from pkg.repository.utente_repo import UtenteRepository
from pkg.services.libro_service import LibroService
from pkg.services.prenotazione_service import PrenotazioneService
from pkg.services.utente_service import UtenteService


@dataclass(frozen=True)
class ServiceDependencies:
    user_service: UtenteService
    book_service: LibroService
    reservation_service: PrenotazioneService


@lru_cache
def get_services() -> ServiceDependencies:
    database = get_postgres_connection()
    user_repository = UtenteRepository(database)
    book_repository = LibroRepository(database)
    reservation_repository = PrenotazioneRepository(database)
    user_service = UtenteService(user_repository)
    book_service = LibroService(book_repository)
    reservation_service = PrenotazioneService(reservation_repository)
    
    print("Deps initialized!")

    return ServiceDependencies(
        user_service=user_service,
        book_service=book_service,
        reservation_service=reservation_service
    )