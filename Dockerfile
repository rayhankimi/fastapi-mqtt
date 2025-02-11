FROM python:3.12.8-alpine
LABEL maintainer="rayhank.com"

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache gcc musl-dev libffi-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir poetry

WORKDIR /app
COPY ./pyproject.toml ./poetry.lock /app/

RUN poetry install --no-root

COPY ./app /app
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
