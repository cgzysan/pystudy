#!/usr/bin/env python3
'''
  * @time: Created on 14/01/2018 4:15 PM
  * @author: by Ysan

  socket 黏包
  两条send语句连一起会发生的概率事件
'''

import socket

client = socket.socket()

client.connect(('localhost', 9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:
        continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size = client.recv(1024)
    print("结果数据大小", cmd_res_size)
    client.send(b"ready")
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):
        print(int(cmd_res_size.decode()))
        data = client.recv(1024)
        received_size += len(data)  # 每次收到的有可能小于1024，所以必须用len判断
        received_data += data
    else:
        print("cmd res receive done...", received_size)
        print(received_data.decode())

client.close()
