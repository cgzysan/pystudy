#!/usr/bin/env python3
'''
  * @time: Created on 18/01/2018 10:51 PM
  * @author: by Ysan

  互斥锁 同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据
'''

import threading, time


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s\n" % n)
    semaphore.release()


if __name__ == '__main__':

    num = 0
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()

while threading.active_count() != 1:
    pass  # print threading.active_count()
else:
    print('----all threads done---')
    print(num)
