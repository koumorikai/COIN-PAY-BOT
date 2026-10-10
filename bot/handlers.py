from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from bot.config import WEBAPP_URL
from bot.db import get_or_create_user

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    # Сохраняем или получаем пользователя в Supabase
    await get_or_create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username or "",
        first_name=message.from_user.first_name or ""
    )
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🛒 Открыть магазин", 
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ]
    ])
    
    await message.answer(
        f"Привет, {message.from_user.first_name}!\n\n"
        "Через нашего бота ты можешь пополнить **Steam**, купить **TikTok Coins** "
        "и оплатить другие цифровые услуги.\n\n"
        "Нажми кнопку ниже, чтобы открыть магазин:",
        reply_markup=kb,
        parse_mode="Markdown"
    )