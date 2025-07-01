from fastapi import APIRouter, UploadFile, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.admin.import_sql import execute_sql_file
from app.models.base import engine

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.post("/admin/import_sql")
async def import_sql(file: UploadFile):
    try:
        await execute_sql_file(file)
        return JSONResponse(content={"message": f"File '{file.filename}' đã được thực thi thành công trên PostgreSQL!"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": f"Lỗi khi thực thi file SQL: {str(e)}"})

@router.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    return templates.TemplateResponse("admin_dashboard.html", {"request": request})

@router.get("/admin/sql", response_class=HTMLResponse)
async def admin_sql_page(request: Request):
    return templates.TemplateResponse("admin_import_sql.html", {"request": request})

@router.get("/")
async def root_redirect():
    return RedirectResponse(url="/admin")

@router.post("/admin/upload_sql")
async def upload_sql(file: UploadFile):
    try:

        content = (await file.read()).decode("utf-8")
        statements = content.split(";")
        for statement in statements:
            stmt = statement.strip()
            if stmt:
                await engine.execute(stmt)
        await engine.close()
        return {"message": "Upload và thực thi SQL thành công!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi thực thi SQL: {str(e)}")