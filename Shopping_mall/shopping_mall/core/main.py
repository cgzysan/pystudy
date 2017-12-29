#!/usr/bin/env python3
# by ysan

from core import auth

user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None,
}


def interactive():
    login_menu = u'''
    --------------- personal center ---------------
    \033[32;1m1. 登录
    2. 注册
    3. 注销
    \033[0m'''
    menu_dict = {
        '1': auth.acc_login,
        '2': auth.acc_sign_in,
        '3': auth.acc_logout,
    }
    exit_flag = False
    while not exit_flag:
        print(login_menu)
        user_option = input(">>>").strip()
        if user_option in menu_dict:
            menu_dict[user_option](user_data)


def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    print("Welcome to Shopping mall!".center(50, "-"))
    interactive()
    pass
