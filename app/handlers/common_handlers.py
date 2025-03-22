from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.middlewares import TestMiddleware

router = Router()

router.message.middleware(TestMiddleware())

# class Reg(StatesGroup):
#     name = State()
#     number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! \nТвой ID: {message.from_user.id}")

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply("Это команда /help")

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