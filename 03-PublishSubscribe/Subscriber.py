#!/usr/bin/env python

import pika

# create connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('server'))
channel = connection.channel()

# create a queue with a temporary name
result = channel.queue_declare(exclusive=True)

# bind to exchange
exchange_key="hello_exchange"
channel.queue_bind(exchange=exchange_key, queue=result.method.queue)

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

    
channel.basic_consume(callback,
                      queue=result.method.queue,
                      no_ack=True)

channel.start_consuming()




