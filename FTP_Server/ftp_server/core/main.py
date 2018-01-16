#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/15 19:24
  * @author: by Ysan
'''

import socketserver
from lib.ftp_tcphandler import FTPTCPHandler


def run():
    '''
    The program run func
    :return:
    '''
    print("FTP 服务端运行")
    HOST, PORT = "localhost", 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), FTPTCPHandler)
    server.serve_forever()
