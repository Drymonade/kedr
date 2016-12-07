FROM python:latest

MAINTAINER Skiba Andrey skiba_andrey@mail.ru

RUN pip install keras==1.1.2
RUN pip install flask==0.11.1
RUN pip install Pillow==3.3.1
RUN pip install h5py==2.6.0

ENV KERAS_BACKEND=theano

ADD . /app

EXPOSE 5000
WORKDIR /app
CMD ["python", "core.py"]