from sqlalchemy.orm import Session
from app.models.bank import Bank

def get_all_banks(db: Session):
    return db.query(Bank).all()