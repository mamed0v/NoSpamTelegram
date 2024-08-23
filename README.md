# NoSpam Telegram Бот

## Описание проекта

Этот проект представляет собой Telegram бота, предназначенного для автоматического обнаружения и фильтрации спам-сообщений в супергруппах. Бот использует модель GPT для анализа сообщений и определения, являются ли они спамом. Обнаруженные спам-сообщения сохраняются в JSON файл для дальнейшего анализа.

## Основные функции

- Автоматическое обнаружение спам-сообщений в Telegram супергруппах
- Использование модели GPT для анализа сообщений
- Сохранение информации о спам-сообщениях в JSON файл
- Отправка предупреждений при обнаружении спама

## Структура проекта

- `main.py`: Основной файл бота
- `spam_checker.py`: Модуль для проверки сообщений на спам с использованием GPT
- `spam_storage.py`: Модуль для сохранения спам-сообщений в JSON файл
- `.env`: Файл для хранения конфиденциальных данных (токен бота)
- `requirements.txt`: Список зависимостей проекта
- `spam_messages.json`: Файл для хранения обнаруженных спам-сообщений (создается автоматически)

## Требования

- Python 3.7+
- Библиотеки: aiogram, python-dotenv, openai

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/mamed0v/NoSpamTelegram.git
   cd telegram-antispam-bot
   ```

2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` в корневой директории проекта и добавьте в него следующие строки:
   ```
   TELEGRAM_BOT_TOKEN=ваш_токен_бота
   OPENAI_API_KEY=ваш_ключ_api_openai
   ```

## Использование

1. Запустите бота:
   ```
   python main.py
   ```

2. Добавьте бота в вашу Telegram супергруппу и предоставьте ему права администратора.

3. Бот автоматически начнет проверять сообщения на наличие спама.

## Настройка

- Для изменения логики определения спама отредактируйте файл `spam_checker.py`.
- Для изменения формата сохранения спам-сообщений отредактируйте файл `spam_storage.py`.
