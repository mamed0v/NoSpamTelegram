import logging
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

logger = logging.getLogger(__name__)

async def check_spam(text: str) -> bool:
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": """
Вы - система определения спама в чатах Telegram. Ваша задача - анализировать сообщения и определять, являются ли они спамом. 

Характеристики спам-сообщений:
1. Предложения быстрого заработка с нереалистично высокими суммами.
2. Призывы к действию типа "пишите в личные сообщения", "ограниченное предложение".
3. Намеренные орфографические ошибки или замена букв символами (например, "сOoбщение" вместо "сообщение").
4. Неконкретные предложения работы без деталей.
5. Обещания легкого заработка, "свободного графика" без объяснения сути работы.
6. Использование эмодзи или необычных символов для привлечения внимания.
7. Отсутствие контекста или связи с предыдущими сообщениями в чате.

Проанализируйте предоставленное сообщение и определите, является ли оно спамом на основе этих критериев. 

Отвечайте только "SPAM", если сообщение соответствует характеристикам спама, или "NOT_SPAM", если это обычное сообщение. Не добавляйте никаких дополнительных комментариев или объяснений.
                """},
                {"role": "user", "content": text}
            ]
        )
        result = completion.choices[0].message.content.strip().upper()
        return result == "SPAM"
    except Exception as e:
        logger.error(f"Ошибка при проверке на спам: {e}")
        return False