import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import asyncio
from aiogram.filters import CommandStart
from aiogram.types import Message

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
  await message.answer(text="Привет!")
  
  
@dp.message()
async def echo(message: Message):
    await message.answer('Это неизвестная команда.')


async def main():
  await dp.start_polling(bot)
  

if __name__ == '__main__':
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print("Бот отключен")