#!/usr/bin/env python3
# by ysan

import logging
from conf import settings

def logger(log_type, *user_name):
    # crate logger
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    if user_name:
        log_file = "%s/log/%s_%s" % (settings.BASE_DIR, user_name[0], settings.LOG_TYPES[log_type])
    else:
        log_file = "%s/log/%s" % (settings.BASE_DIR, user_name[0], settings.LOG_TYPES[log_type])

    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch and fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch and fh to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
