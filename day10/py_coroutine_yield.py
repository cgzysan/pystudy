#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/19 20:37
  * @author: by Ysan

    通过python自带的yield实现协程
'''

import time


def consumer(name):
    print("Now waiting food...")
    while True:
        new_food = yield
        print("[%s] is eating food[%s]" % (name, new_food))


def producer():
    con = consumer("An")
    con2 = consumer("CX")
    con.__next__()
    con2.__next__()
    n = 0
    while True:
        time.sleep(1)
        n += 1
        con.send(n)
        con2.send(n)
        print("Producer is making food[%s]" % n)


if __name__ == '__main__':
    producer()
