#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/19 14:21
  * @author: by Ysan

    IO 操作不占用CPU， 计算占用CPU
    python 的多线程  不适合cpu密集操作型的任务， 适合io操作密集型的任务

    进程的管理是os管理的
    解决GIL，全局同一时刻只允许一个线程运行问题
    通过多进程，多核cpu启多进程，每一个进程至少有一条线程，
'''

import multiprocessing
import time


def sayhi(name):
    time.sleep(2)
    print("hello %s" % name)


if __name__ == '__main__':
    for i in range(10):
        p1 = multiprocessing.Process(target=sayhi, args=("A%s" % i,))
        p1.start()
