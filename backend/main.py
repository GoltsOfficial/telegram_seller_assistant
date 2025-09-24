import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command

# Загружаем переменные окружения из файла .env (где будет лежать BOT_TOKEN)
load_dotenv()

# Создаем роутер
router = Router()


# Обработчик команды /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    # Текст с ссылкой на ваше мини-приложение
    # ВАЖНО: Замените "your_mini_app_url" на реальный URL вашего приложения после деплоя
    web_app_url = "https://your_mini_app_url.com"
    web_app = types.WebAppInfo(url=web_app_url)

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="✨ Заказать рекламу", web_app=web_app)]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "Добро пожаловать! Это сервис по заказу рекламы в нашем паблике.\n\n"
        "Нажмите кнопку ниже, чтобы открыть меню заказа.",
        reply_markup=keyboard
    )


# Обработчик команды /help
@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "Список команд:\n"
        "/start - Начать работу с ботом и открыть меню заказа.\n"
        "/help - Получить справку.\n\n"
        "Если у вас возникли проблемы с доступом к мини-приложению, свяжитесь с поддержкой."
    )
    await message.answer(help_text)


# Главная функция
async def main():
    # Получаем токен бота из переменных окружения
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("Не задан BOT_TOKEN в переменных окружения.")

    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.include_router(router)

    # Запускаем поллинг
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())