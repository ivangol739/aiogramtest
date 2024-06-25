from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
  [KeyboardButton(text='Корзина'),
  KeyboardButton(text='Каталог')],
  [KeyboardButton(text='Контакты', request_contact=True)]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')