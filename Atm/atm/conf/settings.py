# by ysan
#!/usr/bin/env python3

import logging, os

LOG_LEVEL = logging.INFO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_TYPES = {
    'transaction': 'transaction.log',
    'access': 'access.log'
}

DATA_BASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': '%s/db' % BASE_DIR
}