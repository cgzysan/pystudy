#!/usr/bin/env python3
# by ysan

from core import logger
from lib.people import *
from conf import settings

user_data = {  # 初始化帐户数据
    'account_id': None,
    'is_authenticated': False,
    'account_data': None,
}

log_type = "system"  # 系统日志记录到文件中
system_logger = logger.logger(log_type)


def check_login(func):
    '''
    检查是否登录
    :return:
    '''
    def inner(*args, **kwargs):
        if user_data.get("is_authenticated", None):
            ret = func(*args, **kwargs)
            return ret
        else:
            # 登录流程：通过输入用户、密码，取用户得到用户对应的id的帐户，再对比密码
            print("\033[33;1mPlease sign in!\033[0m")
            person = Person()
            person.sign_in()
            转换成子类保存

            if person.account:
                user_data['is_authenticated'] = True
                user_data['account_id'] = person.account.account_id
                user_data['account_data'] = person
                print("\033[32;1mSign in success!\033[0m")
                system_logger.info("Account {} sign in successful!".format(user_data['account_id']))
            else:
                system_logger.info("Sign in failed")
    return inner


def check_authority(arg):
    '''检查权限'''
    def _check_authority(func):
        def inner(*args, **kwargs):
            person = user_data['account_data']
            if person.account.authority == arg:
                ret = func(*args, **kwargs)
                return ret
            else:
                print("Account \033[31;1m{}\033[0m permission access denied.".format(user_data['account_id']))
                system_logger.info("Account {} permission access denied.".format(user_data['account_id']))
        return inner
    return _check_authority


def enroll_student():
    '''学员注册'''
    student = Student()
    student.enroll()
    if student.account:
        print("Account [\033[31;1m%s\033[0m] register successful !" % student.account.account_id)
        system_logger.info("Account {} register successful".format(student.account.account_id))
        user_data['is_authenticated'] = True
        user_data['account_id'] = student.account.account_id
        user_data['account_data'] = student
        return student
    else:
        print("\033[31;1mAccount register failed !\033[0m")
        system_logger.info("Account register failed")
        return False


@check_login
@check_authority(settings.AUTHORITY['student'])
def select_course(base_db):
    if user_data['is_authenticated']:
        student = user_data['account_data']
        if type(student.account.user_info) == dict and "courses" in student.account.user_info:
            print("You are learning a course,please check.【暂不支持已选课程情况】")  # 已有选课，不支持选课
            return

        # 列出学校课程详情
        print("课程信息".center(50, '-'))
        base_data = base_db.get_data()
        schools = base_data['schools']
        for school in schools:
            print("学校名称：\033[34;1m{}\033[0m".format(school.school_name))
            school.show_info('courses')
            print("--------------------------------------------------")

        # 选课
        flag = True
        while flag:
            print("Please input the course name of want to learn,"
                  "eg: [ \033[33;1mshanghai_an_school.java\033[0m ]")
            school_course = input(">>: ").strip()
            s_school = school_course.split(".")[0]
            s_course = school_course.split(".")[1]

            for school in schools:
                if school.school_name == s_school:
                    for course in school.courses['courses']:
                        if course.name == s_course:
                            student.select_course(user_data['account_id'], s_course)
                            school.add_attr_value('students')


@check_login
def show_account_info():
    '''
    查看个人信息
    :return:
    '''
    print(" 个人信息 ".center(50, "-"))
    user_data['account_data'].account.show_info()
