FROM python:3.11.2-slim

RUN useradd -d /home/wsgi -m -s /bin/bash -u 0 -o -g root wsgi
USER wsgi

ENV DockerHOME=/home/wsgi

RUN mkdir -p $DockerHOME

WORKDIR /home/wsgi

ADD ./backend/requirements/base.txt /home/wsgi/backend/requirements/

ENV PATH=/home/wsgi/.local/bin:$PATH

RUN pip install --upgrade pip

RUN python3 -m pip install --upgrade Pillow
RUN pip3 install -r backend/requirements/base.txt

ADD --chown=wsgi:wsgi ./backend /home/wsgi/backend
ADD --chown=wsgi:wsgi ./docker /home/wsgi/docker

RUN chmod +x /home/wsgi/docker/backend/wsgi_entrypoint.sh

