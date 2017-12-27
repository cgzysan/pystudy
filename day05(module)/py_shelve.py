#!/usr/bin/env python3
# by ysan

import shelve

'''
    简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式
'''

d = shelve.open('shelve_test')


class Test(object):
    def __init__(self, n):
        self.n = n


def print_author(author):
    print("this is from %s!" % author)


t = Test(123)
t2 = Test(112233)

# 以k,v的形式写入文件

# name = ['a', 'b', 'c', 'd']
# d['alphabet'] = name
# d['t1'] = t
# d['t2'] = t2
# d['author'] = print_author
#
# d.close()

# 读取数据
for i in d.items():
    print(i)

d.get('t2')
d.get('author')('ysan')

