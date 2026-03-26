from google.adk.agents.llm_agent import Agent
from datetime import datetime
from google.adk.tools import ToolContext, FunctionTool


def get_current_date() -> dict:
    """
    Інстурмент для отримання поточної дати та часу.
    return: Словник з поточною датою та часом у форматі "YYYY-MM-DD HH:MM:SS".
    """
    return {"status": "success", "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


def update_user_preference(preference: str, value: str, tool_context: ToolContext):
    """
    Інструмент для оновлення даних про користувача, його вподобань та налаштувань.
    preference: Назва налаштування, яке потрібно оновити (наприклад, "language", "theme").
    value: Нове значення для цього налаштування."""
    
    user_prefs_key = "user:preferences"

    # Get current preferences or initialize if none exist

    preferences = tool_context.state.get(user_prefs_key, {})

    preferences[preference] = value

    # Write the updated dictionary back to the state

    tool_context.state[user_prefs_key] = preferences

    print(f"Tool: Updated user preference '{preference}' to '{value}'")

    return {"status": "success", "updated_preference": preference}

def get_user_preferences(tool_context: ToolContext):
    """
    Інструмент для отримання даних про користувача, його вподобань та налаштувань.
    return: Словник з поточними налаштуваннями користувача.
    """
    user_prefs_key = "user:preferences"
    preferences = tool_context.state.get(user_prefs_key, {})
    print(f"Tool: Retrieved user preferences: {preferences}")
    return {"status": "success", "preferences": preferences}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Це АІ агент для Телеграму',
    instruction="""
    Ти є АІ агентом помічником, який інтегрований у Телеграм для відповідей користувачу.
    Відповідай українською мовою.
    Ти є помічник для групи КН-32, завжди роби підпис своїх відповідей "З повагою, КН-32". 
    Відповідай на запитання користувача, використовуючи свої знання та можливості. 
    Для визначення поточної дати та часу, використовуй інструмент get_current_date.
    Для оновлення даних про користувача, використовуй інструмент update_user_preference. Записуй всі дані про користувача які вважаєш важливими для того щоб про них памятати.
    Для отримання даних про користувача, використовуй інструмент get_user_preferences.
    Якщо ти не знаєш відповіді, чесно скажи про це.
    Ти відповідаєш на запитання у вигляді повідомлень у месенджері Телеграм, тому відповіді повинні бути короткими та інформативними, не більше 200 слів.
    """,
    tools=[get_current_date, update_user_preference, get_user_preferences]
)
