import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime, timedelta
from bson import ObjectId

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

def add_task(text):
    deadline = datetime.now() + timedelta(days=7)  # Дедлайн через 7 дней
    db.tasks.insert_one({"text": text, "deadline": deadline, "completed": False})

def get_tasks():
    return list(db.tasks.find({"completed": False}))

def edit_task(task_id, new_text):
    db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": {"text": new_text}})

def delete_task(task_id):
    db.tasks.delete_one({"_id": ObjectId(task_id)})

def complete_task(task_id):
    db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": {"completed": True}})

def auto_update_tasks():
    """Автоматически переносит просроченные задачи и напоминает за день до дедлайна"""
    now = datetime.now()
    for task in db.tasks.find({"completed": False}):
        deadline = task["deadline"]
        if deadline < now:  # Просроченная задача
            new_deadline = deadline + timedelta(days=1)
            db.tasks.update_one({"_id": task["_id"]}, {"$set": {"deadline": new_deadline}})
            print(f"⏳ Задача {task['_id']} перенесена на {new_deadline.strftime('%Y-%m-%d')}")
        elif (deadline - now).days == 1:  # Напоминание за день до дедлайна
            print(f"🔔 Напоминание! Завтра дедлайн по задаче: {task['text']}")


