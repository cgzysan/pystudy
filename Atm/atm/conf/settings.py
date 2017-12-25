# by ysan
#!/usr/bin/env python3

import logging, os

LOG_LEVEL = logging.INFO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 不同操作不同的log文件
LOG_TYPES = {
    'transaction': 'transaction.log',
    'access': 'access.log',
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

TRANSACTION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0},
    'withdraw': {'action': 'minus', 'interest': 0.05},
    'transfer': {'action': 'minus', 'interest': 0.05},
    'consume': {'action': 'minus', 'interest': 0},
}
