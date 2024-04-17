# test-textbox

Test task for quality lab.

# Стек

- Python 3.11
- Selenium
- Pytest
- Faker

# Локальный запуск проекта

Клонируйте репозиторий:

```bash
git clone git@github.com:galirkil/test-textbox.git
```

Перейдите в папку с проектом, установите и активируйте виртуально окружение:

```bash
cd test-textbox
python3 -m venv venv
source venv/bin/activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Убедитесь, что на машине установлен Google Chrome, установите при
необходимости.

Запустите тесты:

```bash
python3 -m pytest
```