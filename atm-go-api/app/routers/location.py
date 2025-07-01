from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict, Union
import asyncpg
from app.dependencies import get_db_connection

router = APIRouter()

@router.get("/admin/data", response_model=List[Dict[str, Union[str, float, int, None]]])
async def get_atm_locations_data(conn: asyncpg.Connection = Depends(get_db_connection)):
    query = """
    SELECT 
        id, link, title, category, address, open_hours, 
        website, phone, review_rating, latitude, longitude, 
        descriptions, owner, bank_code, type
    FROM locations;
    """
    try:
        records = await conn.fetch(query)
        return [dict(record) for record in records]
    except Exception as e:
        print(f"Lỗi khi truy vấn dữ liệu từ PostgreSQL: {e}")
        raise HTTPException(status_code=500, detail=f"Lỗi khi tải dữ liệu từ database: {str(e)}")