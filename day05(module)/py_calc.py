#!/usr/bin/env python3
# by ysan

import re

s1 = 'abca(bc)a456c'
pattern1 = '\([^()]+\)'

ss = re.search(pattern1, s1)
print(ss)
print(ss.group())

'''
    简单的python计算器
    实现加减乘除及括号优先级解析
    思路：
    首先找到最内部的括号运算
    正则表达式，首先[^()]+ 找多次出现的除左右括号以外的字符，然后 \([^()]+\) 匹配外面有一层括号，以为需要匹配正常括弧，需要\转义
'''


def calculator(calc):
    print(calc)
    number = re.findall(r"\d+", calc)
    operator = re.findall(r"[\+\-\*\/]", calc)
    operator2 = []

    print(operator)
    print(number)

    for index, ope in enumerate(operator):
        if ope == '*':
            res = float(number[index]) * float(number[index + 1])
            number[index] = None
            number[index + 1] = res
        elif ope == '/':
            res = float(number[index]) / float(number[index + 1])
            number[index] = None
            number[index + 1] = res
        else:
            operator2.append(ope)

    print(operator)
    print(number)
    print(operator2)
    ret = [str for str in number if str not in ['', ' ', None]]     # 可以将 list中的None,'',' ' 删除
    print(ret)

    for k, v in enumerate(operator2):
        if v == '+':
            result = float(ret[k]) + float(ret[k + 1])
            ret[k + 1] = result
        elif v == '-':
            result = float(ret[k]) - float(ret[k + 1])
            ret[k + 1] = result

    print(ret)

# s = '1 - 2 * ((60-30 + (-40/5 + (5 + 5)) * (9-2*5/3 + 7 / 3*99/4*2998 + 10 * 568/14)) - (-4*3) / (16-3*2))'
# pattern = r'\([^()]+\)'
# comp = re.compile(pattern)
# ii = comp.findall(s)
# sss = re.findall(pattern, s)
# print(ii)
# s4 = re.sub(r'\(5 \+ 5\)', '10', s)
# # s4 = s.replace(ii[0], '10')
# print(s4)
# print(sss)

ssss = "-9-2.343*5/3 + 7 / 3.3412*9.9/4*2998.412 + 10.00000000000 * 562.8/14"
expression = re.sub('\s*', '', ssss)  # 去除空格

a = re.findall(r"\d+\.?\d*", expression)
b = re.findall(r"[+\-*/]", expression)
print(ssss)
print(expression)
print(a)
print(b)
# items = [1, 2, 3, 4, 5, 6, 7]
# oppe = ['-', '*', '/', '+', '/', '*', '/', '*', '+', '*', '/']
#
# print('/' in oppe)
#
#
# b = True
# for k, a in enumerate(items):
#     print(k, a)
#     if b:
#         items.pop(3)
#         b = False
#
# print(items)
#
# print("--------------------- calculator test ---------------------")
# calculator(ssss)

