FROM python:3
MAINTAINER @Jijeesh < https://github.com/jijeesh >
ENV PYTHONUNBUFFERED 1
COPY . /django-gentelella/
WORKDIR /django-gentelella
RUN pip install -r requirements.txt
WORKDIR /django-gentelella/gentelella
