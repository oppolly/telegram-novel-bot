import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Осмотреться", callback_data="look"))
    keyboard.add(InlineKeyboardButton("Выйти", callback_data="exit"))

    await message.answer("Ты просыпаешься в тёмной комнате.", reply_markup=keyboard)

@dp.callback_query_handler()
async def handle_callback(callback: types.CallbackQuery):
    if callback.data == "look":
        await callback.message.edit_text("Ты видишь старый сундук.")
    elif callback.data == "exit":
        await callback.message.edit_text("Ты выходишь в коридор.")

if __name__ == "__main__":
    executor.start_polling(dp) 
