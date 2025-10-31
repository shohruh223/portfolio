# from contextlib import asynccontextmanager
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# import asyncio
# from environs import Env
#
# env = Env()
# env.read_env()
#
# TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
# TELEGRAM_CHAT_ID = env.int("TELEGRAM_CHAT_ID")
# bot = Bot(token=TELEGRAM_BOT_TOKEN)
# dp = Dispatcher()
#
# @dp.message(Command("start"))
# async def start_command(msg: types.Message):
#     await msg.answer("Salom! Bot ishga tushdi ✅")
#
#
# @asynccontextmanager
# async def lifespan(app):
#     # botni fon rejimda polling qilish
#     task = asyncio.create_task(dp.start_polling(bot))
#     yield
#     task.cancel()
#     await bot.session.close()
#
