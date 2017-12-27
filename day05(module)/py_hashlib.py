#!/usr/bin/env python3
# by ysan

import hashlib

'''
    用于加密相关的操作，3.x里代理md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512, MD5算法
'''

m = hashlib.md5()
m.update(b"Hello")
# 16进制格式hash
print(m.hexdigest())
# 2进制格式hash
print(m.digest())
m.update(b"It's me")
print(m.hexdigest())

print("---------- md5 ----------")
m = hashlib.md5()
m.update('admin'.encode("utf-8"))
print(m.hexdigest())

print("---------- sha1 ----------")
m = hashlib.sha1()
m.update('admin'.encode("utf-8"))
print(m.hexdigest())

print("---------- sha256 ----------")
m = hashlib.sha256()
m.update('admin'.encode("utf-8"))
print(m.hexdigest())

print("---------- sha384 ----------")
m = hashlib.sha384()
m.update('admin'.encode("utf-8"))
print(m.hexdigest())

print("---------- sha512 ----------")
m = hashlib.sha512()
m.update('admin'.encode("utf-8"))
print(m.hexdigest())
