#!/usr/bin/env python3
# by ysan

'''
    python 类（class）多态的应用
'''


class Animal(object):
    def __init__(self, name):
        self.name = name

    # Abstract method, defined by convention only
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def animal_talk(obj):
        obj.talk()


class Cat(Animal):
    def talk(self):
        print("%s miao miao miao!" % self.name)


class Dog(Animal):
    def talk(self):
        print("%s wang wang wang!" % self.name)


c1 = Cat("An")
d1 = Dog("Ki")

Animal.animal_talk(c1)
Animal.animal_talk(d1)
