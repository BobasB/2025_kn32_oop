from agent import root_agent

from dotenv import load_dotenv
import logging
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

USER_SESSIONS: dict[str, Runner] = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробник команди /start"""
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Привіт! Я бот з AI агентом. Задавайте мені будь-які питання!"
    )

async def setup_session_and_runner(app_name: str, user_id: str, session_id: str):
    """Створює сесію та Runner для AI агента"""
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id)
    runner = Runner(agent=root_agent, app_name=app_name, session_service=session_service)
    return session, runner

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробник текстових повідомлень з використанням AI агента"""
    user_message = str(update.message.text)
    user_id_str = session_id_str = str(update.effective_chat.id)
    user = update.message.from_user.username
    
    logging.info(f"Отримано повідомлення від {user} {session_id_str}: {user_message}")
    #logging.info(f"Змінна update: {update}")
    #logging.info(f"Змінна context: {context}"
    base_message = f"З тобою спілкується користувач Телеграму під ім'ям {user}."
    
    try:
        # Створюємо об'єкт повідомлення для агентаm
        message = types.Content(role='user', parts=[types.Part(text=base_message), types.Part(text=user_message)])
        logging.info(f"Створено повідомлення для агента: {message}")
        
        # Відправляємо повідомлення AI агенту (сесія створюється автоматично)
        if USER_SESSIONS.get(user_id_str+session_id_str):
            runner = USER_SESSIONS[user_id_str+session_id_str]
            logging.info(f"Використовуємо існуючу сесію для користувача {user_id_str} та сесії {session_id_str}")
        else:
            _, runner = await setup_session_and_runner("телеграм_бот", user_id_str, session_id_str)
            USER_SESSIONS[user_id_str+session_id_str] = runner
            logging.info(f"Створено нову сесію для користувача {user_id_str} та сесії {session_id_str}")
        
        # Збираємо відповіді від агента
        agent_responses = []
        response = runner.run_async(user_id=user_id_str, session_id=session_id_str, new_message=message)
        logging.info(f"Очікуємо відповіді від агента...")

        async for event in response:
            logging.info(f"Отримано подію від агента: {event}")
            if event.is_final_response():
                final_response = event.content.parts[0].text
                logging.info("Формування фінальної відповіді від агента...")
                agent_responses.append(final_response)
                
        logging.info(f"Відповіді від агента: {agent_responses}")
        # Формуємо та відправляємо відповідь користувачу
        answer = '\n'.join(agent_responses) if agent_responses else "Агент не надав відповіді."
        await context.bot.send_message(chat_id=user_id_str, text=answer)
        
    except Exception as e:
        logging.error(f"Помилка при обробці повідомлення: {e}")
        await context.bot.send_message(
            chat_id=user_id_str, 
            text="Вибачте, виникла помилка при обробці вашого запиту."
        )

if __name__ == '__main__':
    # Отримуємо токен з змінної середовища
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN не знайдено в .env файлі!")
    
    # Створюємо додаток Telegram бота
    application = ApplicationBuilder().token(token).build()
    
    # Додаємо обробники
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    
    application.add_handler(start_handler)
    application.add_handler(message_handler)
    
    logging.info("Бот запущено...")
    application.run_polling()