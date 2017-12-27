#!/usr/bin/env python3
# by ysan

import pickle


def test(name):
    print("this is from %s" % name)


data = {
    'name': 'ysan',
    'age': 25,
    'func': test,
}

'''
    dumps, dump,                        loads, load
    将序列，字典转成 字节或者字符串       将字节或者字符串转成字典，序列
'''
print("------------- 通过 dumps, loads 进行操作 -------------")

with open('pickle_test', 'wb') as f_write:
    f_write.write(pickle.dumps(data))

with open('pickle_test', 'rb') as f_read:
    info = f_read.read()
    str_data = pickle.loads(info)
    print(info)
    print(str_data)
    str_data['func']('ysan')

print("------------- 通过 dump, load 进行操作 -------------")

with open('pickle_test', 'wb') as f_write:
    pickle.dump(data, f_write)

with open('pickle_test', 'rb') as f_read:
    str_data = pickle.load(f_read)
    print(str_data)
    str_data['func']('cgzysan')
