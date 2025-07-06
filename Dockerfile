FROM python:3.13.5-slim

COPY . /app

WORKDIR /app

ENTRYPOINT [ "python", "cli.py" ]