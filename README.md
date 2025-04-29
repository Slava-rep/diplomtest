# diplomtest
# Дипломный проект

Система управления поверкой средств измерений.

## Установка

1. Клонируйте репозиторий:
git clone https://github.com/yourusername/diplom.git
cd diplom

2. Создайте виртуальное окружение и активируйте его:
python -m venv venv
source venv/bin/activate # для Linux/Mac
venv\Scripts\activate # для Windows

3. Установите зависимости:
pip install -r requirements.txt

4. Создайте базу данных PostgreSQL:
createdb diplom

5. Примените миграции:
python manage.py migrate

6. Создайте суперпользователя:
python manage.py createsuperuser

7. Запустите сервер разработки:
python manage.py runserver

## Использование Docker

1. Соберите и запустите контейнеры:
docker-compose up --build

2. Примените миграции:
docker-compose exec web python manage.py migrate

3. Создайте суперпользователя:
docker-compose exec web python manage.py createsuperuser

## Структура проекта

- `si/` - приложение для управления средствами измерений
- `employees/` - приложение для управления сотрудниками
- `certificates/` - приложение для управления свидетельствами о поверке
- `journals/` - приложение для управления журналами
- `users/` - приложение для управления пользователями
- `utils/` - приложение с общими утилитами

## Лицензия

MIT
