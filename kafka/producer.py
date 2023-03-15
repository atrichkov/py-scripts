import os
import json
from kafka import KafkaProducer

broker = os.environ['kafka_host']
topic = os.environ['kafka_topic']

class MessageProducer:
    broker = ""
    topic = ""
    producer = None

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.broker,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            acks='all',
            retries=3
        )

    def send_msg(self, msg):
        print("sending message...")
        try:
            future = self.producer.send(self.topic, msg)
            self.producer.flush()
            future.get(timeout=60)
            print("message sent successfully...")
            return {'status_code': 200, 'error': None}
        except Exception as ex:
            return ex

message_producer = MessageProducer(broker, topic)

data = {'key1': 'value 1', 'key2': 'value 2', 'key3': 'value 3'}
resp = message_producer.send_msg(data)
print(resp)
