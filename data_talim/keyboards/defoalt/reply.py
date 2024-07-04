from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder,ReplyKeyboardMarkup


phone_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📞telefon raqam jonatish☎️',request_contact=True)]
],
                               resize_keyboard=True,one_time_keyboard=True)

submit_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='✅Xa✅'),KeyboardButton(text='❌Yoq❌')]
],resize_keyboard=True)
