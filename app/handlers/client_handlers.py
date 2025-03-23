from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import app.database as db

client_router = Router()

# Список ID клиентов
CLIENTS = db.get_clients_id()
print(f"Список ID клиентов: {CLIENTS}")


# @client_router.message(Command('ClientMenu'))
# async def admin_help_handler(message: Message):
#     """Отправляет список доступных команд для администратора"""
#     if str(message.from_user.id) in CLIENTS:
#         await message.reply(
#             "ℹ️ *Доступные команды для клиента:*\n"
#             "Я хз что тут будет\n",
#             parse_mode="Markdown"
#         )
#     else:
#         await message.reply("❌ У вас нет прав администратора!")

@client_router.callback_query(F.data == 'open_client_menu')
async def open_client_menu(callback: CallbackQuery):
    """Отправляет список доступных команд для администратора по нажатию кнопки"""
    if str(callback.message.chat.id) in CLIENTS:
        await callback.message.answer(
            "ℹ️ *Доступные команды для клиента:*\n"
            "Я хз что тут будет\n",
            parse_mode="Markdown"
        )
        await callback.answer('')
    else:
        await callback.message.answer("❌ У вас нет прав клиента!")
        await callback.answer('')