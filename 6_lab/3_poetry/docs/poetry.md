# Poetry - Сучасний менеджер залежностей та пакування

## Опис

Poetry - це сучасний інструмент для управління залежностями та пакування Python проектів. Він використовує стандартний `pyproject.toml` (PEP 518, PEP 621) та забезпечує детермінованість через lock-файл.

**Офіційна сторінка:** [python-poetry.org](https://python-poetry.org/)

## Переваги Poetry

- ✅ Використовує стандарт pyproject.toml (PEP 518)
- ✅ Швидкий resolver залежностей
- ✅ Підтримка dependency groups (dev, docs, test тощо)
- ✅ Вбудована підтримка пакування та публікації
- ✅ Зручне управління версіями
- ✅ Автоматична генерація lock-файлу
- ✅ Підтримка приватних репозиторіїв
- ✅ Чудова документація

## Недоліки Poetry

- ❌ Потрібно встановлювати окремо
- ❌ Трохи крута крива навчання
- ❌ Може конфліктувати з pip в деяких випадках

## Встановлення Poetry

```bash
# Офіційний спосіб (рекомендовано)
curl -sSL https://install.python-poetry.org | python3 -

# Через pipx (альтернатива)
pipx install poetry

# Через Homebrew (на macOS)
brew install poetry
```

## Основні команди

### Додавання залежностей

**Основні залежності:**
```bash
poetry add jikanpy-v4 Flask
```

**Dev залежності:**
```bash
poetry add flake8 --dev
# або (новий синтаксис)
poetry add flake8 --group dev
```

**Залежності для docs:**
```bash
poetry add mkdocs --group docs
```

### Перегляд дерева залежностей

```bash
poetry show --tree
```

Виводить ієрархічне дерево всіх залежностей проекту.

### Встановлення залежностей з pyproject.toml

```bash
poetry install
```

Встановлює всі залежності, включаючи необов'язкові групи (якщо вони не позначені як optional).

### Встановлення тільки певних груп

**Тільки docs залежності:**
```bash
poetry install --only docs
```

**З docs залежностями:**
```bash
poetry install --with docs
```

**Без dev залежностей:**
```bash
poetry install --without dev
```

### Синхронізація залежностей

```bash
poetry lock
```

Оновлює `poetry.lock` без встановлення пакетів.

### Активація віртуального середовища

**Варіант 1 - створення subshell:**
```bash
poetry shell
```

**Варіант 2 - для Unix (bash/zsh):**
```bash
eval $(poetry env activate)
```

**Варіант 3 - запуск без активації:**
```bash
poetry run python ../anime.py
poetry run mkdocs serve
```

### Управління середовищами

```bash
# Список середовищ
poetry env list

# Інформація про активне середовище
poetry env info

# Видалити поточне середовище
poetry env remove python

# Видалити всі середовища
poetry env remove --all
```

### Список встановлених пакетів

```bash
# Через poetry
poetry list

# Через pip всередині poetry env
poetry run pip list
```

## Структура проекту з Poetry

```
3_poetry/
├── pyproject.toml       # Конфігурація проекту та залежностей
├── poetry.lock          # Заморожені версії (створюється автоматично)
├── mkdocs.yml           # Конфігурація MkDocs
└── docs/                # Документація
    ├── index.md
    ├── venv.md
    ├── pipenv.md
    └── poetry.md
```

## Файл pyproject.toml

```toml
[project]
name = "3-poetry"
version = "0.1.0"
description = "вчимось працювати з Poetry"
authors = [
    {name = "BobasB", email = "bugil.bogdan@gmail.com"}
]
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "jikanpy-v4 (>=1.0.2,<2.0.0)",
    "flask (>=3.1.3,<4.0.0)"
]

[tool.poetry]
package-mode = false

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"

[dependency-groups]
dev = [
    "flake8 (>=7.3.0,<8.0.0)"
]
docs = [
    "mkdocs (>=1.6.1,<2.0.0)"
]

[tool.poetry.group.docs]
optional = true

[tool.poetry.group.dev]
optional = true
```

### Пояснення секцій

#### `[project]`
Метадані проекту (PEP 621):
- `name` - назва проекту
- `version` - версія
- `description` - опис
- `authors` - автори
- `requires-python` - вимоги до версії Python
- `dependencies` - основні залежності

#### `[tool.poetry]`
Налаштування Poetry:
- `package-mode = false` - вимикає режим пакування (для проектів-застосунків)

#### `[build-system]`
Система збірки (PEP 518):
- Вказує, що використовується `poetry-core` для збірки

#### `[dependency-groups]`
Групи залежностей:
- `dev` - інструменти розробки (linters, formatters)
- `docs` - інструменти документації (mkdocs)

#### Optional groups
```toml
[tool.poetry.group.docs]
optional = true
```
Робить групу необов'язковою - не встановлюється при `poetry install` без явного вказання.

## Workflow з Poetry

### Створення нового проекту

```bash
# 1. Ініціалізація проекту (в існуючій директорії)
poetry init

# 2. Додаємо залежності
poetry add jikanpy-v4 Flask

# 3. Додаємо dev залежності
poetry add flake8 --group dev

# 4. Додаємо docs залежності
poetry add mkdocs --group docs

# 5. Переглядаємо дерево
poetry show --tree
```

### Робота з існуючим проектом

```bash
# 1. Клонуємо репозиторій
git clone <repository>
cd project/6_lab/3_poetry

# 2. Встановлюємо всі залежності
poetry install

# 3. Активуємо середовище
eval $(poetry env activate)

# 4. Запускаємо додаток
python ../../app.py

# 5. Деактивуємо
deactivate
```

### Package-mode vs Application-mode

**Package-mode (за замовчуванням):**
- Для бібліотек, які публікуються в PyPI
- Потребує structure з src/ або пакунком
- Створює wheel/sdist при `poetry build`

**Application-mode (`package-mode = false`):**
- Для застосунків (не бібліотек)
- Не потребує особливої структури
- Не можна опублікувати в PyPI
- **Використано в нашому проекті**

## Створення документації з MkDocs

### Налаштування

1. **Додаємо mkdocs до проекту:**
```bash
poetry add mkdocs --group docs
```

2. **Помічаємо групу docs як optional в pyproject.toml:**
```toml
[tool.poetry.group.docs]
optional = true
```

3. **Видаляємо старі середовища та встановлюємо тільки docs:**
```bash
poetry env remove --all
poetry install --only docs
```

### Ініціалізація MkDocs

```bash
# Активуємо середовище
eval $(poetry env activate)

# Створюємо структуру MkDocs
mkdocs new ./

# Запускаємо dev сервер
mkdocs serve
```

### Команди MkDocs

```bash
# Запуск dev сервера з live reload
poetry run mkdocs serve

# Збірка статичного сайту
poetry run mkdocs build

# Розгортання на GitHub Pages
poetry run mkdocs gh-deploy
```

## Конфігурація MkDocs (mkdocs.yml)

```yaml
site_name: Лабораторна робота 6. Віртуальні середовища

theme:
  name: readthedocs
  language: uk

nav:
  - Головна: index.md
  - Віртуальні середовища:
    - venv: venv.md
    - Pipenv: pipenv.md
    - Poetry: poetry.md
  - Код проекту:
    - Огляд програм: code.md
    - Flask додаток: flask_app.md
  - Висновки: conclusion.md
```

## Різниця між dependency groups

```bash
# Встановити все (main + dev + docs)
poetry install

# Встановити тільки main залежності
poetry install --only main

# Встановити main + dev (без docs)
poetry install --without docs

# Встановити тільки docs
poetry install --only docs

# Встановити main + docs (без dev)
poetry install --with docs
```

## Poetry vs Pipenv vs pip/venv

| Функція | pip/venv | Pipenv | Poetry |
|---------|----------|--------|--------|
| Файл конфігурації | requirements.txt | Pipfile | pyproject.toml |
| Lock файл | ❌ | Pipfile.lock | poetry.lock |
| Dependency groups | ❌ | dev/packages | Groups |
| Граф залежностей | ❌ | ✅ | ✅ |
| Пакування | setuptools | ❌ | ✅ |
| Публікація | twine | ❌ | ✅ |
| Стандарт PEP | ❌ | ❌ | ✅ (PEP 518, 621) |
| Швидкість | Швидко | Середньо | Швидко |

## Best Practices

1. **Коміттьте pyproject.toml та poetry.lock:**
   ```bash
   git add pyproject.toml poetry.lock
   ```

2. **Використовуйте dependency groups для організації:**
   ```toml
   [dependency-groups]
   dev = ["flake8", "black", "mypy"]
   test = ["pytest", "coverage"]
   docs = ["mkdocs", "mkdocs-material"]
   ```

3. **Робіть optional групи, які не потрібні завжди:**
   ```toml
   [tool.poetry.group.docs]
   optional = true
   ```

4. **Вказуйте версії з обмеженнями:**
   ```
   flask = "^3.1.3"  # >=3.1.3, <4.0.0
   mkdocs = "~1.6.1" # >=1.6.1, <1.7.0
   ```

5. **Використовуйте poetry run для одноразових команд:**
   ```bash
   poetry run python script.py
   poetry run pytest
   poetry run mkdocs serve
   ```

6. **Регулярно оновлюйте lock файл:**
   ```bash
   poetry update
   ```

## Корисні команди

```bash
# Пошук пакета
poetry search requests

# Показати інформацію про пакет
poetry show flask

# Видалити пакет
poetry remove requests

# Оновити всі пакети
poetry update

# Оновити конкретний пакет
poetry update flask

# Експорт в requirements.txt
poetry export -f requirements.txt --output requirements.txt

# Перевірка pyproject.toml
poetry check

# Показати застарілі пакети
poetry show --outdated
```

## Висновок

Poetry - це найсучасніший та найпотужніший інструмент для управління Python проектами. Він об'єднує управління залежностями, віртуальні середовища, пакування та публікацію в одному інструменті. 

Рекомендується для:
- Нових проектів
- Бібліотек для публікації
- Проектів з складними залежностями
- Команд, які цінують стандартизацію (PEP 518, 621)
