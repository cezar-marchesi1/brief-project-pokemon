FROM python:3.13.1-slim

ADD . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y curl gcc
RUN python -m ensurepip --default-pip
RUN pip install  --upgrade pip setuptools
RUN pip install  -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]