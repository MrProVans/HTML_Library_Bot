from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import app.database as db

admin_router = Router()

# Список ID админов
ADMINS = db.get_admins_id()
print(f"Список ID админов: {ADMINS}")


# @admin_router.message(Command('AdminHelp'))
# async def help_handler(message: Message):
#     await message.reply(
#         "ℹ️ *Доступные команды:*\n"
#         "/AddUser - Добавление пользователя\n"
#         "/RemoveUser - Удаление пользователя",
#         parse_mode="Markdown"
#     )
#
#
# @admin_router.message(Command("AddUser"))
# async def add_user_handler(message: Message):
#     if not is_admin(message.from_user.id):
#         return await message.answer("❌ У вас нет прав для выполнения этой команды.")
#
#     args = message.text.split()
#     if len(args) != 2 or not args[1].isdigit():
#         return await message.answer("⚠️ Использование: /AddUser <id>")
#
#     user_id = int(args[1])
#     await db.users.insert_one({"user_id": user_id})
#     await message.answer(f"✅ Пользователь {user_id} добавлен!")
#
#
# @admin_router.message(Command("RemoveUser"))
# async def remove_user_handler(message: Message):
#     if not is_admin(message.from_user.id):
#         return await message.answer("❌ У вас нет прав для выполнения этой команды.")
#
#     args = message.text.split()
#     if len(args) != 2 or not args[1].isdigit():
#         return await message.answer("⚠️ Использование: /RemoveUser <id>")
#
#     user_id = int(args[1])
#     result = await db.users.delete_one({"user_id": user_id})
#     if result.deleted_count:
#         await message.answer(f"✅ Пользователь {user_id} удален!")
#     else:
#         await message.answer("⚠️ Пользователь не найден.")
#
#
#
# @admin_router.message(Command('AdminHelp'))
# async def admin_help_handler(message: Message):
#     """Отправляет список доступных команд для администратора"""
#     if is_admin(message.from_user.id):
#         await message.reply(
#             "ℹ️ *Доступные команды для администратора:*\n"
#             "/AddUser - Добавление пользователя\n"
#             "/RemoveUser - Удаление пользователя\n"
#             "/AddCode - Добавить HTML/CSS код\n"
#             "/EditCode - Редактировать код\n"
#             "/DeleteCode - Удалить код",
#             parse_mode="Markdown"
#         )
#     else:
#         await message.reply("❌ У вас нет прав администратора!")

