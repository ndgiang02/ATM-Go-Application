import os
from typing import List, Dict, Union
from fastapi import FastAPI, Request, UploadFile, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi import UploadFile
from app.core.database import engine
from app.admin.import_sql import execute_sql_file
from sqlalchemy import text
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

# --- SQL Upload ---
@app.post("/admin/import_sql")
async def import_sql(file: UploadFile):
    try:
        await execute_sql_file(file)
        return JSONResponse(content={"message": f"File '{file.filename}' đã được thực thi thành công trên PostgreSQL!"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": f"Lỗi khi thực thi file SQL: {str(e)}"})
    
    
@app.post("/admin/upload_sql")   
async def upload_sql(file: UploadFile):
    try:
        # Kết nối tới PostgreSQL
        conn = await asyncpg.connect(DATABASE_URL)

        content = (await file.read()).decode("utf-8")
        statements = content.split(";")
        for statement in statements:
            stmt = statement.strip()
            if stmt:
                await conn.execute(stmt)
        await conn.close()
        return {"message": "Upload và thực thi SQL thành công!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi thực thi SQL: {str(e)}")

# --- Trang quản trị & SQL ---
@app.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    return templates.TemplateResponse("admin_dashboard.html", {"request": request})

@app.get("/admin/sql", response_class=HTMLResponse)
async def admin_sql_page(request: Request):
    return templates.TemplateResponse("admin_import_sql.html", {"request": request})

@app.get("/admin/data", response_model=List[Dict[str, Union[str, float, int, None]]])
async def get_atm_locations_data(conn: asyncpg.Connection = Depends(get_db_connection)):
    query = """
    SELECT 
        link, title, category, address, open_hours, 
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

@app.get("/admin/bank", response_model=List[Dict[str, Union[str, None]]])
async def get_bank_data(conn: asyncpg.Connection = Depends(get_db_connection)):
    query = """
    SELECT 
        code, 
        name, 
        short_name, 
        logo_url
    FROM bank;
    """
    try:
        records = await conn.fetch(query)
        return [dict(record) for record in records]
    except Exception as e:
        print(f"Lỗi khi truy vấn dữ liệu từ PostgreSQL: {e}")
        raise HTTPException(status_code=500, detail=f"Lỗi khi tải dữ liệu từ database: {str(e)}")


# --- Redirect root ---
@app.get("/")
async def root_redirect():
    return RedirectResponse(url="/admin")