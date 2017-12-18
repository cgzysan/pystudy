#!/usr/bin/env python3
# by ysan

'''
   python (解释器) 内置方法
'''

# 取绝对值
abs()
# 列表所有为 True 返回 True
all()
# 列表只要有一个为 True 返回 True
any()
# 转字符串
ascii()
# 数字转 二进制
bin()
# 转成字符数组
bytearray()
# asic码 转 asic字符
chr()
# asci字符 转 asic码
ord()
# 查看 方法
dir()
# 除法运算 返回 (商，余数)
divmod()
#
exec()
#
eval()
# 过滤
filter()
filter(lambda n: n > 5, range(10)) # 从 range(10)中获取一个大于5的列表
# 对所有的值进行处理
map()
# 不可变集合列表
frozenset()
# 获取哈希值
hash()
# 转 十六进制
hex()
# 保留小数有效数字 默认0
round()
# 排序
sorted()
# eg:为一个dict(字典) a 排序
a = {4: 2, 5: 3, -4: 9, 8: 7}
sorted(a.items()) # 以key值为根据排序
sorted(a.items(), key = lambda x: x[1])
# 结合两个集合变成字典
zip()
