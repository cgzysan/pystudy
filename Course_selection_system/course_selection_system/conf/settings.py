#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/08 13:50
  * @author: by Ysan
'''

import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'system': 'system.log',
}

'''
    engine  >>> 文件保存类型
    name    >>> 父文件夹路径
    path    >>> 文件根路径
'''
ACCOUNT_DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': '%s/db' % BASE_DIR,
}

BASE_DATABASE = {
    'engine': 'file_storage',
    'name': 'base',
    'path': '%s/db' % BASE_DIR,
}

AUTHORITY = {
    'student': 1,
    'teacher': 2,
    'admin': 9,
}

STATUS = {
    'normal': 1,
    'locked': 2,
}
