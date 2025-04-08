from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker 

from app.core.config import settings

# Establish connection (lazy initialization)
DATABASE_URL = settings.DATABASE_URL
engine = create_engine (
    DATABASE_URL,
    pool_pre_ping=True
)

Base = declarative_base()

# Init session object
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()