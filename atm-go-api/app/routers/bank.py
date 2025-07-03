from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.dependencies import get_db_connection
from app.crud.bank import get_all_banks
from app.schemas.bank_shemas import BankOut

router = APIRouter()

@router.get("/api/bank/get-bank", response_model=List[BankOut])
def get_bank_data(db: Session = Depends(get_db_connection)):
    try:
        return get_all_banks(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))