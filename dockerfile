FROM python:3.7-alpine


RUN echo http://mirrors.ustc.edu.cn/alpine/v3.7/main > /etc/apk/repositories && \
    echo http://mirrors.ustc.edu.cn/alpine/v3.7/community >> /etc/apk/repositories && \
    mkdir -p /usr/src/app && \
    mkdir -p /var/log/gunicorn

RUN apk update && apk upgrade


COPY . /usr/src/app
WORKDIR /usr/src/app
RUN  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

EXPOSE 8000
CMD ["/usr/local/bin/gunicorn", "-w", "2", "-b", ":8000", "huojingyuan:app"]