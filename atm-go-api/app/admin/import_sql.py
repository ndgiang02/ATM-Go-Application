from fastapi import UploadFile
from sqlalchemy import text
from app.core.database import engine

async def execute_sql_file(file: UploadFile):
    sql_bytes = await file.read()
    sql_text = sql_bytes.decode("utf-8")

    statements = [stmt.strip() for stmt in sql_text.split(';') if stmt.strip()]

    with engine.begin() as connection:
        for statement in statements:
            connection.execute(text(statement))