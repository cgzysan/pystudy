#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/08 14:34
  * @author: by Ysan
'''

import logging
from conf import settings


def logger(log_type):
    # create logger
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOG_TYPES[log_type])

    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    formatter = logging.Formatter('%s(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
