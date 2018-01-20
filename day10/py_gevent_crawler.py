#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/20 10:18
  * @author: by Ysan
'''

import gevent
import time
from urllib.request import urlopen
from gevent import monkey
monkey.patch_all()  # 把当前程序的所有的io操作给我单独的做上标记


def f(url, filename):
    print("GET: %s" % url)
    resp = urlopen(url)
    data = resp.read()
    with open(filename, 'wb') as f:
        f.write(data)


time_start = time.time()
gevent.joinall([
    gevent.spawn(f, "https://www.python.org/", "python"),
    gevent.spawn(f, "https://www.yahoo.com/", "yahoo"),
    gevent.spawn(f, "https://github.com/", "github"),
])
time_end = time.time()
print("花费了时间>>", time_end - time_start)
