import os
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from app.router import read, create, update, delete

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory='app/static'), name="static")
app.include_router(read.router)
app.include_router(create.router)
app.include_router(update.router)
app.include_router(delete.router)




