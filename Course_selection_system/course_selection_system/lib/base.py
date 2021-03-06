#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/08 19:03
  * @author: by Ysan
'''

import os
from lib.db import Db
from lib.course import Course
from lib.school import School
from lib.account import Admin
from conf import settings


class BaseDb(object):
    '''基础数据库类'''
    db = Db(settings.BASE_DATABASE)
    db_path = "%s/base.db" % db.db_handler()

    def __init__(self):
        '''
        初始化基础数据课程和学校
        '''
        if os.path.exists(BaseDb.db_path):  # 初始数据库存在时，不做任何操作
            return None

        # 创建课程
        java = Course("java", 8000)
        linux = Course("linux", 10300)
        python = Course("python", 12000)

        # 创建学校两所，北京An，上海An
        beijing_an_school = School("beijing_an_school", "beijing",
                                   {"teachers": []}, {"courses": [java, linux]},
                                   {"students": []}, {"grades": []})
        shanghai_an_school = School("shanghai_an_school", "shanghai",
                                    {"teachers": []}, {"courses": [java, python]},
                                    {"students": []}, {"grades": []})
        base_data = {
            "schools": [beijing_an_school, shanghai_an_school]
        }
        self.save_data(base_data)

        admin_username = 'admin'
        admin_password = 'admin'
        status = 1
        authority = 9
        admin = Admin(admin_username, admin_password, status, authority)
        admin.create()

    @staticmethod
    def save_data(base_data):
        '''
        保存基础数据库
        :param base_data:   基础数据
        :return:
        '''
        BaseDb.db.dump_pickle_data(BaseDb.db_path, base_data)

    @staticmethod
    def get_data():
        base_data = BaseDb.db.load_pickle_data(BaseDb.db_path)
        # 从文件中读取信息
        schools = base_data['schools']
        attr_students = 'students'
        attr_teachers = 'teachers'
        for school in schools:
            students = getattr(school, attr_students)[attr_students]
            teachers = getattr(school, attr_teachers)[attr_teachers]
            for student in students:
                account_id = student.account.account_id
                student.account = student.account.get_account_data(account_id)
                user_info_dict = student.account.user_info
                student.name = user_info_dict.get['name']
                student.sex = user_info_dict.get['sex']
                student.age = user_info_dict.get['age']
            for teacher in teachers:
                account_id = teacher.account.account_id
                teacher.account = teacher.account.get_account_data(account_id)
                user_info_dict = teacher.account.user_info
                teacher.name = user_info_dict.get['name']
                teacher.sex = user_info_dict.get['sex']
                teacher.age = user_info_dict.get['age']
        return base_data
