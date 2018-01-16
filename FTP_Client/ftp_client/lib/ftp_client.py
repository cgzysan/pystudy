#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/16 10:33
  * @author: by Ysan
'''

import socket
import hashlib
import json
import os
import sys

user_data = {
    'is_authenticated': False,
    'account_data': None
}


class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    def connect(self, ip, port):
        self.client.connect((ip, port))

    def help(self):
        msg = '''
        help    help
        get     get remote_filename
        put     put local_filename
        exit    exit the system
        ls      list all the files in current directory
        cd      cd some_dir
        del     del remote_filename
        '''
        print(msg)

    def show_progress(self, total, finished, percent):
        '''
        显示进度条
        :param total:       文件总大小
        :param finished:    当前已完成文件大小
        :param percent:     已完成占总大小百分比
        '''
        progress_mark = "=" * (percent/2)
        sys.stdout.write("[%s/%s]%s>%s\r" % (total, finished, progress_mark, percent))
        sys.stdout.flush()
        if percent == 100:
            print('\n')

    def authentication(self):
        print("登录")
        account_name = input("please input your account name>>:").strip()
        account_pwd = input("please input your account password>>:").strip()
        md5_pwd = hashlib.new("md5", account_pwd.encode('utf-8')).hexdigest()
        account_info = {
            "action": "login",
            "account_name": account_name,
            "account_pwd": md5_pwd,
        }
        self.client.send(json.dumps(account_info).encode("utf-8"))
        auth_res = self.client.recv(1024).decode()
        if auth_res == '2202':
            print("account name or password error!")
        elif auth_res == '2204':
            print("account hasn't registered!")
        else:
            print("登录成功")
            user_data['is_authenticated'] = True
            user_data['account_data'] = json.loads(auth_res)

    def account_sign_in(self):
        print("注册")
        account_name = input("please input your account name>>:").strip()
        account_pwd = input("please input your account password>>:").strip()
        md5_pwd = hashlib.new("md5", account_pwd.encode('utf-8')).hexdigest()
        account_info = {
            "action": "sign_in",
            "account_name": account_name,
            "account_pwd": md5_pwd,
        }
        self.client.send(json.dumps(account_info).encode("utf-8"))
        sign_res = self.client.recv(1024).decode()
        if sign_res == '2201':
            print("account had registered")
        else:
            print("注册成功")
            user_data['is_authenticated'] = True
            user_data['account_data'] = json.loads(sign_res)

    def interactive(self):
        menu = '''
        --------------------- Welcome to FTP system ---------------------
        1. \033[33;1m注册\033[0m
        2. \033[34;1m登录\033[0m
        '''
        menu_dict = {
            '1': 'account_sign_in',
            '2': 'authentication',
        }
        while True:
            if not user_data['is_authenticated']:
                print(menu)
                user_option = input(">>>").strip()
                if user_option in menu_dict:
                    func = getattr(self, menu_dict[user_option])
                    func()
                else:
                    print("\033[31;1mOption does not exist!\033[0m")
            else:
                cmd = input(">>>").strip()
                if len(cmd) == 0:
                    continue
                cmd_str = cmd.split()[0]
                if hasattr(self, "cmd_%s" % cmd_str):
                    func = getattr(self, "cmd_%s" % cmd_str)
                    func(cmd)
                else:
                    self.help()

    def cmd_put(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            file_name = cmd_split[1]
            if os.path.isfile(file_name):
                file_size = os.stat(file_name).st_size
                print("文件大小》》》", file_size)
                msg_dict = {
                    "action": "put",
                    "filename": file_name,
                    "size": file_size
                }
                self.client.send(json.dumps(msg_dict).encode("utf-8"))
                # 防止粘包，等待服务器确认
                server_response = self.client.recv(1024).decode()
                if server_response == "2203":
                    send_size = 0
                    progress_percent = 0
                    f = open(file_name, 'rb')
                    for line in f:
                        self.client.send(line)
                        send_size += len(line)

                        cur_percent = int(float(send_size) / file_size * 100)
                        if cur_percent > progress_percent:
                            progress_percent = cur_percent
                            # self.show_progress(file_size, send_size, progress_percent)
                    else:
                        print("file upload success!")
                        f.close()
            else:
                print(file_name, "is not exist")
        else:
            print("%s lack parameter!" % args[0])

    def cmd_get(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            file_name = cmd_split[1]
            msg_dict = {
                "action": "get",
                "filename": file_name,
            }
            self.client.send(json.dumps(msg_dict).encode("utf-8"))
            # 防止粘包，等待服务器确认
            server_response = self.client.recv(1024).decode()