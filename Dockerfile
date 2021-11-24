# Dockerfile

FROM python:3.8

COPY ./Backend /Backend

WORKDIR /Backend

RUN pip install -r requirements.txt

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

CMD ["python", "back.py"]

EXPOSE 5000