#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/19 15:24
  * @author: by Ysan

  通过进程queue实现进程间通讯
'''

from multiprocessing import Process, Queue


def f(q):
    q.put(['An', 26, 'black'])


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=f, args=(q,))
    p1.start()

    print(q.get())
    p1.join()
