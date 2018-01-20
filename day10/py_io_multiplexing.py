#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/20 15:32
  * @author: by Ysan

    多路复用
    单个process就可以同时处理多个网络连接的io
    实现模式：
    1,  select
    2,  poll
    3,  epoll
'''

# select 通过单进程实现同时处理多个非堵塞的socket连接
# epoll 实现  >>> py_epoll
# 封装后的 selectors >>> py_selectors
import socket
import select
import queue

HOST = "localhost"
PORT = 9999

server = socket.socket()
server.setblocking(False)   # 设置不堵塞
server.bind((HOST, PORT))
server.listen(1000)

inputs = [server, ]
outputs = []
msg_dict = {}

while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    for r in readable:
        if r is server:
            conn, addr = server.accept()
            inputs.append(conn)
            msg_dict[conn] = queue.Queue()
        else:
            print("客户端发来数据")
            client_data = r.recv(1024).decode()
            print(client_data)
            msg_dict[r].put(client_data.upper())
            outputs.append(r)

    for w in writeable:
        try:
            msg = msg_dict[w].get_nowait().encode('utf-8')
        except queue.Empty:
            print('output queue for', w.getpeername(), 'is empty')
            outputs.remove(w)
        else:
            w.send(msg)

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)

        inputs.remove(e)
        e.close()
        del msg_dict[e]
