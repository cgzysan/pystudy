#!/usr/bin/env python3
'''
  * @time: Created on 2018/03/21 13:50
  * @author: by Ysan
'''

import socket


client = socket.socket()
client.connect(("192.168.254.35", 2121))

while True:
    print("connect success!")
    
