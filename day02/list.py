#!/usr/bin/env python3
# by ysan

'''
    列表(list)的方法
    pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
'''

def test(info, *args):
    str1 = "".join(args)
    str2 = args
    print(str1)
    print(str2, type(str2))



# 列表切片？ 切片是什么
list1 = [1, 2, 3, 4, 5, 6]

# 列表生成式
list2 = [i*2 for i in range(10)]

print(list1)
print(list2)

print("-".center(100, "-"))
print("backend www.oldboy.org".split())

test("ysan", "123456", "wo", "shi")
