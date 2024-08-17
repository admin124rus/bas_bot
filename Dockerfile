FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["python", "main.py"]

FROM ubuntu:latest
RUN apt-get update \
&&  apt-get install -y tzdata \
&&  ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime \
&&  dpkg-reconfigure --frontend noninteractive tzdata
CMD ["date"]