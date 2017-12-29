#!/usr/bin/env python3
# by ysan

import os
import json
from core import db_handler
from core import settings


def acc_auth(account, password):
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account)
    if os.path.isfile(account_file):
        with open(account_file, 'r') as f:
            account_data = json.load(f)


def acc_login(usr_data, log_obj):
    '''
    account login function
    :param usr_data:  user info data, only save in memory
    :param log_obj:  log file
    :return:
    '''
    retry_count = 0
    if usr_data['is_authenticated'] and retry_count < 3:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()

    pass


def acc_sign_in(usr_data):
    print('sign in')
    pass


def acc_logout(usr_data):
    print('logout')
    pass
