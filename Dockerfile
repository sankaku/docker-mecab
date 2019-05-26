FROM python:3
RUN apt-get update \
    && apt-get install -y mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file \
    && apt-get install -y swig

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && cd mecab-ipadic-neologd \
    && yes yes | ./bin/install-mecab-ipadic-neologd -n -p /usr/local/lib/mecab \
    && rm -rf mecab-ipadic-neologd

COPY ./requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
