from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Dict, Union
from app.dependencies import get_db_connection
from app.crud.location import get_all_locations, get_banks_by_code_and_type, get_nearest_locations
from app.schemas.loacation_schemas import LocationOut  

router = APIRouter()

@router.get("/api/location/get-all-location", response_model=List[LocationOut])
def get_bank_data(db: Session = Depends(get_db_connection)):
    try:
        results = get_all_locations(db)
        return [
            LocationOut(
                **{**location.__dict__, "logo": logo}
            )
            for location, logo in results
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/api/location/get-location", response_model=List[LocationOut])
def get_banks_by_code_and_type(
    bank_code: str = Query(..., description="Mã ngân hàng"),
    type: str = Query(..., description="Loại ngân hàng"),
    db: Session = Depends(get_db_connection)
):
    try:
        results = get_banks_by_code_and_type(db, bank_code, type)
        return [
            LocationOut(
                **{**location.__dict__, "logo": logo}
            )
            for location, logo in results
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/api/location/get_nearest_locations", response_model=List[LocationOut])
def get_location_nearest(
    latitude: float = Query(..., description="Vĩ độ người dùng"),
    longitude: float = Query(..., description="Kinh độ người dùng"),
    db: Session = Depends(get_db_connection)
):
    try:
        results = get_nearest_locations(db, latitude, longitude)
        return [
            LocationOut(
                **{**location.__dict__, "logo": logo, "distance": distance}
            )
            for location, logo, distance in results
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
