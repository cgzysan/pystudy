#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/20 14:02
  * @author: by Ysan

    通过gevent实现单线程下的多socket并发
'''

import socket
import gevent
from gevent import monkey
monkey.patch_all()


def server(port):
    server = socket.socket()
    server.bind(('localhost', port))
    server.listen(500)
    while True:
        conn, addr = server.accept()
        gevent.spawn(handle_request, conn)


def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024).decode()
            print("recv:", data)
            conn.send(data.upper().encode('utf-8'))
            if not data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()


if __name__ == '__main__':
    server(8989)
