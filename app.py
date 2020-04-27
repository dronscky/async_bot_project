import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

from config import BOT_TOKEN

PROXY_URL="http://54.37.14.65:3132"

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, proxy=PROXY_URL, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

@dp.message_handler()
async def echo(message: Message):
	text = f"Вы написали {message.text}"
	await bot.send_message(chat_id=message.from_user.id, text=text)
	# await message.answer(text=text)

if __name__ == "__main__":
	
	executor.start_polling(dp)