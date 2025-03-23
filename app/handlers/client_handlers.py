from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import app.database as db

client_router = Router()

# Список ID клиентов
CLIENTS = db.get_clients_id()
print(f"Список ID клиентов: {CLIENTS}")


@client_router.message(Command('ClientMenu'))
async def admin_help_handler(message: Message):
    """Отправляет список доступных команд для администратора"""
    if str(message.from_user.id) in CLIENTS:
        await message.reply(
            "ℹ️ *Доступные команды для клиента:*\n",
            parse_mode="Markdown"
        )
    else:
        await message.reply("❌ У вас нет прав администратора!")