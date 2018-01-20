#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/20 09:55
  * @author: by Ysan

    greenlet 实现协程手动切换
'''

from greenlet import greenlet


def test1(x, y):
    print(12)
    z = gr2.switch(x, y)
    print(56, z)
    gr2.switch()


def test2(*args):
    print(34, args)
    gr1.switch("yyy")
    print(78)


if __name__ == '__main__':
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch("hello", "world")
