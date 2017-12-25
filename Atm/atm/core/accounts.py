#!/usr/bin/env python3
# by ysan

import json
from core import db_handler
from conf import settings


def load_current_balance(account_id):
    '''
    achieve account balance
    :param account_id:  account id
    :return:    return account balance and other basic info
    '''
    db_path = db_handler.db_handler(settings.DATA_BASE)
    account_file = "%s/%s.json" % (db_path, account_id)
    with open(account_file, 'r') as f:
        acc_data = json.load(f)
        return acc_data


def dump_update_account(acc_data):
    '''
    after updated transaction or account data, dump is back to file db
    :param acc_data:    update account data
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATA_BASE)
    account_file = "%s/%s.json" % (db_path, acc_data['id'])
    with open(account_file, 'w') as f:
        json.dump(acc_data, f)
