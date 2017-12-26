#!/usr/bin/env python3
# by ysan
import sys

'''
    列表(list)的方法
    pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
'''

dict_my = {'a': 1, 'b': 2, 'c': 3}


def test(info, *args):
    str1 = "".join(args)
    str2 = args
    print(str1, type(str1))
    print(str2, type(str2))


def test_dict(info, **kwargs):
    print(info)
    print(kwargs)


# 列表切片？ 切片是什么
list1 = [1, 2, 3, 4, 5, 6]

# 列表生成式
list2 = [i*2 for i in range(10)]

print(list1)
print(list2)

print("-".center(100, "-"))
print("backend www.oldboy.org".split())


print("--------- 列表的额外参数测试 ----------")
test("ysan", "123456", "wo", "shi")

print("--------- 字典的额外参数测试 ----------")
test_dict("ysan", a=1, b=2, c=3)
print(dict_my)
print(*dict_my)

print("---------- 环境变量 ----------")
sys_path = sys.path
print(sys_path)

for i in sys_path:
    print(i)
