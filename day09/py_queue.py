#!/usr/bin/env python3
'''
  * @time: Created on 19/01/2018 7:36 AM
  * @author: by Ysan

  队列
  queue.Queue()
  数据只有一份，与列表的区别
  queue.get(block, timeout)  block 设置么有数据是否卡主， timeout 设置取数据的超时时间
  先入先出  queue.get_nowait()

  queue.LifoQueue()
  后进先出

  queue.PriorityQueue()
  存储数据时可以设置优先级
  q.put((priority(int), "name"))
'''

import queue
