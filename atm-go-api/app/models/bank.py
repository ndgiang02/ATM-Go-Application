# app/models/bank.py
from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base

class Bank(Base):
    __tablename__ = "bank"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    short_name = Column(String, nullable=False)
    logo_url = Column(String)
