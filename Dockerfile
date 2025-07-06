FROM python:3.13.5-slim

COPY . .

WORKDIR /app


CMD ["python", "cli.py"]