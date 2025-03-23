from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

import app.database as db
import app.keyboards as kb
from app.middlewares import TestMiddleware

admin_router = Router()

admin_router.message.middleware(TestMiddleware())

# Список ID админов
ADMINS = db.get_admins_id()
print(f"Список ID админов: {ADMINS}")


class TaskState(StatesGroup):
    waiting_for_task_text = State()
    waiting_for_task_edit = State()
    waiting_for_task_delete = State()


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
            "/DeleteClient - Удаление клиента\n",
            "/AddCode - Добавить HTML/CSS код\n"
            "/EditCode - Редактировать код\n"
            "/DeleteCode - Удалить код\n"
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
async def task_menu(message: Message):
    """Выводит меню управления задачами"""
    if str(message.from_user.id) in ADMINS:
        await message.answer("📌 *Меню управления задачами:*", reply_markup=kb.task_menu,
                             parse_mode="Markdown")
    else:
        await message.answer("❌ У вас нет прав администратора!")

# ➕ Добавление задачи
@admin_router.callback_query(F.data == "add_task")
async def add_task_callback(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("📝 Введите текст новой задачи:")
    await state.set_state(TaskState.waiting_for_task_text)
    await callback.answer()

@admin_router.message(TaskState.waiting_for_task_text)
async def process_task_text(message: Message, state: FSMContext):
    db.add_task(message.text)
    await message.answer("✅ Задача добавлена!", reply_markup=kb.task_menu)
    await state.clear()

# ✏ Редактирование задачи
@admin_router.callback_query(lambda c: c.data == "edit_task")
async def edit_task_callback(callback: CallbackQuery, state: FSMContext):
    tasks = db.get_tasks()
    if not tasks:
        await callback.message.answer("❌ У вас нет задач.")
        return

    buttons = [InlineKeyboardButton(text=t['text'], callback_data=f"edit_{t['_id']}") for t in tasks]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons])
    await callback.message.answer("✏ Выберите задачу для редактирования:", reply_markup=keyboard)
    await callback.answer()

@admin_router.callback_query(lambda c: c.data.startswith("edit_"))
async def process_task_edit(callback: CallbackQuery, state: FSMContext):
    task_id = callback.data.split("_")[1]
    await state.update_data(task_id=task_id)
    await callback.message.answer("✏ Введите новый текст задачи:")
    await state.set_state(TaskState.waiting_for_task_edit)
    await callback.answer()

@admin_router.message(TaskState.waiting_for_task_edit)
async def save_task_edit(message: Message, state: FSMContext):
    data = await state.get_data()
    db.edit_task(data["task_id"], message.text)
    await message.answer("✅ Задача обновлена!", reply_markup=kb.task_menu)
    await state.clear()

# 🗑 Удаление задачи
@admin_router.callback_query(lambda c: c.data == "delete_task")
async def delete_task_callback(callback: CallbackQuery, state: FSMContext):
    tasks = db.get_tasks()
    if not tasks:
        await callback.message.answer("❌ Нет задач.")
        return

    buttons = [InlineKeyboardButton(text=t['text'], callback_data=f"delete_{t['_id']}") for t in tasks]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons])
    await callback.message.answer("🗑 Выберите задачу для удаления:", reply_markup=keyboard)
    await callback.answer()

@admin_router.callback_query(lambda c: c.data.startswith("delete_"))
async def process_task_delete(callback: CallbackQuery):
    task_id = callback.data.split("_")[1]
    db.delete_task(task_id)
    await callback.message.answer("✅ Задача удалена!", reply_markup=kb.task_menu)
    await callback.answer()

# 📋 Просмотр всех задач
@admin_router.callback_query(lambda c: c.data == "view_tasks")
async def view_tasks_callback(callback: CallbackQuery):
    tasks = db.get_tasks()
    if not tasks:
        await callback.message.answer("📭 Нет задач.")
    else:
        text = "\n".join([f"📌 {t['text']} (🗓 {t['deadline']})" for t in tasks])
        await callback.message.answer(f"📋 *Задачи:*\n{text}", parse_mode="Markdown")
    await callback.answer()

# ✅ Отметить задачу выполненной
@admin_router.callback_query(lambda c: c.data == "complete_task")
async def complete_task_callback(callback: CallbackQuery):
    tasks = db.get_tasks()
    if not tasks:
        await callback.message.answer("✅ Все задачи выполнены!")
        return

    buttons = [InlineKeyboardButton(text=t['text'], callback_data=f"complete_{t['_id']}") for t in tasks]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons])
    await callback.message.answer("✅ Выберите задачу для отметки выполненной:", reply_markup=keyboard)
    await callback.answer()

@admin_router.callback_query(lambda c: c.data.startswith("complete_"))
async def process_task_complete(callback: CallbackQuery):
    task_id = callback.data.split("_")[1]
    db.complete_task(task_id)
    await callback.message.answer("✅ Задача выполнена и удалена!", reply_markup=kb.task_menu)
    await callback.answer()
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


