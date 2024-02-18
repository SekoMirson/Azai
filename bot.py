from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import re
from colorama import init, Fore
import sqlite3
import datetime
import requests
import json
import os
from pyee import EventEmitter

init(autoreset=True)

menu = """
                     Telegram AI Talking Bot: @azai_robot
                           Developer : sekomirson
"""

colored_menu = menu.replace("Telegram AI Talking Bot:", Fore.GREEN + "Telegram AI Talking Bot" + Fore.RESET + ": ") \
    .replace("@azai_robot", Fore.YELLOW + "@azai_robot" + Fore.RESET)
print(colored_menu)

# AIGram
Browser = {'user-agent': 'Azai_robot/1.0.1'}
Azai = Bot(token="Telegram Botun Tokenini yazin")
dp = Dispatcher(Azai)


def AdiDeyistir(text, eski, yeni):
    return text.replace(eski, yeni)

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer(f"Hello {message.from_user.first_name}!\n\ni am Azai. i like it talking.\n\n/dev - Developer about.")

@dp.message_handler(commands=['dev', 'developer'])
async def start_message(message: types.Message):
    await message.answer("Bot owner: @sekomirson\nGroup: https://t.me/+OgFRxkhXUGBkNTBi")

@dp.message_handler()
async def message_handler(message: types.Message):
    group_id = message.chat.id
    group_title = message.chat.title
    sender_username = message.from_user.username
    message_text = message.text
    zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    api = f"https://hercai.onrender.com/v3/hercai?question={message_text}"
    veriler = requests.get(api, headers=Browser)
    veri = json.loads(veriler.text)

    if message_text:
        text1 = veri["reply"]
        yeniAd = AdiDeyistir(text1, "GPT-4", "Azai")
        await dp.bot.send_message(group_id, yeniAd)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
