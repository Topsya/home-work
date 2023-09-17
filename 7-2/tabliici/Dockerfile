# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.10
FROM python:3.10

WORKDIR /app

# Скопіюємо інші файли в робочу директорію контейнера
COPY . /app

RUN pip install -r requirements.txt

# EXPOSE 5000

# Запустимо наш застосунок всередині контейнера
ENTRYPOINT ["python", "main.py"]