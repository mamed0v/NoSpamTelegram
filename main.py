import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from spam_checker import check_spam
from spam_storage import save_spam_message
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dp.message()
async def handle_message(message: types.Message):
    if message.chat.type != 'supergroup' or message.is_topic_message:
        return

    logger.info(f"Проверка сообщения: {message.text[:50]}...")

    is_spam = await check_spam(message.text)
    
    if is_spam:
        await message.reply("Внимание: это сообщение может быть спамом.")
        save_spam_message(
            sender_full_name=message.from_user.full_name,
            message_text=message.text
        )
    else:
        logger.info(f"Сообщение не является спамом: {message.text[:50]}...")

async def main():
    logger.info("Запуск бота...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Получен сигнал на завершение работы")
    finally:
        logger.info("Программа завершена")