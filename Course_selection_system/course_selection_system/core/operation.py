#!/usr/bin/env python3
# by ysan

from conf import logger
from lib.people import *

user_data = {  # 初始化帐户数据
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}

log_type = "system"  # 系统日志记录到文件中
system_logger = logger.logger(log_type)


def enroll_student():
    '''学员注册'''
    student = Student()
    student.enroll()
    if student.account:
        print("Account [\033[31;1m%s\033[0m] register sucessed !" % student.account.account_id)
        system_logger.info("Account {} register successful".format(student.account.account_id))
        user_data['is_authenticated'] = True
        user_data['account_id'] = student.account.account_id
        user_data['account_data'] = student
        return student
    else:
        print("\033[31;1mAccount register failed !\033[0m")
        system_logger.info("Account register failed")
        return False


def select_course(base_db):
    if user_data['is_authenticated']:
        student = user_data['account_data']
        if type(student.account.user_info) == dict and "courses" in student.account.user_info:
            print("You are learning a course,please check.【暂不支持已选课程情况】")  # 已有选课，不支持选课
            return

        # 列出学校课程详情
        print("课程信息".center(50, '-'))
        base_data = base_db
