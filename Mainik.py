import asyncio

from main import text_to_voice, create_response

from aiogram.types import FSInputFile
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

bot = Bot('7141146341:AAEzY5u7_suRTvd4cPA8Dh8p5vBtJVQEhf0')
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Я нейросеть с голосом! Задай любой вопрос, а я отвечу тебе голосом!")

@dp.message()
async def callbecker(message: Message):
    await message.answer('Генерирую ответ...')
    text_to_voice(create_response(message.text), 1)
    audio = FSInputFile('output.mp3')
    await bot.send_audio(message.chat.id, audio, title="<i>Ответ</i>", parse_mode='HTML', caption='Нейросеть')
           
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())


