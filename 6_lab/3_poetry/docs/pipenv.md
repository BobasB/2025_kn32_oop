# Pipenv - Сучасний менеджер залежностей

## Опис

Pipenv - це інструмент, який об'єднує `pip` та `virtualenv` в один зручний workflow. Він автоматично створює віртуальні середовища та управляє залежностями проекту через файли `Pipfile` та `Pipfile.lock`.

**Офіційна сторінка:** [pipenv.pypa.io](https://pipenv.pypa.io/en/latest/)

## Переваги Pipenv

- ✅ Автоматичне створення та управління віртуальними середовищами
- ✅ Розділення dev та prod залежностей
- ✅ Автоматична генерація lock-файлу для детермінованих білдів
- ✅ Виявлення вразливостей у залежностях (`pipenv check`)
- ✅ Більш читабельний формат Pipfile (TOML)
- ✅ Граф залежностей (`pipenv graph`)

## Недоліки Pipenv

- ❌ Потрібно встановлювати окремо
- ❌ Може бути повільнішим за pip
- ❌ Іноді складно знайти де знаходиться віртуальне середовище

## Встановлення Pipenv

```bash
# На macOS з використанням Homebrew (рекомендовано)
brew install pipenv

# Через pip
pip install --user pipenv
```

Детальна інструкція: [pipenv.pypa.io/installation](https://pipenv.pypa.io/en/latest/installation.html)

## Основні команди

### Ініціалізація проекту

```bash
pipenv --python 3.13
```

Створює новий проект з віртуальним середовищем та файлом `Pipfile` для Python 3.13.

### Встановлення пакетів

**Основні залежності:**
```bash
pipenv install jikanpy-v4 Flask
```

**Dev залежності:**
```bash
pipenv install flake8 --dev
```

### Встановлення всіх залежностей з Pipfile

```bash
pipenv install
```

Встановлює всі залежності, описані у `Pipfile`.

### Встановлення тільки dev залежностей

```bash
pipenv install --dev
```

### Активація середовища

```bash
pipenv shell
```

Активує віртуальне середовище проекту.

### Запуск скрипта без активації

```bash
pipenv run python ../anime.py
```

Виконує Python скрипт у віртуальному середовищі без його активації.

### Граф залежностей

```bash
pipenv graph
```

Виводить дерево залежностей проекту, показуючи які пакети від чого залежать.

### Перевірка на вразливості

```bash
pipenv check
```

Перевіряє встановлені пакети на відомі вразливості безпеки.

**Розширене сканування:**
```bash
pipenv check --scan
```

> **Примітка:** Зараз в основному використовують GitHub Dependabot для автоматичного сканування залежностей на вразливості, але `pipenv check` можна використовувати для локального сканування.

### Видалення віртуального середовища

```bash
pipenv --rm
```

Видаляє віртуальне середовище проекту (залишає Pipfile).

### Деактивація середовища

```bash
deactivate
```

Або просто вийдіть з shell (Ctrl+D або `exit`).

## Структура проекту з Pipenv

```
2_pipenv/
├── Pipfile              # Опис залежностей (читабельний формат)
├── Pipfile.lock         # Заморожені версії (не редагується вручну)
└── run.sh               # Скрипт для запуску
```

## Файл Pipfile

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
jikanpy-v4 = "*"
flask = "*"

[dev-packages]
flake8 = "*"

[requires]
python_version = "3.13"
python_full_version = "3.13.7"
```

### Структура Pipfile

- **`[source]`** - джерела пакетів (PyPI)
- **`[packages]`** - основні залежності для production
- **`[dev-packages]`** - залежності тільки для розробки
- **`[requires]`** - вимоги до версії Python

## Скрипт запуску (run.sh)

```bash
#!/bin/bash

export ENVIRONMENT=development
pipenv install
pipenv run python ../app.py
```

Цей скрипт:
1. Встановлює змінну оточення `ENVIRONMENT`
2. Встановлює всі залежності
3. Запускає Flask додаток у віртуальному середовищі

### Запуск скрипта

```bash
chmod +x run.sh  # Надаємо права на виконання (один раз)
./run.sh         # Запускаємо
```

## Workflow з Pipenv

### Початок роботи над проектом

```bash
# 1. Створюємо проект
pipenv --python 3.13

# 2. Встановлюємо залежності
pipenv install jikanpy-v4 Flask

# 3. Встановлюємо dev залежності
pipenv install flake8 --dev

# 4. Переглядаємо граф залежностей
pipenv graph

# 5. Активуємо середовище
pipenv shell

# 6. Працюємо з кодом
python ../anime.py

# 7. Перевіряємо код
flake8 ../anime.py

# 8. Виходимо
deactivate
```

### Робота з існуючим проектом

```bash
# 1. Клонуємо репозиторій
git clone <repository>
cd project/2_pipenv

# 2. Встановлюємо всі залежності (включаючи dev)
pipenv install --dev

# 3. Активуємо середовище
pipenv shell

# 4. Працюємо
python ../app.py
```

### Оновлення залежностей

```bash
# Оновити всі пакети до останніх версій
pipenv update

# Оновити конкретний пакет
pipenv update flask

# Перевірити застарілі пакети
pipenv update --dry-run
```

## Pipfile vs requirements.txt

| Аспект | requirements.txt | Pipfile |
|--------|------------------|---------|
| Формат | Текст | TOML |
| Читабельність | Середня | Висока |
| Dev залежності | Окремий файл | В одному файлі |
| Детермінованість | Потребує freeze | Автоматичний lock |
| Джерела пакетів | Не вказуються | Вказуються |

## Pipenv Graph - приклад виводу

```
Flask==3.1.3
├── blinker [required: >=1.9, installed: 1.9.0]
├── click [required: >=8.1.3, installed: 8.3.1]
├── itsdangerous [required: >=2.2, installed: 2.2.0]
├── Jinja2 [required: >=3.1, installed: 3.1.6]
│   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
└── Werkzeug [required: >=3.1, installed: 3.1.6]

jikanpy-v4==1.0.2
├── aiohttp [required: Any, installed: 3.13.3]
│   ├── aiohappyeyeballs [required: >=2.6.1, installed: 2.6.1]
│   ├── aiosignal [required: >=1.1.2, installed: 1.4.0]
│   └── ... (інші залежності)
└── simplejson [required: Any, installed: 3.20.2]
```

## Перевірка безпеки

```bash
# Базова перевірка
pipenv check

# Вивід може бути таким:
✔ All good!

# Або якщо є вразливості:
⚠ Warning: Flask 2.0.0 has a known security vulnerability
```

## Best Practices

1. **Коміттьте Pipfile та Pipfile.lock в git:**
   ```
   git add Pipfile Pipfile.lock
   ```

2. **Використовуйте dev залежності для інструментів розробки:**
   ```bash
   pipenv install pytest black mypy --dev
   ```

3. **Регулярно перевіряйте на вразливості:**
   ```bash
   pipenv check
   ```

4. **Використовуйте `pipenv graph` для розуміння залежностей:**
   ```bash
   pipenv graph
   ```

5. **При deployment встановлюйте тільки prod залежності:**
   ```bash
   pipenv install --ignore-pipfile  # Використовує Pipfile.lock
   ```

## Висновок

Pipenv - це потужний інструмент, який спрощує управління залежностями та віртуальними середовищами. Він особливо корисний для проектів середнього розміру, де важлива безпека та детермінованість білдів.
