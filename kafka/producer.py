import sys
import json
from kafka import KafkaProducer

broker = ''
topic = sys.argv[1]


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

data = {'a': 'GAB7WM22CNLUYZA25XS4TAXHRSVEIQ4GO6DX2NJGNVC2XZKW366W6635', 'ht': 44314785}
resp = message_producer.send_msg(data)
print(resp)
