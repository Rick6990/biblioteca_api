from pkg.config.database import engine, get_db
from pkg.controller import libro_controller, prenotazione_controller, utente_controller
from pkg.model import libro, prenotazione, utente 
from pkg.model.prenotazione import Base
from fastapi import FastAPI

connection = get_db()
Base.metadata.create_all(bind=engine)
app = FastAPI()

# Include il router del controller
app.include_router(utente_controller.router)
app.include_router(libro_controller.router)
app.include_router(prenotazione_controller.router)
