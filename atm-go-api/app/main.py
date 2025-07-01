import os
from typing import List, Dict, Union
from fastapi import FastAPI, Request, UploadFile, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi import UploadFile
from app.models.base import engine
from app.admin.import_sql import execute_sql_file
from app.routers.admin import router as admin

from app.routers import admin
from app.routers import bank
from app.routers import location
import asyncpg

app = FastAPI(title="ATM Go API")

# Static & Templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# --- Database config ---
DB_USER = os.environ.get("POSTGRES_USER", "postgres")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
DB_HOST = os.environ.get("POSTGRES_HOST", "localhost")
DB_PORT = os.environ.get("POSTGRES_PORT", "5432")
DB_NAME = os.environ.get("POSTGRES_DB", "atm_go_db")
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

db_pool = None

@app.on_event("startup")
async def startup():
    global db_pool
    try:
        db_pool = await asyncpg.create_pool(DATABASE_URL)
        print("Kết nối PostgreSQL thành công.")
    except Exception as e:
        print(f"Lỗi khi kết nối PostgreSQL: {e}")

@app.on_event("shutdown")
async def shutdown():
    if db_pool:
        await db_pool.close()
        print("Đã đóng kết nối PostgreSQL.")

async def get_db_connection():
    async with db_pool.acquire() as connection:
        yield connection


app.include_router(admin.router)
app.include_router(bank.router)
app.include_router(location.router)