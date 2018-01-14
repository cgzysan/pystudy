#!/usr/bin/env python3
'''
  * @time: Created on 14/01/2018 4:10 PM
  * @author: by Ysan
  通过socket实现简单的ssh

  socket 黏包
  两条send语句连一起会发生的概率事件
'''

import socket
import os

server = socket.socket()
server.bind(('localhost', 9999))

server.listen()

while True:
    conn, addr = server.accept()
    print("new conn: ", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令：", data)
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output..."
        cmd_res_bytes = cmd_res.encode('utf-8')
        conn.send(str(len(cmd_res_bytes)).encode('utf-8'))  # 先发数据大小给客户端
        # time.sleep(0.5)
        client_ack = conn.recv(1024)    # 解决黏包的问题, recv() 收不到数据时堵塞的，wait client to confirm
        conn.send(cmd_res_bytes)

server.close()
