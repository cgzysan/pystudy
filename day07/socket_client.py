#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/12 17:39
  * @author: by Ysan
'''


import socket

client = socket.socket()
client.connect(('localhost', 6969))
client.send(b"Hello World!")
data = client.recv(1024)
print("client receive: ", data)
client.close()
