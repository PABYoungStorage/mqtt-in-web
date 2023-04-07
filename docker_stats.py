import pika
import subprocess
import time
import json
from threading import Thread
import sys

client = "172.19.0.2"

try:
    credentials = pika.PlainCredentials('anish', 'dotmail123')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('172.17.0.10',
                                5672,
                                '/',
                                credentials))
    channel = connection.channel()

    channel.queue_declare(queue='testwire',durable=True)
except Exception as a:
    print(a)

def DockerStats():
    tx = "docker stats --no-stream | grep traefik_anish_1 | awk '{print "'"cpu "'" $3} {print "'"Memory_Usage "'" $4 $5 $6} {print "'"Memory_Percentage "'" $7} {print "'"Net_I "'" $8 $9 $10} {print "'"Block_I "'" $11 $12 $13} {print "'"PID "'" $14}'"
    # print (tx)
    sent = subprocess.run(tx,shell=True,capture_output=True,encoding="utf-8")
    sent2 = sent.stdout
    memdata = {}
    for i in sent2.split("\n"):
        j = i.split(" ")
        if len(j) == 2:
            memdata[j[0]] = j[1]
    print(memdata)
    time.sleep(2)

    channel.basic_publish(exchange='', routing_key='testwire', body=json.dumps(memdata))

def WgPing():
    # Run the "ping" command with a count of 1 and a timeout of 1 second
    result = subprocess.run(["ping", "-c", "1", "-W", "1", client], capture_output=True, text=True)
    # Parse the output to check the ping status
    if "1 received" in result.stdout:
        channel.basic_publish(exchange='', routing_key='testwire', body=json.dumps({"connected":True}))
        # print(result)
        print(f"{client}: ping OK")
    else:
        channel.basic_publish(exchange='', routing_key='testwire', body=json.dumps({"connected":False}))
        # print(result)
        print(f"{client}: ping failed")

try:
    while True:
        docketstats = Thread(target=DockerStats)
        ping = Thread(target=WgPing)

        docketstats.start()
        ping.start()

        docketstats.join()
        ping.join()

except KeyboardInterrupt:
    connection.close()
    print("ctrl+c happens")
    sys.exit(1)
except Exception as e:
    print(e)