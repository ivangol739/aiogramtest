import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
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
  
  
@dp.message()
async def echo(message: Message):
    await message.answer('Это неизвестная команда.')


async def main():
  await dp.start_polling(bot)
  

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print("Бот отключен")