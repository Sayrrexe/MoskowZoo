from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from config import URL

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Пройти Викторину'),],
    [KeyboardButton(text='Преимущества статуса опекуна')],
    [KeyboardButton(text='Что такое Опекунство?')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

start_quiz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Начать Викторину!')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

start_quiz_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Начать!')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

answers_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='А'), KeyboardButton(text='Б')],
    [KeyboardButton(text='В'), KeyboardButton(text='Г')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

async def share_kb(key):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Поделится!', callback_data=f'share_{key}'))
    keyboard.add(InlineKeyboardButton(text='начать с начала', callback_data='menu'))
    return keyboard.adjust(1).as_markup()

link_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пройти тест!", url=URL,)]
    ]
)