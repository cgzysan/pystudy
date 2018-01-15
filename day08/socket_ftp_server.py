#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/15 09:00
  * @author: by Ysan
'''

import socket
import os
import hashlib

server = socket.socket()

server.bind(('localhost', 8989))
server.listen()

while True:
    conn, addr = server.accept()
    print("new conn: ", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
        file_path = data.decode()
        print(file_path)
        if os.path.isfile(file_path):
            file_size = str(os.stat(file_path).st_size).encode('utf-8')
            conn.send(file_size)
            ready = conn.recv(1024)
            print('准备好', ready.decode())
            if ready.decode().startswith("ready"):
                m = hashlib.md5()
                with open(file_path, 'rb') as f:
                    for line in f:
                        m.update(line)
                        conn.send(line)
                    complete = conn.recv(1024)
                    if complete.decode().startswith("complete"):
                        conn.send(m.hexdigest().encode('utf-8'))
                    else:
                        pass
