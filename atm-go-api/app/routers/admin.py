from fastapi import APIRouter, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, UploadFile, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

ASYNC_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@db:5432/atm_go_db"
async_engine = create_async_engine(ASYNC_DATABASE_URL, echo=False, future=True)
async_session = sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession
)

@router.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    return templates.TemplateResponse("admin_dashboard.html", {"request": request})


@router.get("/")
async def root_redirect():
    return RedirectResponse(url="/admin")

@router.post("/admin/upload_sql")
async def upload_sql(file: UploadFile):
    try:
        content = (await file.read()).decode("utf-8")
        statements = [stmt.strip() for stmt in content.split(";") if stmt.strip()]

        async with async_engine.begin() as conn:
            for statement in statements:
                if not statement:
                    continue
                try:
                    await conn.execute(text(statement))
                except Exception as stmt_err:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Lỗi ở câu lệnh: {statement[:100]}... ({stmt_err})"
                    )

        return {"message": "Upload và thực thi SQL thành công!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi thực thi SQL: {str(e)}")
