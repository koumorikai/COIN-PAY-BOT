from supabase import create_client, Client
from bot.config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

async def get_or_create_user(telegram_id: int, username: str, first_name: str):
    res = supabase.table("users").select("*").eq("telegram_id", telegram_id).execute()
    if not res.data:
        user_data = {
            "telegram_id": telegram_id,
            "username": username,
            "first_name": first_name,
        }
        res = supabase.table("users").insert(user_data).execute()
    return res.data[0]