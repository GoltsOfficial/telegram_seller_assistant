import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command

load_dotenv()

# Инициализация бота
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()
router = Router()
dp.include_router(router)


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    # URL вашего GitHub Pages (ЗАМЕНИТЕ на ваш)
    web_app_url = "https://yourusername.github.io/your-repo-name/"
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


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "Список команд:\n"
        "/start - Начать работу с ботом и открыть меню заказа.\n"
        "/help - Получить справку.\n\n"
        "Если у вас возникли проблемы, свяжитесь с поддержкой."
    )
    await message.answer(help_text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())