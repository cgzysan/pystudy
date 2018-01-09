#!/usr/bin/env python3
# by ysan

from lib.account import Account


class Person(object):
    '''人基类'''

    def __init__(self, name=None, age=None, sex=None, account=None):
        '''
        定义人的基本属性
        :param name:    名字，字符类型
        :param age:     年龄，数字类型
        :param sex:     性别，字符类型
        :param account  账户：实例
        '''
        self.name = name
        self.age = age
        self.sex = sex
        self.account = account

    def enroll(self, authority=1):
        '''
        注册账号
        :return:    账号实例
        '''
        user_name = input("Please input user name >>: ").strip()
        password = input("Please input password >>: ").strip()
        re_password = input("Please input password confirmation >>: ").strip()
        if password != re_password:
            print("\033[31;1mPasswords do not match!\033[0m")
            return False
        status = 1
        account = Account(user_name, password, status, authority)
        new_account = account.create()
        self.account = new_account
        return self

    def sign_in(self):
        '''
        登录账户
        :return:
        '''
        login_flag = False
        user_name = input("Please input user name >>: ").strip()
        password = input("Please input password >>: ").strip()
        account = Account(user_name, password)
        self.account = account.login()
        if self.account:
            login_flag = self.account
        return login_flag


class Student(Person):
    '''学生类'''

    def select_course(self, account_id, course):
        '''
        选课，把课程信息更新到账户中
        :param account_id:  账户id
        :param course:      课程
        :return:
        '''
        self.account.user_info = dict(self.account.user_info)
        self.account.user_info['courses'] = [course]
        self.account.save_data(account_id)
