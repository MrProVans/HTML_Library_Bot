import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!")

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply("Это команда /help")

# @dp.message(Command("get_photo"))
# async def get_photo(message: Message):
#     await message.answer_photo(photo="ссылка", caption="описание к картинке")

@dp.message(F.text == "А?")
async def cmd_help(message: Message):
    await message.answer("А?")

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")