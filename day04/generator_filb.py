#!/usr/bin/env python3
# by ysan


'''
    生成器之斐波那契数列
    1，1，2，3，5，8，13，21，34...
    除了第一个数和最后一个数，都是前两位数的和
'''


def filb(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)  换成 yield b 变为生成器 yield 有中断保存当前状态的作用
        yield b
        a, b = b, a + b
        n += 1
    return "hello world"


# filb(10)
f = filb(10)
print(f)
while True:
    try:
        # res = next(f)
        res = f.__next__()
        print(res)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break

# next() 方法可以用，__next__()也可以用
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())