# by ysan
#!/usr/bin/env python3

'''
    handle all the logging works
    logging.debug/info/warning('This is warning message')
    默认情况下，logging将日志打印到屏幕，日志级别为WARNING
    打印：WARNING:root:This is warning message
    日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET

    logging.formatter参数参考：http://www.mamicode.com/info-detail-317126.html
'''


import logging
from conf import settings

def logger(log_type):

    # create logger
    logger = logging.getLogger(log_type)  # 默认root
    logger.setLevel(settings.LOG_LEVEL)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    # create file handler and set level to warning
    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOG_TYPE[log_type])
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
