
# Звіт до роботи
## Тема: _АІ агенти з Google ADK та Telegram Bot_
### Мета роботи: _Навчитись створювати АІ агентів з використанням Google Agent Development Kit (ADK), реалізувати власні інструменти для агента та інтегрувати його у месенджер Telegram_

---

### Виконання роботи

Проект керується через **Poetry**. Конфігурація: [pyproject.toml](pyproject.toml)

```bash
# Активація середовища та запуск Telegram бота
cd 7_lab
eval $(poetry env activate)
export PYTHONPATH="/Users/administrator/it_college/2025_kn32_oop/7_lab"
python telegram_bot
```

---

#### Структура проекту

```
7_lab/
├── pyproject.toml          # Poetry конфігурація
├── my_first_agent/         # Перший агент (cat_agent)
│   ├── __init__.py
│   └── agent.py
├── telegram_bot/           # Telegram бот з АІ агентом
│   ├── __init__.py
│   ├── __main__.py
│   └── agent.py
├── telegram_manager/       # Менеджер Telegram повідомлень
│   ├── __init__.py
│   ├── agent.py
│   └── posts.md
└── tools/                  # Власні інструменти для агентів
    ├── __init__.py
    └── common_tools.py
```

---

#### 1. Перший АІ агент — `cat_agent`

Файл: [my_first_agent/agent.py](my_first_agent/agent.py)

```python
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='cat_agent',
    description='АІ помічник який дуже любить котів.',
    instruction="""
    Ти є АІ помічник який відповідає на запитання користувачів.
    Ти дуже любиш котів і якщо користувач задає запитання про інших тварин —
    починаєш спілкуватись мовою котів та мявкотіти.
    Завжди переконуй користувача в тому що коти найкращі тварини на світі.
    Використовуй Українську мову для спілкування з користувачем.
    """,
)
```

**Запуск через ADK Dev UI:**
```bash
adk web
```

---

#### 2. Telegram Bot агент

Файл: [telegram_bot/agent.py](telegram_bot/agent.py)

Агент інтегровано у Telegram та відповідає на повідомлення користувачів:

```python
from google.adk.agents import LlmAgent
from tools.common_tools import get_current_date, update_user_preference, get_user_preferences

root_agent = LlmAgent(
    name='telegram_bot_agent',
    description='АІ агент для Телеграму',
    instruction="""
    Ти є АІ агентом помічником для групи КН-32, інтегрованим у Telegram.
    Відповідай українською мовою.
    Завжди роби підпис: "З повагою, АІ помічник КН-32".
    """,
    tools=[get_current_date, update_user_preference, get_user_preferences]
)
```

---

#### 3. Власні інструменти агента

Файл: [tools/common_tools.py](tools/common_tools.py)

Реалізовано три інструменти, які агент використовує для роботи:

| Інструмент | Опис |
|------------|------|
| `get_current_date()` | Повертає поточну дату та час |
| `update_user_preference(preferences)` | Зберігає налаштування користувача у стані сесії |
| `get_user_preferences(preference)` | Отримує збережені налаштування |

```python
def get_current_date() -> dict:
    return {"status": "success", "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

def update_user_preference(tool_context: ToolContext, preferences: dict):
    for pref in preferences.keys():
        preference_value = tool_context.state.get(pref, [])
        preference_value.append(preferences[pref])
        tool_context.state[pref] = preference_value
    return {"status": "success", "updated_preference": preferences}
```

---

#### 4. Залежності проекту

```toml
[project]
dependencies = [
    "google-adk (>=1.27.2,<2.0.0)",        # Google Agent Development Kit
    "python-telegram-bot (>=22.7,<23.0)",   # Telegram Bot API
    "python-dotenv (>=1.2.2,<2.0.0)"        # Змінні оточення (.env)
]
```

---

### Висновок

В ході виконання лабораторної роботи:
- Створено першого АІ агента на базі **Google ADK** з моделлю **Gemini 2.5 Flash**
- Реалізовано власні інструменти (`tools`) для агента: отримання дати, зберігання/читання налаштувань користувача
- Інтегровано АІ агента у месенджер **Telegram** через бібліотеку `python-telegram-bot`
- Освоєно концепцію **стану сесії** (`tool_context.state`) для збереження даних між повідомленнями
- Налаштовано проект на **Poetry** з чітким визначенням залежностей у `pyproject.toml`
- Запущено Dev UI для тестування агентів через `adk web`

Мета роботи досягнута: розроблено функціонального Telegram бота з АІ агентом, власними інструментами та пам'яттю.

---