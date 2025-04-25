# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем системные зависимости для WeasyPrint и psycopg2
RUN apt-get update && apt-get install -y \
    libglib2.0-dev \
    libcairo2 \
    libpango-1.0-0 \
    libffi-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libgdk-pixbuf-2.0-0 \
    libpangocairo-1.0-0 \
    libpq-dev \
    gcc && \
    apt-get clean

# Копируем файл зависимостей в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

# Устанавливаем переменные окружения для Django
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Открываем порт для приложения
EXPOSE 8000

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]