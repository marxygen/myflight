FROM python:3.9
WORKDIR /usr/src/webpage/
COPY ./webpage/ .
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt