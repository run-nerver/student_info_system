FROM ubuntu:16.04

LABEL maintainer="BlackRun"
ENV PYTHONIOENCODING=utf-8


RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
&& sed -i s@/security.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
&& apt-get clean \
&& apt-get update \
&& apt-get install -y python3-pip python3-dev nginx supervisor\
&& rm -rf /var/lib/apt/lists/*
ADD pip.conf /etc/pip.conf
COPY supervisord.conf /etc/supervisord.conf
COPY supervisor.conf /etc/supervisor/
RUN pip3 install --upgrade pip 


COPY . /huojingyuan
WORKDIR /huojingyuan
RUN  pip3 install -r requirements.txt \
&& rm -rf /etc/supervisor/supervisord.conf \
&& sed -i 's/nodaemon=false/nodaemon=true/g' /etc/supervisord.conf
EXPOSE 8000
CMD ["supervisord", "-c", "/etc/supervisord.conf"]