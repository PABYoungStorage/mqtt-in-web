import pika
import subprocess
import time
import re
import json

credentials = pika.PlainCredentials('anish', 'dotmail123')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('172.17.0.10',
                              5672,
                              '/',
                              credentials))
channel = connection.channel()

channel.queue_declare(queue='9652c9a480a8eth0',durable=True)

while True:
    tx = "ifconfig | grep -B 0 -A 5 wg0 | grep 'TX packets' | awk '{print $6 ,$7}'  "
    sent = subprocess.run(tx,shell=True,capture_output=True,encoding="utf-8")
    sent2 = sent.stdout
    time.sleep(2)

    channel.basic_publish(exchange='', routing_key='9652c9a480a8eth0', body=json.dumps({"tx":sent2}))
    print(sent2)
connection.close()


# import subprocess
# import time
# while True:
#     tx = "ifconfig | grep -B 0 -A 5 peer-22 | grep 'TX packets' | awk '{print $6 ,$7}' | grep -Eo '[0-9]+\.[0-9]' "
#     rx = "ifconfig | grep -B 0 -A 5 peer-22 | grep 'RX packets' | awk '{print $6 ,$7}' | grep -Eo '[0-9]+\.[0-9]' "
#     subprocess.run(tx,shell=True)
#     subprocess.run(rx,shell=True)
#     time.sleep(2)