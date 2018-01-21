#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/20 17:39
  * @author: by Ysan

    selectors 对select,epoll 进行了封装
    实现 IO多路复用 默认用epoll，如果找不到，不支持epoll, 就换select
'''

import selectors
import socket

sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()
    print("accepted", conn, "from", addr, "mask = ", mask)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    print("read mask :", mask)
    data = conn.recv(1024)
    if data:
        print("recv data :", repr(data), "to", conn)
        conn.send(data)
    else:
        print("closing", conn)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 9191))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()   # 默认在此阻塞，有活动链接就返回活动的链接列表
    for key, mask in events:
        callback = key.data  # 调取注册时传入的回调方法，这里就是注册监听时传入的accept
        callback(key.fileobj, mask)  # key.fileobj = fileobj (文件句柄)
