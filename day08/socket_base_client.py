#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/15 16:49
  * @author: by Ysan
'''

import socket

client = socket.socket()
client.connect(('localhost', 9999))

while True:
    op = input(">>>:").strip()
    client.send(op.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode())
