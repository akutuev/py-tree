FROM python:3.13.5-slim

WORKDIR /app

COPY . /app

ENTRYPOINT [ "python", "cli.py" ]