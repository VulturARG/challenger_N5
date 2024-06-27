FROM python:3.8-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN mkdir /n5_challenge
WORKDIR /n5_challenge
COPY . /n5_challenge/
RUN pip install -r requirements.txt
