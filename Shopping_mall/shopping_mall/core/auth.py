#!/usr/bin/env python3
# by ysan

import os
import json
from core import accounts


def acc_auth(account, password):
    '''
    account auth func
    :param account:  account id
    :param password: account password
    :return: account info data
    '''
    account_data = accounts.load_account_data(account)
    if account_data:
        if account_data['password'] == password:
            return account_data
        else:
            print("\033[31;1mAccount ID or password is incorrect!\033[0m")
    else:
        print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)


def acc_login(usr_data, log_obj):
    '''
    account login function
    :param usr_data:  user info data, only save in memory
    :param log_obj:  log file
    :return:
    '''
    retry_count = 0
    while not usr_data['is_authenticated'] and retry_count < 3:
        account = input("\033[32;1mAccount:\033[0m").strip()
        password = input("\033[32;1mPassword:\033[0m").strip()
        auth = acc_auth(account, password)
        if auth:
            usr_data['is_authenticated'] = True
            usr_data['account_id'] = account
            usr_data['account_data'] = auth
            print("Welcome! %s" % account)
            return True
        retry_count += 1
    else:
        log_obj.error("account [%s] to many login attempts!" % account)
        exit()


def acc_sign_in(usr_data, log_obj):
    '''
    account sign in data
    :param usr_data:  user info data, only save in memory
    :return:
    '''
    if not usr_data['is_authenticated']:
        account = input("\033[32;1mSign in account:\033[0m").strip()
        password = input("\033[32;1mSign in password:\033[0m").strip()
        confirm_pwd = input("\033[32;1mConfirm sign in password:\033[0m").strip()
        while confirm_pwd != password:
            print("\033[42;1mThe two password don't accordance, please input again!")
            password = input("\033[32;1mSign in password:\033[0m").strip()
            confirm_pwd = input("\033[32;1mConfirm sign in password:\033[0m").strip()
        account_data = dict()
        account_data['id'] = account
        account_data['account'] = account
        account_data['password'] = password
        accounts.dump_account_data(account_data)
        return True


def acc_logout(usr_data, log_obj):
    print('logout')
    pass
