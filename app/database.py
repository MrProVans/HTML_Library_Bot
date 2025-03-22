import os
from pymongo import MongoClient
from dotenv import load_dotenv


MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "html_library"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Коллекции
admins = db["admins"]
users = db["users"]
html_codes = db["html-codes"]
css_codes = db["css-codes"]

async def init_db():
    """Инициализация базы данных, создание индексов"""
    await users.create_index("user_id", unique=True)
    await admins.create_index("admin_id", unique=True)
    print("✅ База данных инициализирована!")

