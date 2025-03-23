from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import Message


# Политика конфиденциальности
inline_privacy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Открыть', url='https://docs.google.com/document/d/1xlgO_JlneAiabA7KX-nqhMYTW0jb_JLUAfC9x2TUSFo/edit?tab=t.0')]])

# Приобрести доступ
buy_access = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Получить доступ', url="https://t.me/tyomchikxxx")]])

# Меню клиента
client_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Меню клиента", callback_data="open_client_menu")]
    ]
)

# Меню админа
admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Меню админа", callback_data="open_admin_menu")]
    ]
)

# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Каталог')],
#     [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
# ],
#         resize_keyboard=True,
#         input_field_placeholder='Выберите пункт меню')

# menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Каталог', callback_data='catalog'),],
#     [InlineKeyboardButton(text='Корзина', callback_data='2'),
#     InlineKeyboardButton(text='Контакты', callback_data='3'),]
# ])

# settings = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='TG', url='https://t.me/isklochkov')],
# ])
#
# cars = ['Tesla', 'Mercedes', 'Bmw']
#
# async def reply_cars():
#     keyboard = ReplyKeyboardBuilder()
#     for car in cars:
#         keyboard.add(KeyboardButton(text=car))
#     return keyboard.adjust(2).as_markup(resize_keyboard=True)
#
# async def inline_cars():
#     keyboard = InlineKeyboardBuilder()
#     for car in cars:
#         keyboard.add(InlineKeyboardButton(text=car, callback_data=f'car_{car}'))
#     return keyboard.adjust(2).as_markup(resize_keyboard=True)