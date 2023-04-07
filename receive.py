import pika, sys, os,re

def main():
    credentials = pika.PlainCredentials('anish', 'dotmail123')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('172.17.0.10',
                              5672,
                              '/',
                              credentials))
    channel = connection.channel()

    channel.queue_declare(queue='testwire')

    def callback(ch, method, properties, body):
        receive = body.decode()
        exclude = ['\n']
        normal_string = "".join(filter(lambda char: char not in exclude , receive))
        print(" [x] Received %r" % receive)

    channel.basic_consume(queue='testwire', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)