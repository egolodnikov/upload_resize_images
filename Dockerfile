FROM python:3.6
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt

ADD . /app
WORKDIR /app
