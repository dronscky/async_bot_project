import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

from config import BOT_TOKEN, AV_ID
import voting

PROXY_URL="http://45.147.199.142:7052"

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, proxy=PROXY_URL, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

async def send_to_start(dp):
	await bot.send_message(chat_id=AV_ID, text="!!!Бот запущен!!!")



# @dp.message_handler()
# async def echo(message: Message):
# 	text = f"Вы написали {message.text}"
# 	await bot.send_message(chat_id=message.from_user.id, text=text)
# 	# await message.answer(text=text)

@dp.message_handler(commands=['v'])
async def add_voting(message: Message):
	mes = message.text
	res = voting.add_vote(mes)
	if res == 'Error':
		text = "Ошибка данных"
	else:
		text = f"Изменения внесены, общее число проголосовавших по адресу {res[0]} ({res[1]}%). По участку {res[2]}%."
	await bot.send_message(chat_id=message.from_user.id, text=text)

@dp.message_handler(commands=['c'])
async def change_popul(message: Message):
	mes = message.text
	res = voting.ch_num_people(mes)
	if res == 'Error':
		text = "Ошибка данных"
	else:
		text = "Изменения внесены"
	await bot.send_message(chat_id=message.from_user.id, text=text)


if __name__ == "__main__":
	
	executor.start_polling(dp, on_startup=send_to_start)