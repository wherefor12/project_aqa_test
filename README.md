# project_aqa_test

## Запуск

1. Клонировать репозиторий:
`git clone <ссылка_на_репозиторий>`

2. Перейти в папку проекта:
`cd project_aqa_test`

3. Создать виртуальное окружение:
`python -m venv .venv`

4. Активировать виртуальное окружение:
Windows:
`.venv\Scripts\activate`

5. Установить зависимости:
`pip install -r requirements.txt`

6. Создать файл `.env` по примеру `.env.example`

7. Запустить тесты:
`pytest -q`


## Как запустить UI-тесты

### Установка зависимостей

```bash
pip install -r requirements.txt
playwright install
```

### Переменные окружения

Создать файл `.env` в корне проекта:
GH_USER=логин_github
GH_PASS=пароль_github

> Файл `.env` не хранится в репозитории — он добавлен в `.gitignore`

### Запуск UI-тестов

Все UI-тесты:
```bash
pytest -m ui -v
```

Конкретный файл:
```bash
pytest tests/ui/test_auth.py -v
```