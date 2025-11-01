from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from environs import Env

env = Env()
env.read_env()
TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = env.str("WEBHOOK_URL")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Salom! /start ishlayapti ✅")


@router.message(Command("help"))
async def cmd_start(message: Message):
    await message.answer("Yordaaam")


dp.include_router(router)

async def setup_webhook():
    await bot.set_webhook(
        url=WEBHOOK_URL,
        allowed_updates=["message", "callback_query"],
        drop_pending_updates=True,
    )
