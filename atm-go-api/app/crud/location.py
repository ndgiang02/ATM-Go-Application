from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.location import Location

def get_all_locations(db: Session):
    return db.query(Location).all()

def get_banks_by_code_and_type(db: Session, bank_code: str, type: str):
    return db.query(Location).filter(Location.bank_code == bank_code, Location.type == type).all()

def get_nearest_locations(db: Session, latitude: float, longitude: float, limit: int = 5):
    return (
        db.query(Location)
        .order_by(
            func.pow(Location.latitude - latitude, 2) + func.pow(Location.longitude - longitude, 2)
        )
        .limit(limit)
        .all()
    )
	