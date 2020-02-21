FROM alpine:3
RUN apk --update add --no-cache python3 py3-flask py3-gunicorn py3-setuptools py3-psycopg2

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY gunicorn_conf.py /workdir/gunicorn_conf.py
COPY app /workdir/app
WORKDIR /workdir/app

# Set Python path
ENV PYTHONPATH=/workdir

EXPOSE 8080

CMD ["gunicorn", "--config", "/workdir/gunicorn_conf.py", "main:app"]
