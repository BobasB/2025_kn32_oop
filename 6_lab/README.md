# Звіт до роботи
## Тема: _Віртуальні середовища та керування залежностями_
### Мета роботи: _Навчитись створювати та керувати віртуальними середовищами Python з використанням інструментів `venv`, `pipenv` та `poetry`. Розробити Flask-додаток, що отримує дані з зовнішнього API._

---

### Виконання роботи

#### 1. Стандартне віртуальне середовище — `venv`

Директорія: [1_venv/](1_venv/)

```bash
# Створення середовища
python -m venv ./my_env

# Активація (macOS/Linux)
source my_env/bin/activate

# Встановлення залежностей
pip install jikanpy-v4 Flask

# Збереження залежностей
pip freeze > requirements.txt

# Відновлення середовища
pip install -r requirements.txt

# Деактивація
deactivate
```

**Встановлені залежності:**
- `Flask 3.1.3` — веб-фреймворк
- `jikanpy-v4 1.0.2` — обгортка для Jikan API (MyAnimeList)
- `flake8 7.3.0` — лінтер для перевірки якості коду

---

#### 2. Pipenv

Директорія: [2_pipenv/](2_pipenv/)

```bash
# Ініціалізація проекту
pipenv --python 3.13

# Встановлення залежностей
pipenv install jikanpy-v4 Flask

# Встановлення dev-залежностей
pipenv install flake8 --dev

# Активація середовища
pipenv shell

# Запуск програми
python ../anime.py

# Перевірка дерева залежностей
pipenv graph

# Сканування вразливостей
pipenv check --scan
```

---

#### 3. Poetry

Директорія: [3_poetry/](3_poetry/) з файлом [pyproject.toml](3_poetry/pyproject.toml)

```bash
# Додавання залежностей
poetry add jikanpy-v4 Flask

# Dev-залежності
poetry add flake8 --dev

# Документаційні залежності
poetry add --group=docs mkdocs

# Встановлення всього середовища
poetry install

# Активація середовища
eval $(poetry env activate)

# Запуск застосунку
python ../anime.py
```

**Документація** генерується через **MkDocs** — [3_poetry/docs/](3_poetry/docs/)

---

#### 4. Flask-застосунок з Jikan API

Файл: [anime.py](anime.py)

Додаток отримує список епізодів аніме з [MyAnimeList](https://myanimelist.net/) через безкоштовний **Jikan API**:

```python
from flask import Flask
from jikanpy import Jikan

jikan = Jikan()
app = Flask(__name__)

episodes = jikan.anime(59978, extension='episodes')

@app.route('/')
def home():
    result = ""
    for episode in episodes["data"]:
        result += f"<p>Епізод {episode['mal_id']}: {episode['title']} — оцінка {episode['score']}</p>"
    return result
```

- `GET /` — список всіх епізодів аніме з оцінками
- `GET /about` — сторінка з описом застосунку

---

#### 5. Змінні оточення

Файл: [app.py](app.py)

```python
import os
a = os.getenv('USER')
b = os.getenv('ENVIRONMENT')
c = os.getenv('ENV_USER')
print(f"Привіт, {c}! Ви працюєте в середовищі {b} під профайлом {a}.")
```

Змінні оточення дозволяють зберігати конфіденційні дані (логіни, токени) поза кодом.

---

#### Порівняння інструментів

| Інструмент | Файл конфігурації | Переваги |
|------------|------------------|----------|
| `venv` | `requirements.txt` | Вбудований у Python, простий |
| `pipenv` | `Pipfile` | Об'єднує venv + pip, lockfile |
| `poetry` | `pyproject.toml` | Сучасний стандарт, build-система, docs |

---

### Висновок

В ході виконання лабораторної роботи:
- Освоєно три інструменти для керування залежностями: `venv`, `pipenv`, `poetry`
- Розроблено Flask-застосунок для відображення даних з зовнішнього API (Jikan)
- Навчились розділяти залежності для розробки та продакшену (`--dev`, `--group=docs`)
- Зрозуміло важливість сканування залежностей на вразливості (`pipenv check`)
- Налаштовано генерацію документації через MkDocs у рамках Poetry проекту
- Освоєно роботу зі змінними оточення через `os.getenv()`

Мета роботи досягнута: практично освоєно всі три інструменти керування середовищами Python.

---