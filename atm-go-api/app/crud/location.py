from sqlalchemy.orm import Session
from app.models.location import Location

def get_all_locations(db: Session):
    return db.query(Location).all()

def get_banks_by_code_and_type(db: Session, bank_code: str, type: str):
    return db.query(Location).filter(Location.bank_code == bank_code, Location.type == type).all()