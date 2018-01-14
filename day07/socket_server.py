#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/12 17:44
  * @author: by Ysan
'''

import socket

server = socket.socket()
server.bind(('localhost', 6969))
server.listen()

conn, addr = server.accept()
print(conn, addr)

while True:
    data = conn.recv(1024)
    print("server receive: ", data)
    conn.send(data.upper())

server.close()
