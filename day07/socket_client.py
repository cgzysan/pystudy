#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/12 17:39
  * @author: by Ysan
'''


import socket

client = socket.socket()
client.connect(('localhost', 6969))

while True:
    di = input("send>>:")
    client.send(di.encode('utf-8'))
    data = client.recv(1024)
    print("client receive: ", data.decode('utf_8'))

client.close()
