#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/11 11:32
  * @author: by Ysan
'''

import datetime


class Grade(object):
    '''班级类'''

    def __init__(self, name, courses):
        '''
        定义班级属性
        :param name:    班级名称，字符属性
        :param courses: 学习课程名称，字典类型
        :param students: 学员，字典类型
        :param teachers: 讲师，字典类型
        :param begin_date: 开课时间，默认为班级创建时间
        :param status: 是否已开课，默认开课后不允许添加新成员  0 为开课， 1 为已开课
        '''
        self.name = name
        self.courses = {"courses": courses}
        self.students = {"students": []}
        self.teachers = {"teachers": []}
        self.begin_date = datetime.datetime.now()
        self.status = 0

    def show_info(self):
        '''显示班级信息'''
        print(" 班级信息 ".center(50, "-"))
        print("class name: ")
        print("\033[34;1m{}\033[0m".format(self.name))

        print("teachers: ")
        for teacher in self.students['teachers']:
            if teacher.name:
                print("\033[34;1m{}\033[0m".format(teacher.name))

        print("students: ")
        for student in self.students['students']:
            if student.name:
                print("\033[34;1m{}\033[0m".format(student.name))
