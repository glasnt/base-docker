FROM python:3.6.3-slim-stretch

ENV PYTHONUNBUFFERED=1 \
    PIP_REQUIRE_VIRTUALENV=false \
    WHEELS_PLATFORM=aldryn-baseproject-py36 \
    PATH=/virtualenv/bin:/root/.local/bin:$PATH \
    PROCFILE_PATH=/app/Procfile \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

COPY stack /stack/base
RUN apt-get update
RUN apt-get install -y wget curl

RUN DEBIAN_FRONTEND=noninteractive /stack/base/install.sh
RUN DEBIAN_FRONTEND=noninteractive /stack/base/install2.sh

RUN virtualenv --no-site-packages /virtualenv

ENTRYPOINT ["/tini", "-g", "--"]

ADD Procfile /app/Procfile
CMD ["start", "web"]
