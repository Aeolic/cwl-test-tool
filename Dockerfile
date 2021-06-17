#syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

USER root
WORKDIR /app

RUN mkdir /app/output
RUN mkdir /input
RUN mkdir /app/input
COPY . .

CMD ["python3", "main.py"]

