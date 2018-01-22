#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/22 14:41
  * @author: by Ysan
'''

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print("[x] received %r" % body)


channel.basic_consume(callback, queue='hello', no_ack=True)

print("Waiting for messages...")
channel.start_consuming()
