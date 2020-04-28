import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

from config import BOT_TOKEN, AV_ID

PROXY_URL="http://197.216.2.18:8080"

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, proxy=PROXY_URL, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

async def send_to_start(dp):
	await bot.send_message(chat_id=AV_ID, text="!!!Бот запущен!!!")



@dp.message_handler()
async def echo(message: Message):
	text = f"Вы написали {message.text}"
	await bot.send_message(chat_id=message.from_user.id, text=text)
	# await message.answer(text=text)

if __name__ == "__main__":
	
	executor.start_polling(dp, on_startup=send_to_start)