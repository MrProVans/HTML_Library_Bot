import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["html_library"]

# Коллекции
# admins = db["admins"]
# clients = db["clients"]
# html_codes = db["html-codes"]
# css_codes = db["css-codes"]


def get_admins_id():
    """Получает список ID всех админов из базы данных"""
    list_admins = db.admins.find({}, {"adminId": 1})
    return [admin["adminId"] for admin in list_admins]

def get_clients_id():
    """Получает список ID всех клиентов из базы данных"""
    list_clients = db.clients.find({}, {"clientId": 1})
    return [client["clientId"] for client in list_clients]

def get_count_admins():
    """Получает количество всех админов из базы данных"""
    return db.admins.count_documents({})

def get_count_clients():
    """Получает количество всех юзеров из базы данных"""
    return db.clients.count_documents({})


