FROM python:3.8-alpine3.12

WORKDIR /app

RUN apk add --no-cache build-base

COPY rpc.py .
COPY RadiusApp.py .
COPY .env .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD nameko run rpc --broker amqp://guest:guest@rabbitmq:5672