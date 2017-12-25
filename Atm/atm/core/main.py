# by ysan
#!/usr/bin/env python3

'''
    main program handle module, handle all the user interaction stuff
'''

import os
from core import auth
from core import logger
from core import accounts
from core import transaction
from core import db_handler
from conf import settings

user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}

trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')


# 1. 账号信息
def account_info(usr_data):
    back_flag = False
    while not back_flag:
        info = u'''
        ---------- Welcome [%s] ----------
        登录状态：%s
        注册时间：%s
        过期时间：%s
        信用额度：%s
        余额：%s
        pay_day：%s
        ''' % (usr_data['account_id'],
               usr_data['is_authenticated'],
               usr_data['account_data']['enroll_date'],
               usr_data['account_data']['expire_date'],
               usr_data['account_data']['credit'],
               usr_data['account_data']['balance'],
               usr_data['account_data']['pay_day'])
        print(info)
        user_choice = input("'b' return to the previous level>>")
        if user_choice == 'b':
            back_flag = True


# 2. 还款
def repay(usr_data):
    account_data = accounts.load_current_balance(usr_data['account_id'])
    current_balance = '''
    ---------- [%s] balance info ----------
    Credit  : %s
    Balance : %s 
    ''' % (account_data['id'],
           account_data['credit'],
           account_data['balance'])
    print(current_balance)

    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            account_data_new = transaction.make_transaction(account_data, 'repay', repay_amount, trans_logger)
            if account_data_new:
                print("\033[42;1mNew Balance:%s\033[0m" % (account_data_new['balance']))
        else:
            print("\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m" % repay_amount)

        if repay_amount == 'b':
            back_flag = True


# 3. 取款
def withdraw(usr_data):
    account_data = accounts.load_current_balance(usr_data['account_id'])
    current_balance = '''
    ---------- [%s] balance info ----------
    Credit  : %s
    Balance : %s 
    ''' % (account_data['id'],
           account_data['credit'],
           account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            account_data_new = transaction.make_transaction(account_data, 'withdraw', withdraw_amount, trans_logger)
            if account_data_new:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (account_data_new['balance']))
        else:
            print("\033[31;1m[%s] is not a valid amount, only accept integer !\033[0m" % withdraw_amount)

        if withdraw_amount == 'b':
            back_flag = True


# 4. 转账
def transfer(usr_data):
    account_data = accounts.load_current_balance(usr_data['account_id'])
    current_balance = '''
    ---------- [%s] balance info ----------
    Credit  : %s
    Balance : %s 
    ''' % (account_data['id'],
           account_data['credit'],
           account_data['balance'])
    print(current_balance)

    back_flag = False
    while not back_flag:
        transfer_target = input("\033[33;1mInput transfer amount id:\033[0m")
        db_path = db_handler.db_handler(settings.DATA_BASE)
        account_file = "%s/%s.json" % (db_path, transfer_target)
        while not os.path.isfile(account_file):
            if transfer_target == 'b':
                back_flag = True
                break
            transfer_target = input("\033[31;1m%s is not exist, enter again:\033[0m" % transfer_target)
            account_file = "%s/%s.json" % (db_path, transfer_target)
        if back_flag:
            break
        transfer_amount = input("\033[33;1mInput transfer amount:\033[0m")
        while not (len(transfer_amount) > 0 and transfer_amount.isdigit()):
            if transfer_target == 'b':
                back_flag = True
                break
            transfer_amount = input("\033[31;1m[%s] is not a valid amount, only accept integer ! enter again:\033[0m"
                                    % transfer_amount)
        if back_flag:
            break
        transfer_info = '''u[%s] will transfer %s to %s, if you confirm the operator, please input "y"''' \
                        % (account_data['id'], transfer_amount, transfer_target)
        print(transfer_info)

        transfer_confirm = input("\033[33;1m'y' or any to continue>>")
        if transfer_confirm == 'y':
            account_data_new = transaction.make_transaction(account_data, 'transfer', transfer_amount,
                                                            trans_logger, transfer_target)
            if account_data_new:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (account_data_new['balance']))
        elif transfer_confirm == 'b':
            back_flag = True
        else:
            pass


# 5. 账单
def account_bill(usr_data):
    print(">>>账单")


# 6. 注销
def logout(usr_data):
    print("account [%s] logout successful" % usr_data['account_id'])
    usr_data['account_id'] = None
    usr_data['account_data'] = None
    usr_data['is_authenticated'] = False
    run()


# 7. 退出
def atm_exit(usr_data):
    usr_data['account_id'] = None
    usr_data['account_data'] = None
    usr_data['is_authenticated'] = False
    exit("Thanks!")


def interactive(usr_data):
    '''
    interactive with user
    :param usr_data: user info data
    :return:
    '''
    menu = u'''
    ---------- Ysan Bank ----------
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  注销
    7.  退出
    \033[0m'''
    menu_dict = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': account_bill,
        '6': logout,
        '7': atm_exit,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dict:
            menu_dict[user_option](usr_data)


def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    print("小缘")
    acc_data = auth.acc_login(user_data, access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)  # 交互
