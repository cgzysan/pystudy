#!/usr/bin/env python3
# by ysan

import time, datetime

print("---------- time module ----------")
# 时间戳
print(time.time())
# 当地时间元组
print(time.localtime())
# 转化成UTC时间元组
print(time.gmtime(time.time()))
# 时间元组变成时间戳
print(time.mktime(time.localtime()))
# 讲时间元组格式化
x = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(x)
# 格式化时间转成时间元组
print(time.strptime(x, "%Y-%m-%d %H:%M:%S"))
# 把时间元组按照一个格式转换
print(time.asctime())
# 把时间戳按照一个格式转换
print(time.ctime())

print("---------- datetime module ----------")
# 以一定格式输出当前时间
print(datetime.datetime.now())
# 获取最近几天的时间，需要和datetime.datetime.new()一起调用
print(datetime.datetime.now() + datetime.timedelta(3))      # 三天后的时间
print(datetime.datetime.now() + datetime.timedelta(-3))     # 三天前的时间
print(datetime.datetime.now() + datetime.timedelta(hours=-3))       # 三小时前的时间
# 自行替换修改时间
c_time = datetime.datetime.now()
print(c_time.replace(year=2018, month=2, day=15, hour=16, minute=29, second=49))
