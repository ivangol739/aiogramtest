from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message
from aiogram import F, Router
from aiogram.enums import ChatAction
import asyncio


import app.keyboards as kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
  await message.bot.send_chat_action(chat_id=message.from_user.id,
                                     action=ChatAction.TYPING)
  await asyncio.sleep(2)
  await message.reply("Привет!", reply_markup=kb.main)
  await message.answer("Как дела ?")
  # await message.answer_photo(photo='https://sudoteach.com/static/assets/img/aiogram-banner.jpg',
  #                              caption='Картинка')


@router.message(Command('test'))
async def cmd_test(message: Message):
  await message.bot.send_message(chat_id=message.chat.id,
                                 message_thread_id=message.message_thread_id,
                                 test="OK")


@router.message(Command('help'))
async def cmd_help(message: Message):
  await message.answer(f"{message.from_user.first_name}, вам нужна помощь ?")
  
  
@router.message(Command("get"))
async def cmd_get(message: Message, command: CommandObject):
  if not command.args:
    await message.answer("Аргументы не переданы")
    return
  try:
    value1, value2 = command.args.split(' ', maxsplit=1)
    await message.answer(f"Вы ввели команду get с аргументом {value1} {value2}")
  except:
    await message.answer("Были введены неправильные аргументы")
  
  
@router.message(F.text == "привет")
async def echo(message: Message):
  await message.answer('Привет!!!')
  await message.answer(f'Ваш ID: {message.from_user.id}')


@router.message(F.photo)
async def echo(message: Message):
  photo_id = message.photo[-1].file_id
  await message.answer_photo(photo=photo_id)
  
  
@router.message(F.document)
async def echo(message: Message):
  await message.answer_document(document=message.document.file_id)
  
  
@router.message(F.audio)
async def echo(message: Message):
  await message.answer_audio(audio=message.audio.file_id)
  
  
@router.message(F.animation)
async def echo(message: Message):
  await message.answer_animation(animation=message.animation.file_id)
  await message.answer("Вы прислали Гифку")
  

@router.message(F.from_user.id == 293882390)
async def echo(message: Message):
  await message.answer(f"Написал юзер с ID {message.from_user.id}")