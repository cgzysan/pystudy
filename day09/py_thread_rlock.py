#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/18 20:55
  * @author: by Ysan

  递归锁 Rlock()
'''

import threading, time


def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num


def run2():
    print("grab the second part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2


def run3():
    lock.acquire()
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res, res2)


if __name__ == '__main__':

    num, num2 = 0, 0
    lock = threading.RLock()
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('----all threads done---')
    print(num, num2)