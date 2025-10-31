from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from environs import Env

env = Env()
env.read_env()

TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = env.str("WEBHOOK_URL")  # masalan: https://yourapp.koyeb.app/webhook

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


async def setup_webhook():
    await bot.set_webhook(
        url=WEBHOOK_URL,
        allowed_updates=["message", "callback_query"],
        drop_pending_updates=True)
