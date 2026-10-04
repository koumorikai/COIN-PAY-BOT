import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot.config import BOT_TOKEN
from bot.handlers import router
import os

async def main():
    logging.basicConfig(level=logging.INFO)
    BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
    dp = Dispatcher()
    dp.include_router(router)
    
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())