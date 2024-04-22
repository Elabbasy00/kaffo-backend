FROM python:3.11.2-slim

RUN useradd --create-home --shell /bin/bash wsgi
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



# RUN chmod +x /app/docker/backend/asgi.entrypoint.sh