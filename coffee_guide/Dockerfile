FROM python:3.11

WORKDIR /app

# COPY credentials_copy.json /app/token_credentials/
# COPY token.json /app/token_credentials/

# Установка зависимостей Poetry
RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev

RUN poetry add gunicorn


# Копирование остальных файлов проекта
COPY . .

CMD ["gunicorn", "coffee_guide.wsgi", "--bind", "0.0.0.0:8000"]
