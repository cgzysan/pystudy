#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/19 15:04
  * @author: by Ysan

    获取进程id
    linux 每一个进程都是父进程启动的
'''

import multiprocessing
import os


def info(title):
    print(title)
    print('module name: ', __name__)
    print('parent precess: ', os.getppid())
    print('process id: ', os.getpid())
    print("\n\n")


def f(name):
    info('\033[31;1mcalled from child process\033[0m')
    print("hello %s" % name)


if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p1 = multiprocessing.Process(target=f, args=("An",))
    p1.start()