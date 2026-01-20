import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Costruzione della stringa di connessione a PostgreSQL
DATABASE_URL = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Creazione dell'engine SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    connect_args={"connect_timeout": 5},
    pool_pre_ping=True  # Verifica che la connessione sia ancora valida
)

# Creazione della sessione locale
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base per i modelli
Base = declarative_base()

# Dependency per FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()