# by ysan

import sys

print(sys.getdefaultencoding())

'''在 python2 中， 编码解码的过程
        decode             encode
    str --------> unicode --------> str
    
    而 python3 中，
           decode                 encode
    bytes --------> str(unicode) --------> bytes    
'''


str = u"你好"

str_gbk = str.encode("gbk")
str_utf8 = str.encode("utf-8")
str_default = str.encode()
print(str_gbk)
print(str_utf8)
print(str_default)


b'\xc4\xe3\xba\xc3'
b'\xe4\xbd\xa0\xe5\xa5\xbd'
b'\xe4\xbd\xa0\xe5\xa5\xbd'


gbk_to_uft8 = str_gbk.decode('gbk').encode('utf-8')
print(gbk_to_uft8)