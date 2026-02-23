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