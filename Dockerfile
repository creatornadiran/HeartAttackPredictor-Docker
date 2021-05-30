# syntax=docker/dockerfile:1
FROM python:3.7.6-buster
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python flask_api.py