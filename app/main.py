# app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from environs import Env

from app.bot import bot, dp, setup_webhook  # aiogramdan import
from app.database import get_db
from app.model import Contact

env = Env()
env.read_env()

TELEGRAM_CHAT_ID = env.int("TELEGRAM_CHAT_ID", 0)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    message = request.query_params.get("message")
    return templates.TemplateResponse("index.html", {"request": request, "message": message})


@app.post("/contact")
async def create_contact(request: Request):
    form = await request.form()
    phone_number = form.get("phone_number")
    gmail = form.get("gmail")
    subject = form.get("subject")
    message = form.get("message")

    contact = Contact(phone_number=phone_number,
                      gmail=gmail,
                      subject=subject,
                      message=message)
    db = get_db()
    db.add(contact)
    db.commit()

    # (ixtiyoriy) Telegramga xabar yuborish
    if TELEGRAM_CHAT_ID:
        text = (
            "<b>Yangi kontakt xabari</b>\n"
            f"📱 <b>Phone:</b> {phone_number}\n"
            f"🤖 <b>Telegram:</b><a href='https://t.me/{phone_number}'> {phone_number}</a>\n"
            f"✉️ <b>Email:</b> {gmail}\n"
            f"🧾 <b>Subject:</b> {subject}\n"
            f"📝 <b>Message:</b>\n{message}\n"
        )
        try:
            await bot.send_message(
                chat_id=TELEGRAM_CHAT_ID,
                text=text,
                parse_mode="HTML",
                disable_web_page_preview=True
            )
        except Exception:
            pass

    return RedirectResponse("/?message=success#contact", status_code=303)


# --- Webhook endpoint (hech qanday secret tekshiruvi yo‘q) ---
@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    await dp.feed_raw_update(bot, data)
    return JSONResponse({"ok": True})


# --- FastAPI ishga tushganda webhookni o‘rnatish ---
@app.on_event("startup")
async def on_startup():
    await setup_webhook()


# # app/main.py (qo'shimcha diagnostika endpointlari)
# from fastapi import HTTPException
# from aiogram.methods.get_webhook_info import GetWebhookInfo
#
# @app.get("/_webhook_info", response_class=JSONResponse)
# async def webhook_info():
#     try:
#         info = await bot(GetWebhookInfo())
#         return info.model_dump()
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
# @app.post("/_set_webhook")
# async def force_set_webhook():
#     try:
#         await setup_webhook()
#         return JSONResponse({"ok": True, "message": "Webhook set via setup_webhook()"})
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
# @app.post("/_delete_webhook")
# async def delete_webhook():
#     try:
#         # Webhookni tozalash
#         await bot.delete_webhook(drop_pending_updates=True)
#         return JSONResponse({"ok": True, "message": "Webhook deleted"})
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
