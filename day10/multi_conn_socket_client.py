#!/usr/bin/env python3
'''
  * @time: Created on 20/01/2018 10:19 PM
  * @author: by Ysan

    高并发的socket的链接
'''

import sys
import socket

message = [
    b'This is the message',
    b'It will be send',
    b'in parent',
]

server_address = ('localhost', 9191)

sockets = [
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
]

# print("connecting to %s " % server_address)
for sock in sockets:
    sock.connect(server_address)

for msg in message:
    for s in sockets:
        s.send(msg)

    # Read responses on both sockets
    for s in sockets:
        data = s.recv(1024)
        print('%s: received "%s"' % (s.getsockname(), data))
        if not data:
            print(sys.stderr, 'closing socket', s.getsockname())
