#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/19 16:50
  * @author: by Ysan

    Manager实现进程间的数据共享
'''

import os
from multiprocessing import Process, Manager


def f(d, l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()  # 生成一个字典，可在多个进程间共享和传递
        l = manager.list(range(5))  # 生成一个列表，可在多个进程间共享和传递

        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)
