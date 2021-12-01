FROM python:3
USER root


RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools


RUN pip install scikit-image==0.18.3
RUN pip install ezdxf==0.17.1
RUN pip install opencv-python==4.5.4.60
RUN pip install opencv-contrib-python==4.5.4.60

RUN apt-get install -y libgl1-mesa-dev=20.3.5-1
RUN apt-get install -y tesseract-ocr=4.1.1-2.1
RUN apt-get install -y libtesseract-dev=4.1.1-2.1
RUN apt-get install tesseract-ocr-jpn  tesseract-ocr-jpn-vert
RUN apt-get install tesseract-ocr-script-jpan tesseract-ocr-script-jpan-vert


