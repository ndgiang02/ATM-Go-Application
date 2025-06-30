from fastapi import UploadFile
from app.core.database import engine

async def execute_sql_file(file: UploadFile):
    sql_bytes = await file.read()
    sql_text = sql_bytes.decode("utf-8")

    with engine.connect() as connection:
        connection.execute(sql_text)
        connection.commit()
