from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

admin = Router()

@admin.message(Command("/adminpanel"))
async def cmd_panel(message: Message):
  await message.answer("Админ-панель")