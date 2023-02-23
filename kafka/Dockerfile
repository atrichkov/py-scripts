FROM python:3-alpine3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV KAFKA_HOST="0.0.0.0:9092"
ENV KAFKA_TOPIC="test"
ENV KAFKA_MESSAGE="{key: value}"

CMD [ "python3", "producer.py" ]