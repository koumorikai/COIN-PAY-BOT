import asyncio
import os
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

async def main():
    if not BOT_TOKEN:
        print("ОШИБКА: BOT_TOKEN пустой!")
        return

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    print("--- БОТ УСПЕШНО ИНИЦИАЛИЗИРОВАН И ЗАПУЩЕН ---")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())