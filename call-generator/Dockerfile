FROM alpine:3.10
# Use alpine linux as base image

COPY . /home/web/

# RUN apk add gcc python3 python3-dev libc-dev libffi-dev openssl-dev
RUN apk add python3
RUN adduser --disabled-password web && mkdir -p /home/web/log/ && chown -R web.web /home/web/

USER web
WORKDIR /home/web


ENV PATH=$PATH:/home/web/.local/bin \
    ERRLOG=/home/web/log/error.log \
    ACCESSLOG=/home/web/log/access.log \
    LOGLVL=INFO

# Install application
# RUN pip3 install --user -r requirements.txt

# EXPOSE 8080

# CMD gunicorn --bind 0.0.0.0:8080 --access-logfile ${ACCESSLOG} --error-logfile ${ERRLOG} --log-level ${LOGLVL} wsgi:app
CMD pyhon client.py