#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/19 19:45
  * @author: by Ysan

    协程  又称微线程   协程是一种用户态的轻量级线程
    遇到IO操作就切换

    协程的特点：
    1. 必须在只有一个单线程里实现并发
    2. 修改数据不需要加锁
    3. 用户程序里自己保存多个控制流的上下文栈
    4. 一个协程遇到IO操作自动切换到其他协程

    python 自带的 yield 实现
    Greenlet 实现手动切换
    Gevent 包装了Greenlet ，实现自动切换
    切换之后，通过回调方法切换回来
'''
