FROM python:3.5

WORKDIR /asynctmdb
COPY . /asynctmdb/
RUN python3 -m pip install .
