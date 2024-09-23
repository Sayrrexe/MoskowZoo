from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Пройти Викторину'),],
    [KeyboardButton(text='Преимущества статуса опекуна')],
    [KeyboardButton(text='Что такое Опекунство?')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

start_quiz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Начать Викторину!')]
])

start_quiz_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Начать!')]
])

answers_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='А'), KeyboardButton(text='Б')],
    [KeyboardButton(text='В'), KeyboardButton(text='Г')]
])