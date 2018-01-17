#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/15 19:28
  * @author: by Ysan
'''

import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_LEVEL = logging.INFO

# 不同操作不同的log文件
LOG_TYPES = {
    'xxx': 'xxx.log',
    'ggg': 'ggg.log',
}

'''
    engine  >>> 文件保存类型
    name    >>> 父文件夹路径
    path    >>> 文件根路径
'''
DATA_BASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': '%s/db' % BASE_DIR,
}

HOST = "localhost"
PORT = 9999
