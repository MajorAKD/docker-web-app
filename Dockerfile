FROM python:3.11.2
LABEL maintainer="Akinlabi Akindayo <akinlabiakindayoakd@gmail.com>"

COPY ./WebApp/requirements.txt requirements.txt

RUN pip install uwsgi && pip install -r requirements.txt

ARG UWSGI_HTTP_PORT=8080
ENV UWSGI_HTTP_PORT=$UWSGI_HTTP_PORT

ARG USWGI_APP=webapp
ENV UWSGI_APP=$UWSGI_APP

RUN useradd -ms /bin/bash admin
USER admin

COPY ./WebApp /WebApp
COPY ./uwsgi.ini uwsgi.ini

WORKDIR /WebApp

VOLUME /WebApp

ENTRYPOINT ["uwsgi","--ini","/uwsgi.ini"]

