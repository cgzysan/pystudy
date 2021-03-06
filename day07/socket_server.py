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
server.bind(('localhost', 6565))
server.listen(5)

conn, addr = server.accept()
print(conn, addr)

while True:
    data = conn.recv(1024)
    print("server receive: ", data)
    choice = input(">>>").strip()
    if choice == '1':
        res = json.dumps(request)
        print("发送>>", res, type(res))
        conn.send(res.encode("utf-8"))
    elif choice == '2':
        print()
        conn.send(json.dumps(location).encode("utf-8"))
    elif choice == '3':
        conn.send("".encode("utf-8"))

server.close()
