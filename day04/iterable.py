#!/usr/bin/env python3
# by ysan

'''
    可以直接作用于 for 循环的对象统称为可迭代对象：Iterable
    可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

    python 的 Iterator 对象表示的是一个数据流，Iterator 对象可以被 next() 函数调用并不断返回下一个数据，
    知道没有数据时抛出 StopIteration 错误。可以把这个数据看做是一个有序序列，但却不能提前知道序列的长度，
    只能不断通过 next() 函数实现按需计算下一个数据，所以 Iterator 的计算是惰性的，只有在需要返回下一个数据
    的时候它才会计算。
'''

from collections import Iterable

print(isinstance(100, Iterable))

info = {
    'name': 'ysan',
    'age': 24,
    "salary": 7000
}

print(type(info))

for i in range(5):
    print(i, "uuu")
    if i == 3:
        break
else:
    print("nonono")