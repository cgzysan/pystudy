#!/usr/bin/env python3
# by ysan

'''
    time 模块 >>> http://www.runoob.com/python/att-time-strptime.html
'''

import time, json

with open('1234.json', 'r') as f_read:
    info = f_read.read()
    print(info, type(info))
    info_json = json.loads(info)
    print(info_json, type(info_json))

exp_time_stamp = info_json['expire_date']
exp_time_strp = time.strptime(exp_time_stamp, "%Y-%m-%d")   # 根据指定的格式把一个时间字符串解析为时间元组
exp_time_mk = time.mktime(exp_time_strp)    # 参数 >> 结构化的时间或者完整的9位元组元素  返回 >> 返回用秒数来表示时间的浮点数

cur_time = time.time()

print("exp-time".center(50, "-"))

print(exp_time_stamp)
print(exp_time_strp)
print(exp_time_mk)

print("cur_time".center(50, "-"))
print(cur_time)
