from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import app.database as db
from app.middlewares import TestMiddleware

admin_router = Router()

admin_router.message.middleware(TestMiddleware())

# Список ID админов
ADMINS = db.get_admins_id()
print(f"Список ID админов: {ADMINS}")


# @admin_router.message(Command('AdminMenu'))
# async def admin_help_handler(message: Message):
#     """Отправляет список доступных команд для администратора"""
#     if str(message.from_user.id) in ADMINS:
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

@admin_router.callback_query(F.data == 'open_admin_menu')
async def open_admin_menu(callback: CallbackQuery):
    """Отправляет список доступных команд для администратора по нажатию кнопки"""
    if str(callback.message.chat.id) in ADMINS:
        await callback.message.answer(
            "ℹ️ *Доступные команды для администратора:*\n"
            "/ShowClients - Список клиентов\n"
            "/AddClient - Добавление клиента\n"
            "/DeleteClient - Удаление клиента\n"
            "/TaskMenu - Меню планировщика задач",
            parse_mode="Markdown"
        )
        await callback.answer('')
    else:
        await callback.message.answer("❌ У вас нет прав администратора!")

@admin_router.message(Command("ShowClients"))
async def show_clients(message: Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer("Тут будет список клиентов")
    else:
        await message.answer("❌ У вас нет прав администратора!")

@admin_router.message(Command("AddClient"))
async def add_client(message: Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer("Тут добавить клиента")
    else:
        await message.answer("❌ У вас нет прав администратора!")

@admin_router.message(Command("DeleteClient"))
async def delete_client(message: Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer("Тут удалить клиента")
    else:
        await message.answer("❌ У вас нет прав администратора!")

@admin_router.message(Command("TaskMenu"))
async def create_news(message: Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer("Тут меню для работы с задачами")
    else:
        await message.answer("❌ У вас нет прав администратора!")

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


