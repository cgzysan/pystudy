# by ysan
#!/usr/bin/env python3
import os, sys

'''
    将项目的路径放到系统变量中，使可以导入同级目录文件，调用其方法
'''
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core import main


if __name__ == '__main__':      # 使下面内的代码只能在文件作为脚本的时候执行，而import到其他脚本是不会执行的
    main.run()
