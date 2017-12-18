# by ysan

'''
    面向过程编程和面向函数编程，
    面向过程其实就是没有返回值的函数而已，
    在 python 中则不同，过程返回的是 None
'''

def fun_1():
    i = 1 + 2
    # print(i)
    return i

def fun_2(str):
    f = eval(str)
    print(str)
    return f

# res = fun_1()
# print(res)

res = fun_2('''{
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }''')
print(res)
print(res["bakend"])