FROM python:3.6.12-alpine

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev

RUN mkdir /data && mkdir /data/reference
RUN mkdir /{{cookiecutter.package_name}}

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY ./{{cookiecutter.package_name}} /{{cookiecutter.package_name}}/{{cookiecutter.package_name}}
COPY ./tests /{{cookiecutter.package_name}}/tests
COPY ./requirements.txt /{{cookiecutter.package_name}}/requirements.txt
COPY nginx.conf /etc/nginx/nginx.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /{{cookiecutter.package_name}}

RUN export PYTEST_ADDOPTS="--color=yes"

ENV LANG "C.UTF-8"
ENV LC_ALL "C.UTF-8"
ENV UWSGI_INI /{{cookiecutter.package_name}}/uwsgi-app.ini
