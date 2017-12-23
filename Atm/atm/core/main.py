# by ysan
#!/usr/bin/env python3

'''
    main program handle module, handle all the user interaction stuff
'''

from core import auth
from core import logger

user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}

access_logger = logger.logger('access')

def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    print("小缘")
    acc_data = auth.acc_login(user_data, access_logger)
