import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from urllib.parse import quote_plus
from app.infrastructure.config import settings



SQLALCHEMY_DATABASE_URL = f"mysql://{quote_plus(settings.db_user)}:{quote_plus(settings.db_password)}@{quote_plus(settings.db_host)}/{quote_plus(settings.db_name)}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_session():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
