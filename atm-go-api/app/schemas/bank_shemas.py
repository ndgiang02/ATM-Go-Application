# app/schemas/bank.py
from pydantic import BaseModel

class BankCreate(BaseModel):
    code: str
    name: str
    short_name: str
    logo_url: str

class BankOut(BankCreate):
    id: int
    class Config:
        orm_mode = True
