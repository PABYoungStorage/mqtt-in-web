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

channel.queue_declare(queue='testwire')

while True:
    tx = "docker stats --no-stream | grep traefik_anish_1 | awk '{print "'"cpu "'" $3} {print "'"Memory_Usage "'" $4 $5 $6} {print "'"Memory_Percentage "'" $7} {print "'"Net_I/O "'" $8 $9 $10} {print "'"Block_I/O "'" $11 $12 $13} {print "'"PID "'" $14}'"
    sent = subprocess.run(tx,shell=True,capture_output=True,encoding="utf-8")
    sent2 = sent.stdout

    time.sleep(2)

    channel.basic_publish(exchange='', routing_key='testwire', body=json.dumps({"rx":sent2}))
    print(sent2)
connection.close()
