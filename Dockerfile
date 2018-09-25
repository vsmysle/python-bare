FROM python:3.6

RUN mkdir /app
WORKDIR /app

COPY ./python_base /app
