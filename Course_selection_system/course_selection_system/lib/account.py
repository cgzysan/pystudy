#!/usr/bin/env python3
# by ysan

import os
import re
from conf import settings
from lib.db import Db


class Account(object):
    '''
    账号信息
    '''
    db = Db(settings.ACCOUNT_DATABASE)  # 数据库连接，公共属性
    db_path = db.db_handler()

    def __init__(self, user_name, password, status=settings.STATUS['normal'],
                 authority=settings.AUTHORITY['student'], user_info={}):
        '''
        定义账号属性
        :param user_name:   用户名，字符属性
        :param password:    密码，字符属性
        :param status:      账号状态，整数类型
        :param authority:   账号权限，整数类型
        :param user_info:   用户信息，字典类型
        '''
        self.user_name = user_name
        self.password = password
        self.status = status
        self.authority = authority
        self.user_info = user_info

    def show_info(self):
        '''查看user_info属性'''
        print("account_id: \033[32;1m{}\033[0m".format(self.account_id))
        if self.user_info:
            for k in self.user_info:
                print("{}: \033[32;1m{}\033[0m".format(k, self.user_info[k]))

    def create(self):
        '''
        创建新账号
        :return: 账户实例
        '''
        # 获取自增长id
        begin_id = 10000
        auto_increment_file = "%s/increment_id" % os.path.dirname(Account.db_path)
        if os.path.exists(auto_increment_file):
            line = Account.db.load_pickle_data(auto_increment_file)
            auto_increment_id = int(line) + 1
        else:   # 自增长id文件不存在
            id_list = []
            files_list = os.listdir(Account.db_path)
            for f in files_list:
                exist_flag = re.match(r'^(\d{5,})', f)
                if exist_flag:
                    id_list.append(f)

            if id_list:
                id_list.sort()
                max_id = int(id_list[-1])
                auto_increment_id = max_id + 1
            else:
                auto_increment_id = begin_id

        self.account_id = auto_increment_id
        check_flag = self.check_user_name(auto_increment_id)
        if not check_flag:  # 用户名不存在，才创建用户
            user_file = "%s/%s" % (Account.db_path, auto_increment_id)
            Account.db.dump_pickle_data(auto_increment_file, auto_increment_id)
            Account.db.dump_pickle_data(user_file, self)
            return self
        else:
            print("User name [\033[31;1m%s\033[0m] has been registered!" % self.user_name)
            return False

    def check_user_name(self, account_id):
        '''
        查询数据库用户名是否存在
        :param account_id:  用户名，字符类型
        :return:  True 存在，False 不存在
        '''
        user_names = []  # 初始化用户名数据库
        exist_flag = False  # 初始存在标记
        user_names_file = "%s/user_names" % Account.db_path
        if os.path.exists(user_names_file):
            user_names = Account.db.load_pickle_data(user_names_file)
            for usr in user_names:
                if usr["user_name"] == self.user_name:
                    exist_flag = usr["account_id"]
                    return exist_flag

        user_names.append({"account_id": account_id, "user_name": self.user_name})
        Account.db.dump_pickle_data(user_names_file, user_names)

    @staticmethod
    def get_account_data(account_id):
        '''
        获取账户数据
        :param account_id: 账户id
        :return:
        '''
        exist_flag = False
        user_file = "%s/%s" % (Account.db_path, account_id)
        if os.path.exists(user_file):
            account = Account.db.load_pickle_data(user_file)
            return account
        print("Account [\033[31;1m%s\033[0m] does not exist!" % account_id)
        return exist_flag

    @staticmethod
    def get_account_id(user_name):
        '''
        用user_name查询出account_id
        :param user_name:
        :return:
        '''
        exist_flag = False
        user_name_file = "%s/user_names" % Account.db_path
        if os.path.exists(user_name_file):
            user_names = Account.db.load_pickle_data(user_name_file)    # 获取用户名：id 的列表数据
            for u_n in user_names:
                if u_n['user_name'] == user_name:
                    exist_flag = u_n['account_id']
                    return exist_flag

        print("User name [\033[31;1m%s\033[0m] does not exist!" % user_name)
        return exist_flag

    def save_data(self, account_id):
        '''保存数据至数据库
        :param account_id: 帐户id
        '''
        user_file = "%s/%s" % (Account.db_path, account_id)
        Account.db.dump_pickle_data(user_file, self)  # 保存帐户数据

    def login(self):
        '''
        用户输入的是账号，通过账号获取account_id验证登录
        :return:    账号实例
        '''
        account_id = self.get_account_id(self.user_name)
        if account_id:
            account = self.get_account_data(account_id)
            if account.password == self.password:
                if self.status == settings.STATUS['normal']:
                    return account
                else:
                    print("Account locked, [\033[31;1m%s\033[0m] sign in failed!" % self.user_name)
                    return False
            else:
                print("Password error, [\033[31;1m%s\033[0m] sign in failed!" % self.user_name)
                return False
        else:
            print("User name [\033[31;1m%s\033[0m] does not exist!" % self.user_name)
            return False


class Admin(Account):
    '''管理员帐户'''

    def manage_teachers(self):
        '''管理学校讲师'''
        print("管理学校讲师")

    def manager_students(self):
        '''管理学校学员'''
        print("管理学校学员")

    def manager_banjis(self):
        '''管理学校班级'''
        print("管理学校班级")
