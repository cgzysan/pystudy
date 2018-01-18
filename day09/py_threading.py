#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/18 18:26
  * @author: by Ysan

    json(timeout) 使主线程等待子线程的完成，参数timeout是一个数值类型，表示超时时间，如果未提供该参数，那么主调线程将一直堵塞到被调线程结束。
    setDaemon(True) 将main线程设置为Daemon线程,子线程做为程序主线程的守护线程,当主线程退出时,m线程也会退出,由m启动的其它子线程会同时退出,不管是否执行完任务
'''

import threading
import time


def sayhi(num):
    print("running on number %s" % num)
    time.sleep(2)
    print("done!")


if __name__ == '__main__':
    t1 = threading.Thread(target=sayhi, args=(1,))
    t2 = threading.Thread(target=sayhi, args=(2,))

    # 将main线程设置为Daemon线程,子线程做为程序主线程的守护线程,当主线程退出时,子线程也会退出,由该子线程启动的其它子线程会同时退出,不管是否执行完任务
    t1.setDaemon(True)
    t2.setDaemon(True)

    t1.start()
    t2.start()
    # json() 方法使主线程等待子线程完成
    # t1.join(timeout=1)
    # t2.join()
    print(threading.main_thread(), "---done---")
