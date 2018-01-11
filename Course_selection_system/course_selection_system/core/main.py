#!/usr/bin/env python3
# by ysan

import os
import pickle
from conf import settings
from lib.base import BaseDb
from core import operation

base_db = BaseDb()  # 第一次运行生成初始化数据库，后续登录读取数据库到内存


def welcome():
    '''
    Welcome to the course selection system
    :return:
    '''
    menu = '''
    ----------------- 欢迎进入选课系统 -----------------
        1.  \033[33;1m学员系统\033[0m
        2.  \033[34;1m讲师系统\033[0m
        3.  \033[35;1m系统管理\033[0m
        4.  退出
    --------------------------------------------------
        '''
    menu_dict = {
        '1': 'system_student()',
        '2': 'system_teacher()',
        '3': 'system_manager()',
        '4': 'logout()',
    }
    interactive(menu, menu_dict)


def system_student():
    '''
    student system
    :return:
    '''
    menu = '''
    ----------------- 欢迎进入学员系统 -----------------
        1.  \033[33;1m学员注册\033[0m
        2.  \033[34;1m进入选课\033[0m
        3.  \033[35;1m查看班级\033[0m
        4.  \033[36;1m查看个人信息\033[0m
        5.  \033[37;1m修改个人信息\033[0m
        6.  后退（注销）
    --------------------------------------------------
    '''
    menu_dict = {
        '1': 'operation.enroll_student()',
        '2': 'operation.select_course(base_db)',
        '3': 'operation.show_grade_info(base_db)',
        '4': 'operation.show_account_info()',
        '5': 'operation.modify_info()',
        '6': 'callback("logout")',
    }
    interactive(menu, menu_dict)


def system_teacher():
    '''
    teacher system
    :return:
    '''
    menu = '''
----------------- 欢迎进入讲师系统 -----------------
    1.  \033[33;1m授课排课\033[0m
    2.  \033[34;1m查看学员信息\033[0m
    3.  \033[35;1m修改学员成绩\033[0m
    4.  \033[36;1m查看个人信息\033[0m
    5.  \033[37;1m修改个人信息\033[0m
    6.  \033[38;1m查看学校\033[0m
    7.  后退（注销）
--------------------------------------------------
    '''
    menu_dict = {
        '1': 'operation.course_schedule(base_db)',
    }


def system_manager():
    pass


def logout():
    exit(" 谢谢使用 ".center(50, "#"))


def callback(action=None):
    # 注销帐户
    if action == "logout":
        operation.user_data = {
            'account_id': None,
            'is_authenticated': False,
            'account_data': None,
        }
    break_flag = "b"
    # print(operate.user_data)
    return break_flag


def interactive(menu, menu_dict):
    '''
    user interactive func
    :param menu:
    :param menu_dict:
    :return:
    '''
    exit_flag = False
    while exit_flag != 'b':
        print(menu)
        user_option = input(">>>").strip()
        if user_option in menu_dict:
            exit_flag = eval(menu_dict[user_option])
        else:
            print("\033[31;1mOption does not exist!\033[0m")


def test():
    db_path = "%s/%s/%s" % (settings.BASE_DIR, "db", "increment_id")
    if os.path.exists(db_path):
        with open(db_path, "rb") as f:
            data1 = pickle.load(f)
        print("increment_id", data1)

    db_ss = "%s/%s/%s/%s" % (settings.BASE_DIR, "db", "accounts", "user_names")
    if os.path.exists(db_ss):
        with open(db_ss, "rb") as f:
            data2 = pickle.load(f)
        print("user_names", data2)
    else:
        print("不存在")


def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    welcome()
    # test()
