from kafka import KafkaProducer

producer = KafkaProducer(value_serializer=str.encode,bootstrap_servers='192.168.99.100:9092')
for i in range(10):
    producer.send('test', str(i))
producer.flush() # Block until all pending messages are at least put on the network