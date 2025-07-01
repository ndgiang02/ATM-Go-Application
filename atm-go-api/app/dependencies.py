from fastapi import Depends
from app.models.base import SessionLocal
from sqlalchemy.orm import Session


def get_db_connection() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()