FROM python:3.9-bullseye
WORKDIR /app
COPY . /app

RUN pip install -qr requirements.txt 2>/dev/null

CMD python app.py