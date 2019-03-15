import time
import pika

# create connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('server'))
channel = connection.channel()

# create a new queue so that future messages can be received
queue_key='hello3'
channel.queue_declare(queue=queue_key, durable=True)

# callback which is being called for each new message
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    
# don't grep more than one message
channel.basic_qos(prefetch_count=1)

# register callback at channel
channel.basic_consume(callback, queue=queue_key)

# start listening and blocking
channel.start_consuming()


