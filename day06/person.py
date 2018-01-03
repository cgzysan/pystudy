#!/usr/bin/env python3
# by ysan

'''
    python 类（class）的运用
    类变量的用途，大家共用的属性
'''


class people(object):
    def __init__(self, name, age, sex, salary):
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary

    def say_hello(self):
        print("hello, my name is %s, I have %s years old" % (self.name, self.age))

    def go_shooping(self):
        print("My salary is %s, and I will shopping at once" % self.salary)


p1 = people('ysan', '25', 'm', '7000')
p1.say_hello()
p1.go_shooping()