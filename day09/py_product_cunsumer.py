#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/19 11:34
  * @author: by Ysan

    生产者和消费者模型
    在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。

    为什么要使用生产者和消费者模式
    在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，
    如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。
    同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

    什么是生产者消费者模式
    生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，
    而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，
    而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力
'''

import threading
import time
import queue


def producer():
    count = 0
    while True:
        print("生产了 [%s]" % count)
        q.put("产品 [%s]" % count)
        count += 1
        time.sleep(1)


def consumer(name):
    while True:
        data = q.get()
        print("[%s] 取走了商品 [%s]" % (name, data))


q = queue.Queue()
t1 = threading.Thread(target=producer)
c1 = threading.Thread(target=consumer, args=("CI",))
c2 = threading.Thread(target=consumer, args=("AN",))
t1.start()
c1.start()
c2.start()
