#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/16 10:16
  * @author: by Ysan
'''

from lib.ftp_client import FtpClient


def welcome():
    ftp_client = FtpClient()
    ftp_client.connect("localhost", 9999)
    ftp_client.interactive()


def interactive(menu, menu_dict):
    print(menu)
    user_option = input(">>>").strip()
    if user_option in menu_dict:
        eval(menu_dict[user_option])
    else:
        print("\033[31;1mOption does not exist!\033[0m")


def run():
    '''
    FTP client program run func
    :return:
    '''
    print("FTP客户端")
    welcome()

