FROM alpine:3.10
# Use alpine linux as base image

COPY . /home/web/

RUN apk add gcc python3 python3-dev libc-dev libffi-dev openssl-dev curl
RUN adduser --disabled-password web && mkdir -p /home/web/log/ && chown -R web.web /home/web/

USER web
WORKDIR /home/web


ENV PATH=$PATH:/home/web/.local/bin \
    PORT=8080 \
    ERRLOG=/home/web/log/error.log \
    ACCESSLOG=/home/web/log/access.log \
    LOGFORMAT="%(h)s %(l)s %(t)s %({Server-IP}o)s %(l)s %(r)s %(s)s %(b)s %(a)s" \
    LOGLVL=INFO \
    SECRET_KEY=DockerFileSecret

# Install application
RUN pip3 install --user -r requirements.txt

EXPOSE 8080

CMD sh run_gunicorn.sh