# 🌦️ Weather Telegram Bot

Этот Telegram-бот предоставляет актуальную информацию о погоде в любом городе мира, используя OpenWeatherMap API.

## 🛠️ Технологии
- Python 3.9+
- [aiogram](https://docs.aiogram.dev/) (асинхронный фреймворк для Telegram ботов)
- [OpenWeatherMap API](https://openweathermap.org/api)

## ⚙️ Установка

1. Клонируйте репозиторий:
  git clone https://github.com/ваш-репозиторий/weather-bot.git
  cd weather-bot

2. Установите зависимости:
    pip install -r requirements.txt

3. Создайте файл config.py в корне проекта:
  TOKEN = "ваш_telegram_bot_token"
  WEATHER_API = "ваш_openweathermap_api_key"

## 🚀 Запуск
  python main.py

## 📋 Команды бота
  /start - Приветственное сообщение
  /help - Список доступных команд
  /weather - Запросить погоду (бот попросит ввести город)

## 📌 Особенности
  Показывает температуру (°C), влажность, облачность
  Определяет направление ветра (8 румбов)
  Обрабатывает ошибки (неверные названия городов)
