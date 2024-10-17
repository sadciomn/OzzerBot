import asyncio
from config.config import hello_sticker
from config.token import api_token
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters.command import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.context import FSMContext
from functions.weather import weather_check
from states.steps import Steps


logging.basicConfig(level=logging.INFO)
bot = Bot(token=api_token, default=DefaultBotProperties(parse_mode="html"))
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(msg: types.Message):
    await msg.answer_sticker(hello_sticker)
    await msg.answer(
        f"Привет, <b>{msg.from_user.first_name}</b> 🐶 Пока что я умею только выводить погоду.\
              Введи название города на любом языке, а я выдам погоду"
    )


@dp.message()
async def show_weather(msg: types.Message, state: FSMContext):
    weather = weather_check(msg.text)
    await msg.answer(
        f"Регион: <b>{weather[0]}</b>\nТемпература: <b>{weather[1]}°C - {weather[2]}</b>"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
