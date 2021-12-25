FROM ubuntu:20.04
ARG TOKEN

RUN apt update
RUN apt install -y python3 pip
COPY ./ /usr/local/workspace

RUN pip3 install -r /usr/local/workspace/requirements.txt

ENV TOKEN=$TOKEN
CMD python3 /usr/local/workspace/run.py
