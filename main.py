import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers.common_handlers import common_router
from app.handlers.admin_handlers import admin_router
from app.handlers.client_handlers import client_router


from app.database import get_count_admins, get_count_clients

async def db_connection_info():
    """Проверка подключения БД к сервису."""
    try:
        print(f"""✅ Подключение к MongoDB успешно! 
Количество пользователей: clients - {get_count_clients()}, admins - {get_count_admins()}.
Успехов в разработке и пользовании сервисом!""")
    except Exception as e:
        print(f"❌ Ошибка подключения к MongoDB: {e}")


async def main():
    """Сердце сервиса."""
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(common_router)
    dp.include_router(admin_router)
    dp.include_router(client_router)
    await db_connection_info()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")