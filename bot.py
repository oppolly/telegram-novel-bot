import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Осмотреться", callback_data="look")],
        [InlineKeyboardButton(text="Выйти", callback_data="exit")]
    ])

    await message.answer("Ты просыпаешься в тёмной комнате.", reply_markup=keyboard)

@dp.callback_query()
async def handle_callback(callback):
    if callback.data == "look":
        await callback.message.edit_text("Ты видишь старый сундук.")
    elif callback.data == "exit":
        await callback.message.edit_text("Ты выходишь в коридор.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
