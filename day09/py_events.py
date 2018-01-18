#!/usr/bin/env python3
'''
  * @time: Created on 18/01/2018 10:57 PM
  * @author: by Ysan

  通过Event来实现两个或多个线程间的交互，
  下面是一个红绿灯的例子，即起动一个线程做交通指挥灯，生成几个线程做车辆，车辆行驶按红灯停，绿灯行的规则。

  wait() 等待标志位设定   阻塞
  set() 设置全局变量
  clear() 清空全局变量
'''

import time
import threading

event = threading.Event()


def lighter():
    count = 0
    while True:
        if count > 5 and count < 10:  # 改成红灯
            event.clear()   # 清标志位
            print("\033[41;1mred light is on...\033[0m")
        elif count > 10:
            event.set()  # 变绿灯
            count = 0
        else:
            print("\033[42m;1mgreen light is on...\033[0m")
        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():  # 代表绿灯
            print("[%s] running..." % name)
        else:
            print("[%s] sees red light, waiting..." % name)
            event.wait()
            print("\033[34;1m[%s] green light is on, start going...\033[0m" % name)
