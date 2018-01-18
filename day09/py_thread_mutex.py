#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/18 20:38
  * @author: by Ysan

  线程锁（互斥锁）
  2.x 会不同
  3.0 不需要，好像优化自带了
'''

import threading
import time

num = 0
thread_list = []
lock = threading.Lock()
def addNum():
    lock.acquire()  # 获取锁
    global num  # 在每个线程中都获取这个全局变量
    print("--ger num ", num)
    # time.sleep(1)
    num += 1    # 对此公共变量进行+1操作
    lock.release()  # 释放锁


for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:   # 等待所有线程执行完毕
    t.join()

print("final num ", num)
