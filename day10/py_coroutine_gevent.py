#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/20 09:57
  * @author: by Ysan

    Gevent 包装了 Greenlet ，实现协程的自动切换
'''

import gevent
import asyncio


def func1():
    print(12)
    gevent.sleep(2)
    print(34)


def func2():
    print(56)
    gevent.sleep(1)
    print(78)


def task(pid):
    gevent.sleep(1)
    print("Task %s done." % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
])

print("synchronous")
asynchronous()

print("asynchronous:")
asynchronous()
