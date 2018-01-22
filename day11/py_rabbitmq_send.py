#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/22 14:37
  * @author: by Ysan

    http://www.cnblogs.com/wupeiqi/articles/5132791.html
'''

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World')

print("[x] send hello world")
conn.close()
