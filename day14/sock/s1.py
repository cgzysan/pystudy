#!/usr/bin/env python3
'''
  * @time: Created on 2018/02/05 09:06
  * @author: by Ysan
'''

import socket


def handle_request(client):
    buf = client.recv(1024)
    print(buf.decode())
    client.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf-8"))
    with open("h1", "rb") as f:
        # client.send("Hello World".encode("utf-8"))
        data = f.read()
        client.send(data)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        print(conn, addr)
        handle_request(conn)
        conn.close()


if __name__ == '__main__':
    main()
