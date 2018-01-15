#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/15 19:28
  * @author: by Ysan
'''

import logging
from conf import settings


def logger(log_type):
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    return logger
