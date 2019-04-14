FROM python:3.7

MAINTAINER Skiba Andrey skiba_andrey@mail.ru

ENV KERAS_BACKEND=theano

RUN pip install keras flask Pillow h5py theano

WORKDIR /app
COPY . /app

EXPOSE 5000

CMD ["python", "core.py"]
