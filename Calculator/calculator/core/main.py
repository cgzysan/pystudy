#!/usr/bin/env python3
# by ysan

import re

def compute(calc):
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


def run():
