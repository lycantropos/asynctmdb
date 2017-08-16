FROM python:3

WORKDIR /asynctmdb
COPY . /asynctmdb/
RUN python3 -m pip install .
