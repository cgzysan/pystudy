#!/usr/bin/env python3
# by ysan

import sys
'''
    用于提供对解释器相关的操作
'''

# 命令行参数list, 第一个元素是程序本身路径
sys.argv
# 退出程序, 正常退出时exit(0)
sys.exit(0)
# 获取Python解释程序的版本信息
sys.version
# 最大的Int值   >>> 3.x 没有这个属性
sys.maxint
# 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.path
# 返回操作系统平台名称
sys.platform
# 屏幕输出
sys.stdout.write('hello world')
# 等待屏幕输入
val = sys.stdin.readline()[:1]
