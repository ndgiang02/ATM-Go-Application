from fastapi import UploadFile, HTTPException
from sqlalchemy import text
from app.models.base import engine


async def execute_sql_file(file: UploadFile):
    sql_bytes = await file.read()
    sql_text = sql_bytes.decode("utf-8")

    try:
        with engine.begin() as connection:
            connection.exec_driver_sql(sql_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi thực thi file SQL: {str(e)}")