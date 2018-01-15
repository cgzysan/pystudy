#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/15 09:00
  * @author: by Ysan
'''

import socket
import hashlib

client = socket.socket()
client.connect(('localhost', 8989))

while True:
    file_name = input(">>>:").strip()
    if len(file_name) == 0:
        continue
    client.send(file_name.encode('utf-8'))
    receive_size = client.recv(1024)
    client.send(b'ready complete')
    file_size = 0
    recv_file = file_name.split("\\")[-1]
    print(recv_file)
    with open(recv_file, 'wb') as f:
        m = hashlib.md5()
        while file_size < int(receive_size.decode()):
            file_data = client.recv(1024)
            m.update(file_data)
            f.write(file_data)
            file_size += len(file_data)
        client.send(b'complete')
        checkout_md5 = client.recv(1024).decode()
        print("checkout_md5: ", checkout_md5)
        print("file_md5: ", m.hexdigest())
        if m.hexdigest() == checkout_md5:
            print("file transmission successful")
