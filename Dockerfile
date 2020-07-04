FROM python:slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt && python manage.py migrate
