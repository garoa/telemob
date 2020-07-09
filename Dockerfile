FROM python:3.8.3-slim-buster
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
