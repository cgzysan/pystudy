# by ysan

import sys
import os

# print(sys.path)

# cmd_res = os.system("dir") #执行命令，不保存结果

cmd_res = os.popen("dir").read()
os.makedirs("yyy")
os.name

print(cmd_res)
