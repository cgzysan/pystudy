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


# 1. 账号信息
def account_info(acc_data):
    print(acc_data)


# 2. 还款
def repay(acc_data):
    pass


# 3. 取款
def withdraw(acc_data):
    pass


# 4. 转账
def transfer(acc_data):
    pass


# 5. 账单
def account_bill(acc_data):
    pass


# 6. 退出
def logout(acc_data):
    pass


def interactive(acc_data):
    '''
    interactive with user
    :param acc_data: user info data
    :return:
    '''
    menu = u'''
    ---------- Ysan Bank ----------
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''
    menu_dict = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': account_bill,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dict:
            menu_dict[user_option](acc_data)


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
