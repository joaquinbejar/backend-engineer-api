FROM python:3.13-bookworm
WORKDIR /app
COPY . /app

RUN pip install -qr requirements.txt 2>/dev/null

CMD python app.py