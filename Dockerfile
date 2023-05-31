FROM python:3.10.9

WORKDIR /src
RUN pip install --upgrade pip
COPY requirements.txt /src
RUN pip install -r requirements.txt
COPY . /src