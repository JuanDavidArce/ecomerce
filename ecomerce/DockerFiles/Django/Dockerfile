FROM ubuntu

RUN mkdir app
RUN apt update -y
RUN apt upgrade -y
RUN apt install python3 -y
RUN apt install python3-pip -y
COPY requirements.txt /app/
RUN apt install netcat -y
RUN pip install -r /app/requirements.txt
WORKDIR /app
