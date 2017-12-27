#!/usr/bin/env python3
# by ysan

import os
'''
    用于提供系统级别的操作
    切换目录填写路径的时候需要写'\'进行对分隔符'\'的转义，也可以用r”强制python不转义
'''

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
os.rename('oldname', 'newname')
# 获取文件/目录信息
os.stat('path/filename')
# 输出操作系统特定的路径分隔符，win下为"\\", Linux下为"/"
os.sep
# 输出当前平台使用的行终止符，win下为"\r\n", Linux下为"/n"
os.linesep
# 输出用于分割文件路径的字符串
os.pathsep
# 输出字符串指示当前使用平台 win下为"nt", Linux下为"posix"
os.name
# 运行shell命令，直接显示
os.system("bash command")
# 获取系统环境变量
os.environ
# 返回path规范化的绝对路径
os.path.abspath('path')
# 讲path分割成目录和文件名二元组返回
os.path.split('path')
# 返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.dirname('path')
# 返回path最后的文件名，如果以/或\结尾，那么会返回空值
os.path.basename('path')
# 如果path存在，返回True，如果path不存在，返回False
os.path.exists('path')
# 如果path是绝对路径，返回True
os.path.isabs('path')
# 如果path是一个存在的文件，返回True，否则返回False
os.path.isfile('path')
# 如果path是一个存在的文件夹，返回True，否则返回False
os.path.isdir('path')
# 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.join('path1[, path2[, ...]]')
# 返回path所指向的文件或者目录的最后存取时间
os.path.getatime('path')
# 返回path所指向的文件或者目录的最后修改时间
os.path.getmtime('path')
