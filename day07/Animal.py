#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/12 10:08
  * @author: by Ysan
'''


class Dog(object):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat():
        print("eating")

    @classmethod
    def sleep(cls):
        print(cls)

    @property
    def drink(self):
        status = self.checking_status()
        if status == 0:
            print("drinking0")
        elif status == 1:
            print("drinking1")
        elif status == 2:
            print("drinking2")
        elif status == 3:
            print("drinking3")

    def checking_status(self):
        print("checking status %s" % self.name)
        return 1

    @drink.setter
    def drink(self, status):
        status_dict = {
            1: "yyy",
            2: "uuu",
            3: "iii",
        }
        print("\033[31;1mHas changed the status %s\033[0m" % status_dict.get(status))

    @drink.deleter
    def drink(self):
        print("status got remove...")

    def __call__(self, *args, **kwargs):
        print("__call__方法", *args, **kwargs)

    def __str__(self):
        return ("Ysan")

    def __getitem__(self, item):
        print('__getitem__', item)
        return getattr(self, item)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        setattr(self, key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


d = Dog("An")
d.eat()
d.sleep()
d.drink
d.drink = 2
del d.drink

print("--------------------------- 类的特殊成员方法 ------------------------------")
print("__doc__ 表示类的描述信息".center(50, "-"))
print(d.__doc__)
print(Dog.__doc__)
print("__module__ 表示当前操作的对象在那个模块".center(50, "-"))
print(d.__module__)
print(Dog.__module__)
print("__class__ 表示当前操作的对象的类是什么".center(50, "-"))
print(d.__class__)
print(Dog.__class__)
print("__call__ 对象后面加括号，触发执行".center(50, "-"))
d.__call__('A', 'B')
print("__dict__ 查看类或对象中的所有成员".center(50, "-"))
print(d.__dict__)
print(Dog.__dict__)
print("__str__ 如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值".center(50, "-"))
print(d)
print(Dog)
print("__getitem__、__setitem__、__delitem__，获取，设置，删除数据".center(50, "-"))
hh = d['name']
print(hh)
d['name'] = 'Ys'
print(d['name'])

