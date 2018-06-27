
FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /tmp

COPY requirements.txt /tmp

RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . /app

CMD [ "python3", "app.py" ]

