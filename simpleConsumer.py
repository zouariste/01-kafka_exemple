from kafka import KafkaConsumer


print('debut')
consumer = KafkaConsumer('test', 
    bootstrap_servers='192.168.99.100:9092',
    auto_offset_reset='earliest', 
    enable_auto_commit=True)

for message in consumer:
    print('msg : ', message.value.decode('utf-8'))
