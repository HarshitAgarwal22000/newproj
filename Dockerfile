FROM python:3.8-slim

WORKDIR /app

COPY venv /app/venv/
COPY app.py /app/
COPY templates /app/templates/
COPY requirements.txt /app/

RUN /app/venv/bin/pip install --trusted-host pypi.python.org -r /app/requirements.txt

EXPOSE 5000

CMD ["/app/venv/bin/python", "app.py"]
