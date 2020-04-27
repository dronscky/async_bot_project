import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

from config import BOT_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

@dp.mesage_handler()
async def echo(message: Message):
	text = f"Вы написали {message.text}"
	await bot.send_message(chat_id=message.from_user.id, text=text)
	# await message.answer(text=text)

if __name__ == "__main__":
	
	executor.start_polling(dp)