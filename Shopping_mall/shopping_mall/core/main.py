#!/usr/bin/env python3
# by ysan

from core import auth
from core import logger
from conf import goods

user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None,
}

access_logger = logger.logger('access')
shopping_cart = {}
all_cost = 0


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
            exit_flag = menu_dict[user_option](user_data, access_logger)
        else:
            print("\033[31;1mOption does not exist!\033[0m")


def show_shopping_cart(usr_data):
    '''
    show shopping cart list and user info data
    :param usr_data:
    :return:
    '''
    if usr_data['is_authenticated']:
        for value in shopping_cart:
            pass


def list_one_layer():
    '''
    print one layer goods
    :return:
    '''
    one_layer_list = []
    print("Species list".center(50, "-"))
    for index, value in enumerate(goods.menu):
        print("\033[31;1m%d\033[0m --> %s" % (index, value))
        one_layer_list.append(value)
    print("END".center(50, "-"))
    print("[q|b] to quit;[c] to check;[t] to top up")

    once_choice = input("Input your choice:").strip()
    if once_choice.isdigit():
        once_choice = int(once_choice)
        if 0 <=  once_choice < len(goods.menu):
            print("---->Enter \033[32;1m%s\033[0m" % (one_layer_list[once_choice]))
            two_layer_list = goods.menu[one_layer_list[once_choice]]
            return two_layer_list
        else:
            print("\033[31;1mNumber out of range, please enter again!\033[0m")
    else:
        if once_choice == 'b' or once_choice == 'back' or once_choice == 'q' or once_choice == 'quit':
            pass
    return None


def list_two_layer(two_layer_list):
    '''
    print two layer goods
    :return:
    '''
    print("Product list".center(50, "-"))
    for item in enumerate(two_layer_list):
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print("%s.%-20s %-20s" % (index, p_name, p_price))
    print("END".center(50, "-"))
    print("[q|quit] to quit;[b|back] to back;[c|check] to check")


def go_shopping(usr_data, log_obj):
    '''
    shopping function
    :param usr_data:  memory account info data
    :param log_obj:
    :return:
    '''
    flag = False
    while not flag:
        two_layer_list = list_one_layer()

        exit_flag = False
        while not exit_flag:
            list_two_layer(two_layer_list)
            user_choice = input("Please choice the product:").strip()
            if user_choice.isdigit():
                user_choice = int(user_choice)
                if 0 <= user_choice < len(two_layer_list):
                    product_number = input("Please input the number of product:").strip()
                    if product_number.isdigit():
                        product_number = int(product_number)
                    else:
                        continue

                p_item = two_layer_list[user_choice]
                # goods name
                p_name = p_item[0]
                # goods price
                p_price = int(p_item[1])


def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    print("Welcome to Shopping mall!".center(50, "-"))
    interactive()
    print(user_data)
    # define shopping log
    log_type = 'shopping'
    shopping_logger = logger.logger(log_type, user_data['account_id'])
    go_shopping(user_data, shopping_logger)
    pass
