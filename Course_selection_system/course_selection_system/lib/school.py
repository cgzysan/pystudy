#!/usr/bin/env python3
# by ysan


class School(object):
    '''学校类'''

    def __init__(self, school_name, city_name, teachers=None, courses=None, students=None, grades=None):
        '''
        定义学校属性
        :param school_name: 学校名，字符类型
        :param city_name:   城市名，字符类型
        :param teachers:    讲师，字典类型，eg:{"teacher": []}
        :param courses:     课程，字典类型，eg:{"courses": []}
        :param students:    学员，字典类型，eg:{"students": []}
        :param grades:       班级，字典类型，eg:{"grades": []}
        '''
        self.school_name = school_name
        self.city_name = city_name
        self.teachers = teachers
        self.courses = courses
        self.students = students
        self.grades = grades

