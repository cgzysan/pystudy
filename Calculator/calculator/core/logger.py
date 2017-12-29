#!/usr/bin/env python3
# by ysan

import logging
from conf import settings


def logger(log_tpye):
    # create logger
    logger = logging.getLogger(log_tpye)
    logger.setLevel(settings.LOG_LEVEL)

    # create console handle and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    # create file handler and set level to warning
    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOG_TYPES[log_tpye])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch , fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch and fh to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
