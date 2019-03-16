#!/usr/bin/env python

import sys
import pika
import time

# create connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('server'))
channel = connection.channel()

# create a new queue so that future messages can be received
queue_key='hello_queue'
channel.queue_declare(queue=queue_key)


# declare exchange
exchange_key="hello_exchange"
channel.exchange_declare(exchange=exchange_key, exchange_type="fanout")


# publish a message to the exchange
while True:
    message = ' '.join(sys.argv[1:]) or "info: Hello World!"
    channel.basic_publish(exchange=exchange_key,
                        routing_key='',
                        body=message)
    time.sleep(1)






