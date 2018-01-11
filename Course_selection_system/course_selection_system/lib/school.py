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
        :param grades:      班级，字典类型，eg:{"grades": []}
        '''
        self.school_name = school_name
        self.city_name = city_name
        self.teachers = teachers
        self.courses = courses
        self.students = students
        self.grades = grades

    def show_info(self, attr=None):
        '''
        打印学校信息
        :param attr:
        :return:
        '''
        attr_list = ["courses", "teachers", "students", "grades"]

        def show_attr_value(attr):
            attr_value = getattr(self, attr)    # 字典类型
            attr_value_list = attr_value[attr]  # 列表类型
            print("{} :".format(attr))
            for a in attr_value_list:  # 循环显示
                # a.show_info()
                if a.name:
                    print("\033[34;1m{}\033[0m".format(a.name))
                else:  # 显示人的帐户名
                    print("\033[34;1m{}\033[0m".format(a.account.user_name))

        if attr in attr_list:
            show_attr_value(attr)
        else:
            for attr in attr_list:
                show_attr_value(attr)

    def add_attr_value(self, attr, item):
        '''
        学校添加属性
        :return:
        '''
        attr_value = getattr(self, attr)    # 字典类型
        attr_value_list = attr_value[attr]  # 列表类型
        if item not in attr_value_list:
            attr_value_list.append(item)
        else:
            print("{} already exist.".format(item))
