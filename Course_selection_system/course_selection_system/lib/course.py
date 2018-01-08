#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/08 19:18
  * @author: by Ysan
'''


class Course(object):
    '''课程类'''

    def __init__(self, course_name, price):
        '''
        定义课程属性
        :param course_name: 课程名称，字符类型
        :param price:       课程价格，整数类型
        '''
        self.name = course_name
        self.price = price

    def show_info(self):
        '''
        输入课程信息
        :return:
        '''
        print("课程：\033[33;1m{:<15}\033[0m价格：\033[32;1m{:<6}\033[0m".format(self.name, self.price))
