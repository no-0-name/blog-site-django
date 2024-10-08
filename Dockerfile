FROM python:3.10

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONENBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
