#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/20 14:11
  * @author: by Ysan
'''

import socket


HOST = 'localhost'
PORT = 9191

client = socket.socket()
client.connect((HOST, PORT))

while True:
    data = input(">>>").strip()
    client.sendall(data.encode('utf-8'))
    resp = client.recv(1024)
    print("server resp:", resp.decode())

client.close()
