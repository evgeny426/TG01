import requests
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN, WEATHER_API

def get_weather(city):
    api_key = WEATHER_API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('weather'))
async def weather_command(message: Message):
    await message.answer('Введите название города, для которого хотите узнать погоду.')


@dp.message(Command('help'))
async def help_command(message: Message):
    await message.answer('Этот бот умеет выполнять команды:\n/start\n/help\n/weather')

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer('Привет! Я бот, который умеет показывать погоду в любом городе. Используйте команду /weather, чтобы начать.')

@dp.message()
async def get_city_weather(message: Message):
    city = message.text
    weather = get_weather(city)

    if weather.get("cod") != 200:
        await message.answer(f'Ошибка: {weather.get("message", "Неизвестная ошибка")}. Попробуйте другой город.')
        return

    temp = weather["main"]["temp"]
    humidity = weather["main"]["humidity"]
    wind_speed = weather["wind"]["speed"]
    wind_deg = weather["wind"]["deg"]
    clouds = weather["clouds"]["all"]

    # Преобразуем направление ветра в текст
    wind_direction = ""
    if 0 <= wind_deg < 45:
        wind_direction = "Северо-восток"
    elif 45 <= wind_deg < 90:
        wind_direction = "Юго-восток"
    elif 90 <= wind_deg < 135:
        wind_direction = "Юг"
    elif 135 <= wind_deg < 180:
        wind_direction = "Юго-запад"
    elif 180 <= wind_deg < 225:
        wind_direction = "Запад"
    elif 225 <= wind_deg < 270:
        wind_direction = "Северо-запад"
    elif 270 <= wind_deg < 315:
        wind_direction = "Север"
    else:
        wind_direction = "Северо-восток"

    await message.answer(
        f'Погода в городе {city}:\n'
        f'Температура: {temp}°C\n'
        f'Облачность: {clouds}%\n'
        f'Влажность: {humidity}%\n'
        f'Скорость ветра: {wind_speed} м/с\n'
        f'Направление ветра: {wind_direction}'
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())