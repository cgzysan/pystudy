#!/usr/bin/env python3
# by ysan

import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'history': 'history.log'
}
