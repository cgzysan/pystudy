#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/19 17:00
  * @author: by Ysan

    进程同步，进程锁，屏幕打印不乱
'''

from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    print("hello ", i)
    l.release()


if __name__ == '__main__':
    lock = Lock()

    for i in range(10):
        Process(target=f, args=(lock, i)).start()
