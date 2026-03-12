# Огляд програм проекту

У рамках лабораторної роботи було створено дві програми на Python, які демонструють роботу з віртуальними середовищами та зовнішніми бібліотеками.

## Файли проекту

```
6_lab/
├── anime.py    # Робота зі змінними оточення
└── app.py      # Flask веб-додаток з Jikan API
```

---

## anime.py - Робота зі змінними оточення

### Вихідний код

```python
import os
import math

a = os.getenv('USER')
b = os.getenv('ENVIRONMENT')
c = os.getenv('ENV_USER')
print(f"Привіт, {c}! Ви працюєте в середовищі {b} під профайлом {a}.")
```

### Опис

Ця проста програма демонструє роботу зі змінними оточення (environment variables) в Python.

### Використані модулі

- **os** - вбудований модуль Python для роботи з операційною системою
- **math** - вбудований модуль для математичних операцій (імпортовано, але не використано)

### Функції os.getenv()

```python
os.getenv(key, default=None)
```

- **key** - назва змінної оточення
- **default** - значення за замовчуванням, якщо змінна не знайдена
- **Повертає** - значення змінної або None

### Змінні оточення у програмі

1. **USER** - системна змінна, ім'я користувача ОС
2. **ENVIRONMENT** - користувацька змінна, тип середовища (development/production)
3. **ENV_USER** - користувацька змінна, ім'я користувача додатку

### Приклад запуску

**Без встановлення змінних:**
```bash
python anime.py
```
**Вивід:**
```
Привіт, None! Ви працюєте в середовищі None під профайлом administrator.
```

**Зі встановленням змінних:**
```bash
export ENVIRONMENT=development
export ENV_USER=BobasB
python anime.py
```
**Вивід:**
```
Привіт, BobasB! Ви працюєте в середовищі development під профайлом administrator.
```

### Використання у різних середовищах

#### З venv
```bash
cd 6_lab/1_venv
source my_env/bin/activate
export ENVIRONMENT=development
export ENV_USER=BobasB
python ../anime.py
deactivate
```

#### З Pipenv
```bash
cd 6_lab/2_pipenv
export ENV_USER=BobasB
pipenv run python ../anime.py
```

> **Примітка:** У `run.sh` вже встановлена змінна `ENVIRONMENT=development`

#### З Poetry
```bash
cd 6_lab/3_poetry
eval $(poetry env activate)
export ENVIRONMENT=production
export ENV_USER=BobasB
python ../anime.py
deactivate
```

### Практичне застосування змінних оточення

Змінні оточення широко використовуються для:

1. **Конфігурації програм:**
   - Підключення до бази даних
   - API ключі
   - Секретні токени

2. **Розділення середовищ:**
   - development (розробка)
   - staging (тестування)
   - production (продакшн)

3. **Чутливі дані:**
   - Паролі
   - Ключі шифрування
   - Credentials

### Покращення коду

**Версія з значеннями за замовчуванням:**
```python
import os

user = os.getenv('USER', 'default_user')
environment = os.getenv('ENVIRONMENT', 'development')
env_user = os.getenv('ENV_USER', 'Guest')

print(f"Привіт, {env_user}! Ви працюєте в середовищі {environment} під профайлом {user}.")
```

**Версія з перевіркою:**
```python
import os
import sys

required_vars = ['ENVIRONMENT', 'ENV_USER']
missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    print(f"❌ Помилка: Не встановлені змінні оточення: {', '.join(missing_vars)}")
    sys.exit(1)

user = os.getenv('USER')
environment = os.getenv('ENVIRONMENT')
env_user = os.getenv('ENV_USER')

print(f"✅ Привіт, {env_user}! Ви працюєте в середовищі {environment} під профайлом {user}.")
```

---

## Порівняння програм

| Аспект | anime.py | app.py |
|--------|----------|--------|
| Складність | Проста | Середня |
| Залежності | Тільки вбудовані | Flask, Jikan |
| Призначення | Демонстрація env vars | Веб-додаток |
| Вивід | Консоль | Веб-сторінка |
| API | Немає | Jikan API (MyAnimeList) |

---

## Висновок

Програма `anime.py` демонструє базову роботу зі змінними оточення, що є важливим навиком для конфігурації додатків у різних середовищах. Програма `app.py` показує створення повноцінного веб-додатку з використанням зовнішніх API.

Для детального аналізу Flask додатку перейдіть до розділу **[Flask додаток](flask_app.md)**.
