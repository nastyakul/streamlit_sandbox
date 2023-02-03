# syntax=docker/dockerfile:1
FROM --platform=linux/amd64 python:3.10-slim-buster
WORKDIR /app
EXPOSE 8501

RUN pip install poetry

COPY pyproject.toml .
COPY .streamlit/config.toml ~/.streamlit/config.toml
COPY poetry.lock .
RUN poetry install

COPY . .
CMD ["poetry", "run", "streamlit", "run" , "src/main.py"]
