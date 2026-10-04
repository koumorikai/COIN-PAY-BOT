import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot.config import BOT_TOKEN
from bot.handlers import router

logging.basicConfig(level=logging.INFO)

async def main():
    if not BOT_TOKEN:
        print("ОШИБКА: BOT_TOKEN пустой!")
        return

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрируем роутер с командами
    dp.include_router(router)

    print("--- БОТ УСПЕШНО ИНИЦИАЛИЗИРОВАН И ЗАПУЩЕН ---")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())