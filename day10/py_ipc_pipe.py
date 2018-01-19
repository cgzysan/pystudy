#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/19 15:28
  * @author: by Ysan

    通过pipe(管道，电话线)，实现进程通讯
'''

from multiprocessing import Process, Pipe


def f(conn):
    conn.send(['An', 25, 'white'])
    conn.send("你还好吗")
    print(conn.recv())
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    res = parent_conn.recv()
    print(res)
    print(parent_conn.recv())
    parent_conn.send("I'm fine Thank you")
    p.join()
