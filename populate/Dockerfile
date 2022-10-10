FROM debian:latest

LABEL maintainer="Orange DE Infarctus 2"

WORKDIR /app

RUN apt-get update && apt-get install python3-pip -y && pip3 install requests==2.22.0 && pip3 install pymongo && pip3 install pandas \
    && rm -rf /root/.cache

COPY . .

CMD python3 app.py
