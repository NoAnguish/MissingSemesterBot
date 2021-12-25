FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3 pip

COPY ./requirements.txt /usr/local/workspace/requirements.txt
COPY ./run.py /usr/local/workspace/run.py
COPY ./bot /usr/local/workspace/bot

RUN pip3 install -r /usr/local/workspace/requirements.txt

CMD python3 /usr/local/workspace/run.py
