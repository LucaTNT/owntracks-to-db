FROM python:3.9-slim

RUN adduser --system --no-create-home --uid 1001 owntracks-to-db && mkdir /app && chown owntracks-to-db /app

WORKDIR /app

COPY --chown=1001:1001 app/requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY --chown=1001:1001 app /app

USER owntracks-to-db

ENTRYPOINT [ "/usr/local/bin/python3", "/app/app.py" ]
