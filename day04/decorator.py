#!/usr/bin/env python3
# by ysan
import time

'''
    装饰器
    1.函数即变量
    2.高阶函数
        a.把一个函数名当做实参传给另外一个函数（在不修改被装饰函数源代码的情况下为其添加功能）
        b.返回值中包含函数名（不修改函数的调用方式）
    3.嵌套函数
    
    高阶函数 + 嵌套函数 => 装饰器

'''

def deco(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the func run time %s" % (stop_time - start_time))

# 装饰器实现
def timer1(func):
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time %s" % (stop_time - start_time))
    return deco

# 传参数 *args 和 **kwargs 有所区别？？
# 列表切片
def timer2(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print("the func run time %s" % (stop_time - start_time))
    return deco


@timer2  # 语法糖 == func = timer(func)
def func1():
    time.sleep(3)
    print("this is func1")

@timer2
def func2():
    time.sleep(4)
    print("this is func2")

@timer2
def func3(name, age):
    print(name, age)

# 如果被装饰的函数有参数，timer1 装饰器无法完成，优化成 timer2

# deco(func1)
# func2 = timer(func2)
# func1()
# func2()
func3("ysan",26)

