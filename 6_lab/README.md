# Віртуальні середовища

```bash
pip list
pip show requests
pip install requests

```

### Робота в середовищі

```bash
python -m venv ./my_env
source my_env/bin/activate
pip install jikanpy-v4 Flask

pip freeze > requirements.txt
# Після перевстановлення середовища потрібно встановити всі залежності, які описані в requirements.txt
pip install -r requirements.txt

python -m venv ./my_env && source my_env/bin/activate && pip install -r requirements.txt
pip list
deactivate
```

### Бібліотеки для розробки програмного забезпечення
```
source ./my_env/bin/activate
pip install -r requirements-dev.txt
```

### Pipenv
- встановлюємо з використанням гайду https://pipenv.pypa.io/en/latest/installation.html
```bash
pipenv --python 3.13
pipenv install jikanpy-v4 Flask
pipenv graph

pipenv install
pipenv shell
python ../anime.py
deactivate

pipenv install flake8 --dev
pipenv --rm
pipenv install --dev
pipenv shell
flake8 ../anime.py 
deactivate

pipenv check --scan
```
- зараз в основному використовують Github Dependabot для автоматичного сканування залежностей на вразливості, але можна використовувати і цей інструмент для локального сканування