FROM python:3.13.5-slim

WORKDIR /app

COPY . .

ENTRYPOINT  ["python", "-m", "app.cli"]