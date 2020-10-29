FROM python:3.7

RUN pip install -U celery[redis]

COPY ./src /src

WORKDIR /src

ENTRYPOINT [ "celery","-A","proj","worker","--loglevel=INFO" ]