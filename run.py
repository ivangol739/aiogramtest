import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
  await message.reply("Привет!")
  await message.answer("Как дела ?")
  # await message.answer_photo(photo='https://sudoteach.com/static/assets/img/aiogram-banner.jpg',
  #                              caption='Картинка')


@dp.message(Command('help'))
async def cmd_help(message: Message):
  await message.answer(f"{message.from_user.first_name}, вам нужна помощь ?")
  
  
@dp.message(F.text == "привет")
async def echo(message: Message):
  await message.answer('Привет!!!')
  await message.answer(f'Ваш ID: {message.from_user.id}')


@dp.message(F.photo)
async def echo(message: Message):
  photo_id = message.photo[-1].file_id
  await message.answer_photo(photo=photo_id)
  
  
@dp.message(F.document)
async def echo(message: Message):
  await message.answer_document(document=message.document.file_id)
  
  
@dp.message(F.audio)
async def echo(message: Message):
  await message.answer_audio(audio=message.audio.file_id)
  
  
@dp.message(F.animation)
async def echo(message: Message):
  await message.answer_animation(animation=message.animation.file_id)
  await message.answer("Вы прислали Гифку")
  

@dp.message(F.from_user.id == 293882390)
async def echo(message: Message):
  await message.answer(f"Написал юзер с ID {message.from_user.id}")


async def main():
  await dp.start_polling(bot)
  

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print("Бот отключен")