import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def save_spam_message(sender_full_name: str, message_text: str):
    spam_data = {
        "timestamp": datetime.now().isoformat(),
        "sender_full_name": sender_full_name,
        "message": message_text
    }
    
    try:
        with open('spam_messages.json', 'r+') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
            
            data.append(spam_data)
            
            file.seek(0)
            json.dump(data, file, indent=2, ensure_ascii=False)
            file.truncate()
    except FileNotFoundError:
        with open('spam_messages.json', 'w') as file:
            json.dump([spam_data], file, indent=2, ensure_ascii=False)

    logger.info(f"Спам-сообщение сохранено: {spam_data}")