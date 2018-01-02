#!/usr/bin/env python3
# by ysan

import json
import os
from conf import settings
from core import db_handler


def load_account_data(account_id):
    '''
    achieve account info data
    :param account_id:  account
    :return: account info data
    '''
    db_path = db_handler.db_handler(settings.DATA_BASE)
    account_file = "%s/%s.json" % (db_path, account_id)
    if os.path.isfile(account_file):
        with open(account_file, 'r') as f:
            acc_data = json.load(f)
            return acc_data


def dump_account_data(acc_data):
    '''
    dump account info data to file
    :param acc_data: account info data
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATA_BASE)
    account_file = "%s/%s.json" % (db_path, acc_data['id'])
    with open(account_file, 'w') as f:
        json.dump(acc_data, f)
