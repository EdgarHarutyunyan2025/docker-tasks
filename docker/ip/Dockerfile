# Используем базовый образ Python
FROM python:3.9-slim

# Установка необходимых зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем приложение в контейнер
COPY app.py .

# Открываем порт
EXPOSE 80

# Запускаем приложение
CMD ["python", "app.py"]
