FROM python:3.7.11-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/opt/collector"

RUN apt-get update && apt-get -y install lsb-release gcc libssl-dev libffi-dev
RUN pip install -U pip
RUN pip install setuptools==45

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /opt/collector
WORKDIR /opt/collector

# cleanup
RUN rm -rf /var/lib/apt/lists/*
