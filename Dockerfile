FROM python:alpine

WORKDIR /app

RUN apk add firefox \
    && apk add --no-cache --virtual .pynacl_deps build-base libffi-dev \
    && pip3 install selenium

COPY /app .

RUN crontab -l | { cat; echo "* 18 * * * python3 /app/skelbiu-renew.py"; } | crontab -

CMD ["crond", "-f"]