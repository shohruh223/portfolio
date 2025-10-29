import os
import shutil
from fastapi import APIRouter
from fastapi import Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND
from app.model import db, User

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
UPLOAD_DIRECTION = "app/static/media"


@router.get("/create-user", response_class=HTMLResponse)
async def form_user(request: Request):
    return templates.TemplateResponse("create_user.html",
                                      {"request": request})


@router.post("/create-user")
async def create_user(request: Request):
    form = await request.form()

    fullname = form.get("fullname")
    job = form.get("job")
    about = form.get("about")
    image: UploadFile = form.get("image")

    file_path = os.path.join(UPLOAD_DIRECTION, image.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    user = User(image=image.filename,
         fullname=fullname,
         job=job,
         about=about)

    db.add(user)
    db.commit()
    db.close()

    return RedirectResponse("/", status_code=HTTP_302_FOUND)