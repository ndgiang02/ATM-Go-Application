from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.location import Location
from app.models.bank import Bank

def get_all_locations(db: Session):
    return (
    db.query(Location, Bank.logo_url.label("logo"))
    .join(Bank, Location.bank_code == Bank.code)
    .all()
    )


def get_banks_by_code_and_type(db: Session, bank_code: str, type: str):
    return (
        db.query(Location, Bank.logo_url.label("logo"))
        .join(Bank, Location.bank_code == Bank.code)
        .filter(Location.bank_code == bank_code, Location.type == type)
        .all()
    )


def get_nearest_locations(db: Session, latitude: float, longitude: float, limit: int = 5):
    return (
        db.query(
            Location,
            Bank.logo_url.label("logo"),
            haversine_distance(latitude, longitude, Location.latitude, Location.longitude).label("distance")

        )
        .join(Bank, Location.bank_code == Bank.code)
        .order_by("distance")
        .limit(limit)
        .all()
    )
	

def haversine_distance(lat1, lon1, lat2, lon2):
    return (
        6371 * func.acos(
            func.cos(func.radians(lat1)) *
            func.cos(func.radians(lat2)) *
            func.cos(func.radians(lon2) - func.radians(lon1)) +
            func.sin(func.radians(lat1)) *
            func.sin(func.radians(lat2))
        )
    )
