import os
import json
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command

load_dotenv()

router = Router()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()
dp.include_router(router)


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    # ЗАМЕНИТЕ на ваш реальный URL после деплоя GitHub Pages
    web_app_url = "https://goltsofficial.github.io/telegram_seller_assistant/"
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


# Обработчик данных из мини-приложения
@router.message(lambda message: message.web_app_data)
async def handle_web_app_data(message: types.Message):
    try:
        data = json.loads(message.web_app_data.data)
        plan = data.get('plan')
        months = data.get('months')
        user_id = data.get('user_id')

        # Здесь можно сохранить заказ в базу данных
        response_text = (f"✅ Спасибо за заказ!\n\n"
                         f"Тариф: {plan}\n"
                         f"Срок: {months} месяцев\n\n"
                         f"С вами свяжутся для уточнения деталей.")

        await message.answer(response_text)

    except Exception as e:
        print(f"Ошибка при обработке данных: {e}")
        await message.answer("❌ Произошла ошибка при обработке заказа.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())