#!/usr/bin/env python3
# by ysan

import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': '%s/db' % BASE_DIR,
}

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'shopping': 'shopping.log',
    'access': 'access.log',
}
