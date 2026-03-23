from agent import root_agent, app
from dotenv import load_dotenv
import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from google.adk.runners import InMemoryRunner
from google.adk.models import Message

load_dotenv()
runner = InMemoryRunner(app=app)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробник команди /start"""
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Привіт! Я бот з AI агентом. Задавайте мені будь-які питання!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробник текстових повідомлень з використанням AI агента"""
    user_message = update.message.text
    chat_id = update.effective_chat.id
    
    logging.info(f"Отримано повідомлення від {chat_id}: {user_message}")
    
    try:
        # Створюємо об'єкт повідомлення для агента
        message = Message(role='user', content=user_message)
        
        # Відправляємо повідомлення AI агенту
        response = runner.run(user_id=str(chat_id), session_id=str(chat_id), new_message=message)
        
        # Збираємо відповіді від агента
        agent_responses = []
        for event in response:
            logging.info(f"Отримано подію від агента: {event}")
            if hasattr(event, 'content') and event.content:
                agent_responses.append(event.content)
        
        # Формуємо та відправляємо відповідь користувачу
        answer = '\n'.join(agent_responses) if agent_responses else "Отримано відповідь від агента"
        await context.bot.send_message(chat_id=chat_id, text=answer)
        
    except Exception as e:
        logging.error(f"Помилка при обробці повідомлення: {e}")
        await context.bot.send_message(
            chat_id=chat_id, 
            text="Вибачте, виникла помилка при обробці вашого запиту."
        )

if __name__ == '__main__':
    # Отримуємо токен з змінної середовища
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN не знайдено в .env файлі!")
    
    application = ApplicationBuilder().token(token).build()
    
    # Додаємо обробники
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    
    application.add_handler(start_handler)
    application.add_handler(message_handler)
    
    logging.info("Бот запущено...")
    application.run_polling()