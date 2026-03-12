# Flask додаток з Jikan API

## Загальний опис

Веб-додаток на Flask, який використовує **Jikan API** для отримання інформації про епізоди аніме та відображення їх на веб-сторінці.

**Jikan** - це безкоштовний REST API для MyAnimeList (найбільша база даних аніме та манги).

## Вихідний код (app.py)

```python
from flask import Flask, render_template
from jikanpy import Jikan

jikan = Jikan()
app = Flask(__name__)

j = jikan.anime(59978, extension='episodes')


@app.route('/')
def home():
    a = str()
    for episode in j["data"]:
        a += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {episode['score']}<p>"
    return a


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    print(j)
    app.run(debug=True)
```

## Використані бібліотеки

### Flask 3.1.3
**Мікро-фреймворк для створення веб-додатків**

- Легкий та гнучкий
- Мінімум шаблонного коду
- Вбудований сервер розробки
- Підтримка шаблонів Jinja2
- Routing для URL endpoints

**Офіційний сайт:** [flask.palletsprojects.com](https://flask.palletsprojects.com/)

### jikanpy-v4 1.0.2
**Python обгортка для Jikan REST API**

- Асинхронні та синхронні запити
- Простий інтерфейс для MyAnimeList
- Автоматична обробка rate limits
- Підтримка всіх endpoint'ів Jikan API

**GitHub:** [github.com/abhinavk99/jikanpy](https://github.com/abhinavk99/jikanpy)

**Jikan API Docs:** [docs.api.jikan.moe](https://docs.api.jikan.moe/)

## Структура додатку

### Імпорти

```python
from flask import Flask, render_template
from jikanpy import Jikan
```

- **Flask** - клас для створення веб-додатку
- **render_template** - функція для рендерингу HTML шаблонів
- **Jikan** - клас для роботи з Jikan API

### Ініціалізація

```python
jikan = Jikan()
app = Flask(__name__)
```

- **jikan** - екземпляр клієнта Jikan API
- **app** - екземпляр Flask додатку

### Отримання даних

```python
j = jikan.anime(59978, extension='episodes')
```

**Що відбувається:**
- Звертається до Jikan API
- Отримує дані про аніме з ID **59978**
- Розширення **'episodes'** - отримати список епізодів
- Результат зберігається у змінній `j`

**Аніме ID 59978:** [Dandadan](https://myanimelist.net/anime/59978/Dandadan)

**Структура відповіді:**
```json
{
  "data": [
    {
      "mal_id": 1,
      "title": "Епізод 1: Назва",
      "score": 4.5,
      ...
    },
    ...
  ]
}
```

## Маршрути (Routes)

### Головна сторінка '/'

```python
@app.route('/')
def home():
    a = str()
    for episode in j["data"]:
        a += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {episode['score']}<p>"
    return a
```

**Що робить:**
1. Створює порожній рядок `a`
2. Ітерує по всіх епізодах з `j["data"]`
3. Для кожного епізоду додає HTML параграф з інформацією
4. Повертає сформований HTML

**Приклад виводу:**
```html
<p>Епізод 1 з назвою: That's How Love Starts, Ya Know має оцінку 4.44<p>
<p>Епізод 2 з назвою: That's a Space Alien, Ain't It?! має оцінку 4.52<p>
<p>Епізод 3 з назвою: It's a Grays! має оцінку 4.56<p>
...
```

### Сторінка 'About' /about

```python
@app.route('/about')
def about():
    return render_template('about.html')
```

**Що робить:**
- Намагається знайти шаблон `about.html` у папці `templates/`
- Рендерить та повертає HTML

> **Примітка:** шаблон `about.html` не створений у проекті, тому при відвідуванні `/about` буде помилка.

### Запуск сервера

```python
if __name__ == '__main__':
    print(j)
    app.run(debug=True)
```

**Що робить:**
1. Перевіряє, чи скрипт запущений напряму
2. Виводить у консоль отримані дані `j`
3. Запускає Flask dev сервер з увімкненим debug режимом

**Debug режим забезпечує:**
- Автоматичне перезавантаження при змінах коду
- Детальні повідомлення про помилки
- Інтерактивний debugger у браузері

## Запуск додатку

### З різних віртуальних середовищ

#### venv
```bash
cd 6_lab/1_venv
source my_env/bin/activate
python ../app.py
```

#### Pipenv
```bash
cd 6_lab/2_pipenv
./run.sh
# або
pipenv run python ../app.py
```

#### Poetry
```bash
cd 6_lab/3_poetry
eval $(poetry env activate)
python ../app.py
```

### Доступ до додатку

Після запуску сервер буде доступний за адресою:
```
http://127.0.0.1:5000/
```

або

```
http://localhost:5000/
```

**Маршрути:**
- `http://localhost:5000/` - головна сторінка з епізодами
- `http://localhost:5000/about` - сторінка about (буде помилка, якщо шаблон не створений)

### Вивід у консолі

При запуску у консолі з'явиться:
```
{JSON з даними про епізоди}

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
```

## Jikan API endpoints

### Аніме інформація

```python
# Базова інформація
anime = jikan.anime(59978)

# Персонажі
characters = jikan.anime(59978, extension='characters')

# Епізоди
episodes = jikan.anime(59978, extension='episodes')

# Новини
news = jikan.anime(59978, extension='news')

# Відгуки
reviews = jikan.anime(59978, extension='reviews')
```

### Інші endpoints

```python
# Пошук аніме
search = jikan.search('anime', 'Dandadan')

# Топ аніме
top = jikan.top('anime')

# Сезон
season = jikan.season(2024, 'fall')

# Випадкове аніме
random = jikan.random('anime')
```

## Покращення коду

### Проблеми поточної реалізації

1. ❌ Дані отримуються при імпорті модуля (не при запиті)
2. ❌ HTML генерується конкатенацією рядків (небезпечно)
3. ❌ Немає обробки помилок
4. ❌ Unused змінна `math` в `anime.py`
5. ❌ Відсутній шаблон `about.html`

### Покращена версія

```python
from flask import Flask, render_template
from jikanpy import Jikan

app = Flask(__name__)
jikan = Jikan()

ANIME_ID = 59978


@app.route('/')
def home():
    try:
        data = jikan.anime(ANIME_ID, extension='episodes')
        episodes = data.get("data", [])
        return render_template('episodes.html', episodes=episodes)
    except Exception as e:
        return f"<h1>Помилка: {e}</h1>", 500


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
```

### Шаблон episodes.html

```html
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Епізоди Dandadan</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .episode { 
            border: 1px solid #ddd; 
            padding: 10px; 
            margin: 10px 0; 
            border-radius: 5px;
        }
        .episode:hover { background-color: #f5f5f5; }
    </style>
</head>
<body>
    <h1>Епізоди аніме Dandadan</h1>
    
    {% for episode in episodes %}
    <div class="episode">
        <h3>Епізод {{ episode.mal_id }}</h3>
        <p><strong>Назва:</strong> {{ episode.title }}</p>
        <p><strong>Оцінка:</strong> {{ episode.score if episode.score else 'Немає оцінки' }}</p>
    </div>
    {% endfor %}
</body>
</html>
```

### Шаблон about.html

```html
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Про додаток</title>
</head>
<body>
    <h1>Про додаток</h1>
    <p>Це демонстраційний додаток для лабораторної роботи №6.</p>
    <p>Використовуються технології:</p>
    <ul>
        <li>Flask 3.1.3</li>
        <li>Jikan API v4</li>
        <li>Python 3.13</li>
    </ul>
    <a href="/">Повернутися до епізодів</a>
</body>
</html>
```

## Переваги використання Jikan API

- ✅ Безкоштовний (не потрібен API ключ)
- ✅ Велика база даних (MyAnimeList)
- ✅ Добра документація
- ✅ Підтримка багатьох endpoint'ів
- ✅ Python обгортка (jikanpy)

## Обмеження Jikan API

- ⚠️ Rate limits (3 запити/секунду)
- ⚠️ Залежить від MyAnimeList
- ⚠️ Можуть бути затримки при оновленні даних

## Висновок

Flask додаток демонструє:
- Створення простого веб-сервера
- Роботу з зовнішніми API
- Використання сторонніх бібліотек
- Роутинг та обробку HTTP запитів

Проект показує важливість віртуальних середовищ для ізоляції залежностей та можливість створення повноцінних веб-додатків з мінімальним кодом.
