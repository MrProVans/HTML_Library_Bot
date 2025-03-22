import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers.common_handlers import router
from app.handlers.admin_handlers import admin_router

from app.database import db


# async def test_db():
#     try:
#         count = await db.users.count_documents({})
#         print(f"✅ Подключение к MongoDB успешно! Количество пользователей: {count}")
#     except Exception as e:
#         print(f"❌ Ошибка подключения к MongoDB: {e}")

async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(admin_router)
    # await test_db()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")