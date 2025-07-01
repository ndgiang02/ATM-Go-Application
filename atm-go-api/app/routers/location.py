from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Dict, Union
from app.dependencies import get_db_connection
from app.crud.location import get_all_locations
from app.schemas.loacation_schemas import LocationOut  

router = APIRouter()

@router.get("/admin/location", response_model=List[LocationOut])
def get_bank_data(db: Session = Depends(get_db_connection)):
    try:
        return get_all_locations(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/admin/location/search", response_model=List[LocationOut])
def search_banks(
    bank_code: str = Query(..., description="Mã ngân hàng"),
    type: str = Query(..., description="Loại ngân hàng"),
    db: Session = Depends(get_db_connection)
):
    try:
        from app.crud.location import get_banks_by_code_and_type
        return get_banks_by_code_and_type(db, bank_code, type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))