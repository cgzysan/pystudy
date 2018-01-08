#!/usr/bin/env python3
# by ysan

from core import operation

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
        '2': 'operation.select_course()',
        '3': 'operation.enroll_student()',
        '4': 'operation.enroll_student()',
        '5': 'operation.enroll_student()',
        '6': 'operation.enroll_student()',
    }
    interactive(menu, menu_dict)


def system_teacher():
    pass


def system_manager():
    pass


def logout():
    exit(" 谢谢使用 ".center(50, "#"))


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


def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    welcome()
