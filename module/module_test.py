#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/18 08:55
  * @author: by Ysan
'''

import re
import os

# data = input(">>>:").strip()
a = "E:\Ysan\python\pystudy\FTP_Server\ftp_server"
b = "E:\Ysan\python\pystudy\FTP_Server\ftp_server/home/ysan"
aa = re.escape("E:\Ysan\python\pystudy\FTP_Server\ftp_server")
bb = re.escape("E:\Ysan\python\pystudy\FTP_Server\ftp_server/home/ysan")
print(a)
print(b)
new = re.sub("^%s" % aa, "", "E:\Ysan\python\pystudy\FTP_Server\ftp_server/home/ysan")
print(new)

print("--------------------------------------------------------")
print(b.endswith("ysan"))
print(len(new.split(os.path.sep)))
print(new.split("/")[0])
print(new.split("/")[1])
print(new.split("/")[2])

print(len("ls -l core".split()))

new2 = re.sub("/ysan$", "", new)
print(new2)

print(os.path.sep, type(os.path.sep))