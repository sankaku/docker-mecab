#!/bin/sh
docker run --rm \
  -v `pwd`/mount/input:/app/input \
  -v `pwd`/mount/output:/app/output \
  -v `pwd`/script.py:/bin/script.py docker-mecab python /bin/script.py
