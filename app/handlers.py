from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!", reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply("Это команда /help")

# @router.message(Command("get_photo"))
# async def get_photo(message: Message):
#     await message.answer_photo(photo="ссылка", caption="описание к картинке")

@router.message(F.text == "А?")
async def cmd_help(message: Message):
    await message.answer("А?")

@router.callback_query(F.data == 'catalog')
async def callback_query(callback: CallbackQuery):
    await callback.answer('Вы выбрали каталог')
    await callback.message.edit_text('Привет!', reply_markup=await kb.inline_cars())