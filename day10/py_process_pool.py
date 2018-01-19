#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/19 17:01
  * @author: by Ysan

    进程池

    apply           同步
    apply_async     异步  参数中可以传入callback，callback的参数由func的返回值传入
'''

from multiprocessing import Process, Pool
import time
import os


def func(i):
    time.sleep(2)
    print("in precess ", os.getpid())
    return i + 100


def call(*args):
    print("callback args", args[0])


def bar(i):
    print("__>exec done ", i)


if __name__ == '__main__':
    pool = Pool(processes=3)

    for i in range(10):
        pool.apply(func=func, args=(i,))
        pool.apply_async(func, args=(i,), callback=bar)     # callback方法不给参数，将会等func方法返回值传入，如果直接给参将，将会直接执行

    print("end")
    pool.close()
    pool.join()     # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
