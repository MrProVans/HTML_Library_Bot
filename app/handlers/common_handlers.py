from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database as db
from app.middlewares import TestMiddleware

common_router = Router()

common_router.message.middleware(TestMiddleware())

# class Reg(StatesGroup):
#     name = State()
#     number = State()


@common_router.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! 🤩\n\nНаш сервис помогает дизайнерам и сайтологам,"
                         f" предоставляя HTML и CSS-коды. \n\nТвой ID: {message.from_user.id} "
                         f"\n\nИспользуй /help для навигации."
                         )

@common_router.message(Command('privacy'))
async def help_handler(message: Message):
    await message.answer(
        "Политика конфиденциальности 👇",
        reply_markup=kb.inline_privacy
    )

@common_router.message(Command('help'))
async def help_handler(message: Message):
    """Определяет роль пользователя и вызывает соответствующую команду"""
    if str(message.from_user.id) in db.get_clients_id():
        await message.bot.send_message(message.chat.id, f"Поздравляем с приобретением доступа к полному функционалу "
                                                        f"нашего сервиса! \nМы старались, надеемся, что этот бот принесет много пользы)"
                                                        f"\nПодробнее тут 👉 /ClientMenu")
    elif str(message.from_user.id) in db.get_admins_id():
        await message.bot.send_message(message.chat.id, f"Здарова, {message.from_user.first_name}!\n"
                                                        f"Че ты, команды забыл?) \nЛадно, посмотри тут 👉 /AdminMenu")
    else:
        await message.bot.send_message(message.chat.id, f"Получите доступ 👇", reply_markup=kb.buy_access)

# @common_router.message(Command('help'))
# async def help_handler(message: Message):
#     await message.reply(
#         "ℹ️ *Доступные команды:*\n"
#         "/start - Начать работу с ботом\n"
#         "/menu - Главное меню\n"
#         "/help - Помощь по командам",
#         parse_mode="Markdown"
#     )
# @common_router.message(Command("menu"))
# async def menu_handler(message: Message):
#     await message.answer("📌 Главное меню:", reply_markup=kb.menu_keyboard)
#
#
#
# @common_router.message(Command('UserHelp'))
# async def user_help_handler(message: Message):
#     """Отправляет список команд для обычного пользователя"""
#     await message.reply(
#         "ℹ️ *Доступные команды для пользователя:*\n"
#         "/GetCode - Получить HTML/CSS код\n"
#         "/ListCodes - Список доступных кодов",
#         parse_mode="Markdown"
#     )

# @router.message(Command("get_photo"))
# async def get_photo(message: Message):
#     await message.answer_photo(photo="ссылка", caption="описание к картинке")
#
# @router.message(F.text == "А?")
# async def cmd_help(message: Message):
#     await message.answer("А?")

# @router.callback_query(F.data == 'catalog')
# async def callback_query(callback: CallbackQuery):
#     await callback.answer('Вы выбрали каталог')
#     await callback.message.edit_text('Привет!', reply_markup=await kb.inline_cars())
#
#
# @router.message(Command('reg'))
# async def reg_one(message: Message, state: FSMContext):
#     await state.set_state(Reg.name)
#     await message.answer('Введите Ваше имя')
#
# @router.message(Reg.name)
# async def reg_two(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#
#     await state.set_state(Reg.number)
#     await message.answer('Введите номер телефона')
#
# @router.message(Reg.number)
# async def two_three(message: Message, state: FSMContext):
#     await state.update_data(number=message.text)
#     data = await state.get_data()
#     await message.answer(f'Регистрация завершена. Имя: {data["name"]}, Номер: {data["number"]}')
#     await state.clear()