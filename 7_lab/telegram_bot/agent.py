from google.adk.agents import LlmAgent
from datetime import datetime
from google.adk.tools import ToolContext, FunctionTool
import logging


def get_current_date() -> dict:
    """
    Інстурмент для отримання поточної дати та часу.
    return: Словник з поточною датою та часом у форматі "YYYY-MM-DD HH:MM:SS".
    """
    logging.info(f">>>Tool<<<: Використано інструмент get_current_date для отримання поточної дати та часу.")
    return {"status": "success", "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


def update_user_preference(tool_context: ToolContext, preferences: dict):
    """
    Інструмент для оновлення даних про користувача, його вподобань та налаштувань.
    args:
        tool_context: Контекст інструменту.
        preferences: Словник з налаштуваннями, які потрібно оновити.
        return: Словник з результатом оновлення.
    """
    
    for pref in preferences.keys():
        preference_value = tool_context.state.get(pref, [])
        preference_value.append(preferences[pref])
        tool_context.state[pref] = preference_value

    logging.info(f">>>Tool<<<: Записуємо '{preferences}'")

    return {"status": "success", "updated_preference": preferences}

def get_user_preferences(tool_context: ToolContext, preference: str) -> dict:
    """
    Інструмент для отримання даних про користувача, його вподобань та налаштувань.
    args:
        tool_context: Контекст інструменту.
        preference: Назва налаштування, яке потрібно отримати (наприклад, "language", "theme").
        return: Словник з поточними налаштуваннями користувача.
    """
    preferences = tool_context.state.get(preference, {})
    logging.info(f">>>Tool<<<: Вичитуємо {preferences}")
    return {"status": "success", "preferences": preferences}

root_agent = LlmAgent(
    name='telegram_bot_agent',
    description='АІ агент для Телеграму',
    instruction="""
    Ти є АІ агентом помічником для групи КН-32, який інтегрований у месенджер Телеграм для відповідей користувачу.
    Відповідай українською мовою.
    Завжди роби підпис своїх відповідей "З повагою, АІ помічник КН-32". 
    Відповідай на запитання користувача, використовуючи свої знання та можливості. 
    Якщо ти не знаєш відповіді, чесно скажи про це.
    Ти відповідаєш на запитання у вигляді повідомлень у месенджері Телеграм, тому відповіді повинні бути короткими та інформативними, не більше 200 слів.
    ## **Завжди** використовуй наступні інструменти:
    - get_current_date: Використовуй цей інструмент, коли тобі потрібно отримати поточну дату та час. Не вигадуй дату, а завжди використовуй цей інструмент для отримання актуальної інформації.
    - update_user_preference: Використовуй цей інструмент, коли хочеш зберегти або оновити інформацію про користувача, його вподобання або налаштування. Передавай у цей інструмент словник з ключами, які описують тип інформації (наприклад, {"language": "українська"}, {"name": "Богдан"}, {"hobbies": ["читання", "плавання"]}) та їхніми відповідними значеннями.
    - get_user_preferences: Використовуй цей інструмент, коли хочеш отримати збережену інформацію про користувача, його вподобання або налаштування. Передавай у цей інструмент назву налаштування, яке хочеш отримати (наприклад, "language", "theme", "interests"), і він поверне відповідні дані, які ти раніше зберігав за допомогою update_user_preference.
    """,
    tools=[get_current_date, update_user_preference, get_user_preferences]
)
