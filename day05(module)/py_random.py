#!/usr/bin/env python3
# by ysan

import random

# 随机[0,1)浮点数
print(random.random())
# 随机整数[x, y]
print(random.randint(1, 3))
# 随机整数[x, y)
print(random.randrange(1, 3))
# 从序列中获取一个元素
print(random.choice("hello world"))
# 从序列中获取n个元素，n由第二个参数决定
print(random.sample("hello world", 3))
# 获取指定区间的浮点数
print(random.uniform(1, 3))
# 洗牌
items = [1, 2, 3, 4, 5, 6]
print(items)
random.shuffle(items)
print(items)
