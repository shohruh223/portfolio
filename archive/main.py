# from fastapi import FastAPI, Request, status
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from starlette.responses import RedirectResponse
# from starlette.staticfiles import StaticFiles
# from starlette.status import HTTP_302_FOUND
# from app.bot import bot, TELEGRAM_CHAT_ID, lifespan
# from app.database import get_db
# from app.model import Contact
#
# app = FastAPI(lifespan=lifespan)
# templates = Jinja2Templates(directory="app/templates")
# app.mount("/static", StaticFiles(directory='app/static'), name="static")
#
#
# @app.get("/", response_class=HTMLResponse)
# async def index(request: Request):
#     message = request.query_params.get("message", None)
#     return templates.TemplateResponse("index.html",
#                                       {"request": request, "message":message})
#
#
# @app.post("/contact")
# async def create_contact(request: Request):
#     form = await request.form()
#     phone_number = form.get("phone_number")
#     gmail = form.get("gmail")
#     subject = form.get("subject")
#     message = form.get("message")
#
#     contact = Contact(phone_number=phone_number,
#                       gmail=gmail,
#                       subject=subject,
#                       message=message)
#     db = get_db()
#     db.add(contact)
#     db.commit()
#
#     # Telegramga yuboriladigan xabar
#     text = (
#         "<b>Yangi kontakt xabari</b>\n"
#         f"📱 <b>Phone:</b> {phone_number}\n"
#         f"🤖 <b>Telegram:</b><a href='https://t.me/{phone_number}'> {phone_number}</a>\n"
#         f"✉️ <b>Email:</b> {gmail}\n"
#         f"🧾 <b>Subject:</b> {subject}\n"
#         f"📝 <b>Message:</b>\n{message}"
#     )
#
#     await bot.send_message(chat_id=TELEGRAM_CHAT_ID,
#                            text=text,
#                            parse_mode="HTML",
#                            disable_web_page_preview=True)
#
#
#     return RedirectResponse("/?message=success#contact", status_code=status.HTTP_303_SEE_OTHER)
