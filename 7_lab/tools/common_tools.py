import logging
from datetime import datetime
from google.adk.tools import ToolContext

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
