#!/usr/bin/env python3
# by ysan

import os

# 切换目录填写路径的时候需要写'\'进行对分隔符'\'的转义，也可以用r”强制python不转义

# 获取当前工作目录
print(os.getcwd())
# 改变当前脚本工作目录，相当于shell下cd
os.chdir("new_workspace")
# 返回当前目录    "."
os.curdir
# 获取当前目录的父目录字符串名    ".."
os.pardir
# 可生成多层递归目录
os.makedirs('dirname1/dirname2')
# 若目录为空，则删除，并递归上一级目录，如若也为空，则删除，以此类推
os.removedirs('dirname')
# 生成单级目录，相当于shell中mkdir dirname
os.mkdir('dirname')
# 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中的rmdir dirname
os.rmdir('dirname')
# 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.listdir('dirname')
# 删除一个文件
os.remove()
# 重命名文件/目录
# 获取文件/目录信息
# 输出操作系统特定的路径分隔符，win下为"\\", Linux下为"/"
#