import subprocess
import time
import pika
import json

credentials = pika.PlainCredentials('anish', 'dotmail123')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('172.17.0.10',
                              5672,
                              '/',
                              credentials))
channel = connection.channel()

channel.queue_declare(queue='9652c9a480a8eth0',durable=True)

# Define the IP addresses or hostnames of the clients you want to ping
clients = ["172.19.0.2"]

# Loop indefinitely to ping the clients periodically
while True:
    # Iterate over the list of clients and ping each one
    for client in clients:
        # Run the "ping" command with a count of 1 and a timeout of 1 second
        result = subprocess.run(["ping", "-c", "1", "-W", "1", client], capture_output=True, text=True)

        # Parse the output to check the ping status
        if "1 received" in result.stdout:
            channel.basic_publish(exchange='', routing_key='9652c9a480a8eth0', body=json.dumps({"connected":True}))
            print(f"{client}: ping OK")
        else:
            channel.basic_publish(exchange='', routing_key='9652c9a480a8eth0', body=json.dumps({"connected":False}))
            print(f"{client}: ping failed")

    # Wait for some time before pinging the clients again
    time.sleep(3)

connection.close()


