#!/usr/bin/env python3
# by ysan

import re
import sys
from core import logger


def input_func():
    '''
    输入计算表达式，同时进行判断
    :return:
    '''
    while True:
        expression = input("Please input your expression\033[31;1m q\033[0m to quit：").strip()
        if expression == 'q':
            sys.exit("Bye bye".center(30, "*"))
        elif len(expression) == 0:
            continue
        elif re.match("[A-Z]+", expression, flags=re.I):
            print("\033[31;1mThe input expression is not correct, please input again!\033[0m")
            continue
        else:
            expression = re.sub('\s*', '', expression)  # 去空格
            return expression


def deal_expression(expression):
    '''
    对运算表达式进行运算符的去重处理
    :param expression:
    :return:
    '''
    expression = expression.replace('+-', '-')  # 替换表达式里的所有'+-'
    expression = expression.replace('--', '+')  # 替换表达式里的所有'--'
    expression = expression.replace('-+', '-')  # 替换表达式里的所有'-+'
    expression = expression.replace('++', '+')  # 替换表达式里的所有'++'
    return expression


def achieve_final_result(expression):
    '''
    获取运算表达式最里面括号的表达式, 进行递归计算
    :return:  最终的运算结果
    '''
    expression = deal_expression(expression)
    pattern = r'\([^()]+\)'
    com = re.compile(pattern)
    sub_expression = com.findall(expression)
    if len(sub_expression) > 0:
        for sub in sub_expression:
            res = compute(sub.replace('(', '').replace(')', ''))
            # expression = re.sub(sub, str(res), expression)
            expression = expression.replace(sub, str(res))
        return achieve_final_result(expression)  # 递归函数调用，如果这里不写return, 会发生return None的情况，以为并没有走else
    else:
        return expression


def compute(calc):
    '''
    加减乘除运算
    :param calc:  运算表达式
    :return:    运算结果
    '''
    number = re.findall(r"\d+\.?\d*", calc)
    operator = re.findall(r"[+\-*/]", calc)

    if len(number) == len(operator):
        pop = operator.pop(0)
        number[0] = pop + number[0]

    operator2 = []
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

    ret = [str for str in number if str not in ['', ' ', None]]     # 可以将 list中的None,'',' ' 删除

    for k, v in enumerate(operator2):
        if v == '+':
            result = float(ret[k]) + float(ret[k + 1])
            ret[k + 1] = result
        elif v == '-':
            result = float(ret[k]) - float(ret[k + 1])
            ret[k + 1] = result

    return ret[len(ret) - 1]


def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    exit_flag = False
    print("Welcome to calculator".center(30, "*"))
    while not exit_flag:
        try:
            expression = input_func()
            # 左右加上括号，利于运算
            expression = '(' + expression + ')'
            result = str(achieve_final_result(expression))
            res = str(float(eval(expression)))  # 用eval计算验证

            if res == result:
                print("The expression result is %s" % result)
            else:
                print("The expression correct result:\033[32;1m%s\033[0m" % res)
                print("The expression of calculator result:\033[32;1m%s\033[0m" % result)

            log_type = "history"  # 历史记录记录到文件中
            history_logger = logger.logger(log_type)
            history_logger.info("Expression: %s=%s" % (expression, result))
        except(SyntaxError, ValueError, TypeError):     # 如果有不合法输出，则抛出错误
            print("\033[31;1m Error! The input expression is not correct, please check again!\033[0m")
        print("-".center(30, "-"))
