FROM python:3.10-buster

ENV APP_HOST 0.0.0.0
ENV APP_PORT 8000
ENV APP_WORKERS 2
ENV APP_WORKER_TIMEOUT 120

ENV DJANGO_ENV=${DJANGO_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.12

# System deps:
RUN python -m pip install -U pip && pip install poetry==$POETRY_VERSION

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

VOLUME /app/database

COPY . /app/
RUN ["chmod", "+x", "start.sh"]
CMD ["/app/start.sh"]