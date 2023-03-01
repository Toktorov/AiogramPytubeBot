from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

inline_buttons = [
    InlineKeyboardButton('Старт', callback_data='start'),
    InlineKeyboardButton('Помощь', callback_data='help'),
    InlineKeyboardButton('Скачать видео', callback_data='video'),
    InlineKeyboardButton('Скачать аудио', callback_data='audio')
]

button = InlineKeyboardMarkup().add(*inline_buttons)

share_keyboards = [
    KeyboardButton('Поделиться номером', request_contact=True),
    KeyboardButton('Отправить локацию', request_location=True)
]

share_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*share_keyboards)