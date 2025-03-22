from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest

from app.database import db

admin_router = Router()

# Список ID админов (пока временно, позже из БД)
ADMINS = {1925398093, 469301996, 690930776}


# Проверка прав администратора
def is_admin(user_id):
    return user_id in ADMINS


@admin_router.message(Command('AdminHelp'))
async def help_handler(message: Message):
    await message.reply(
        "ℹ️ *Доступные команды:*\n"
        "/AddUser - Добавление пользователя\n"
        "/RemoveUser - Удаление пользователя",
        parse_mode="Markdown"
    )


@admin_router.message(Command("AddUser"))
async def add_user_handler(message: Message):
    if not is_admin(message.from_user.id):
        return await message.answer("❌ У вас нет прав для выполнения этой команды.")

    args = message.text.split()
    if len(args) != 2 or not args[1].isdigit():
        return await message.answer("⚠️ Использование: /AddUser <id>")

    user_id = int(args[1])
    await db.users.insert_one({"user_id": user_id})
    await message.answer(f"✅ Пользователь {user_id} добавлен!")


@admin_router.message(Command("RemoveUser"))
async def remove_user_handler(message: Message):
    if not is_admin(message.from_user.id):
        return await message.answer("❌ У вас нет прав для выполнения этой команды.")

    args = message.text.split()
    if len(args) != 2 or not args[1].isdigit():
        return await message.answer("⚠️ Использование: /RemoveUser <id>")

    user_id = int(args[1])
    result = await db.users.delete_one({"user_id": user_id})
    if result.deleted_count:
        await message.answer(f"✅ Пользователь {user_id} удален!")
    else:
        await message.answer("⚠️ Пользователь не найден.")
