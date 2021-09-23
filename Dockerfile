FROM python:3.7.11-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/opt/Monitor"

RUN apt-get update && apt-get -y install lsb-release gcc libssl-dev libffi-dev
RUN pip install -U pip
RUN pip install setuptools==45

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /opt/Monitor
WORKDIR /opt/Monitor

# cleanup
RUN rm -rf /var/lib/apt/lists/*
