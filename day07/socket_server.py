#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/12 17:44
  * @author: by Ysan
'''

import socket
import json

request = {
    "msgId": 1234567,
    "action": "navigate",
    "data": {
        "customer_id": 1,
        "customer_name": "张三",
        "robot_id": 1000,
        "location_id": 5,
    }
}

location = {
    "msgId": 1234567,
    "action": "move",
    "data": {
        "location_name": "大门口",
        "location_id": 5,
    }
}


server = socket.socket()
server.bind(('192.168.1.165', 8888))
server.listen(5)

conn, addr = server.accept()
print(conn, addr)

while True:
    data = conn.recv(1024)
    print("server receive: ", data)
    # res = json.dumps(request)
    # print("发送>>", res, type(res))
    # conn.send(res.encode("utf-8"))
    # reply = conn.recv(1024)
    # print(reply.decode())
    conn.send(json.dumps(location).encode("utf-8"))
    reply = conn.recv(1024)
    print(reply.decode())

server.close()
