from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.bank import Bank

def get_all_banks(db: Session):
    return db.query(Bank).all()