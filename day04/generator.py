#!/usr/bin/env python3
# by ysan

'''
    列表容量收到内存限制，如果创建一个大容量的列表，却仅仅只访问几个元素，
    会导致大部分的元素空间都被浪费了。
    如果列表元素可以按照某种算法推算出来，就可以在循环的过程中不断的推算
    后续的元素，在python中，这种一边循环一边计算的机制，称为生成器：generator


    1.生成器只有在调用的时候才能生成相应的数据
    2.只记录当前位置
    3.只有一个 __next__() 方法，在2.7中 >>> next()

    yield 的作用
        1.中断保存当前状态
        2.通过 next() 方法可以从函数外返回函数内 yield 的位置
        3.通过 send() 方法可以给 yield 发送一个值，同时从函数外返回
'''

# 通过 yield 实现在单线程的情况下实现并发运算效果
# 异步IO的雏形   协程
import time


def customer(name):
    print("%s要开始吃包子了" % name)
    while True:
        baozi = yield
        print("包子[%s]来了，被%s吃掉了" % (baozi, name))


def produce(num):
    c1 = customer("A")
    c2 = customer("B")
    c1.__next__()
    c2.__next__()
    print("老子开始做包子了！")
    for i in range(num):
        time.sleep(1)
        print("老子做了两个包子，第%s次")
        c1.send("韭菜馅")
        c2.send("大葱馅")


produce(5)

