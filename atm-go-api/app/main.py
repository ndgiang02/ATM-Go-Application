from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="ATM Go API")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
