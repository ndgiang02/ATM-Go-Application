from fastapi import Depends
from app.db.database import SessionLocal
from sqlalchemy.orm import Session

def get_db_connection() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()