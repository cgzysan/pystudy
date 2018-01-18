#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/16 10:54
  * @author: by Ysan
'''


import socketserver
import json
import os
import re
from core import db_handler
from conf import settings


class FTPTCPHandler(socketserver.BaseRequestHandler):

    def sign_in(self, *args):
        db_path = db_handler.db_handler(settings.DATA_BASE)
        cmd_dic = args[0]
        file_path = "%s/%s" % (db_path, cmd_dic['account_name'])
        if os.path.isfile(file_path):
            print("account name already exists")
            self.request.send(b'2201')
        else:
            del cmd_dic['action']
            cmd_dic['size'] = 66 * 1024 * 1024
            with open(file_path, 'w') as f:
                d_data = json.dumps(cmd_dic)
                f.write(d_data)
            self.request.send(d_data.encode('utf-8'))
            self.account_data = cmd_dic
            self.home_dir = "%s/home/%s" % (settings.BASE_DIR, cmd_dic['account_name'])
            self.current_dir = self.home_dir
            os.makedirs(self.current_dir)

    def login(self, *args):
        cmd_dic = args[0]
        db_path = db_handler.db_handler(settings.DATA_BASE)
        file_path = "%s/%s" % (db_path, cmd_dic['account_name'])
        if os.path.isfile(file_path):
            print("account exists")
            with open(file_path, 'r') as f:
                l_data = json.load(f)
                if cmd_dic['account_pwd'] == l_data['account_pwd']:
                    print("login success")
                    self.request.send(json.dumps(l_data).encode('utf-8'))
                    self.account_data = cmd_dic
                    self.home_dir = "%s/home/%s" % (settings.BASE_DIR, cmd_dic['account_name'])
                    self.current_dir = self.home_dir
                else:
                    print("name pwd err")
                    self.request.send(b'2202')
        else:
            print("account hasn't registered")
            self.request.send(b'2204')

    def put(self, *args):
        '''接收客户端文件'''
        current_relative_dir = self.__get_relative_path(self.current_dir).strip()
        dirs = current_relative_dir.split("/")
        if len(dirs) > 2 and dirs[2] == self.account_data['account_name']:
            self.request.send(b'2203')
            cmd_dic = args[0]
            file_name = cmd_dic['filename']
            file_size = cmd_dic['size']
            if os.path.isfile(file_name):
                file = file_name.split('.')
                f = open("%s/%s_new.%s" % (self.current_dir, file[0], file[1]), 'wb')
            else:
                f = open("%s/%s" % (self.current_dir, file_name), 'wb')
            received_size = 0
            while received_size < file_size:
                data = self.request.recv(1024)
                f.write(data)
                received_size += len(data)
            else:
                f.close()
                print("file [%s] has uploaded..." % file_name)
        else:
            self.request.send(b'2206')

    def get(self, *args):
        '''发送服务端的文件'''
        current_relative_dir = self.__get_relative_path(self.current_dir).strip()
        dirs = current_relative_dir.split("/")
        if len(dirs) > 2 and dirs[2] == self.account_data['account_name']:
            cmd_dic = args[0]
            file_name = "%s/%s" % (self.current_dir, cmd_dic['filename'])
            if os.path.isfile(file_name):
                self.request.send(str(os.stat(file_name).st_size).encode('utf-8'))
                client_response = self.request.recv(1024).decode()
                if client_response == '2203':
                    with open(file_name, 'rb') as f:
                        for line in f:
                            self.request.send(line)
                else:
                    print("response err!")
            else:
                print("This file [%s] is not exist!" % file_name)
                self.request.send(b'2205')
        else:
            self.request.send(b'2206')

    def __get_relative_path(self, abs_path):
        """return relative path of this user"""
        base_dir = re.escape(settings.BASE_DIR)
        relative_path = re.sub("^%s" % base_dir, "", abs_path)
        print(("relative path", relative_path, abs_path))
        return relative_path

    def pwd(self, *args):
        current_relative_dir = self.__get_relative_path(self.current_dir)
        self.request.send(current_relative_dir.encode('utf-8'))

    def ls(self, *args):
        cmd_dict = args[0]
        cmd_split = cmd_dict['action'].split()
        lenth = len(cmd_split)
        if lenth == 3:
            cmd = "%s %s %s" % (cmd_split[0], cmd_split[1], "%s/%s" % (self.current_dir, cmd_split[2]))
        elif lenth == 2:
            if cmd_split[1].startswith("-"):
                cmd = cmd_dict['action']
            else:
                cmd = "%s %s" % (cmd_split[0], "%s/%s" % (self.current_dir, cmd_split[1]))
        elif lenth == 1:
            cmd = "%s %s" % (cmd_split[0], self.current_dir)
        file_list = os.popen(cmd).read().encode("utf-8")
        print(type(file_list))
        self.request.send(str(len(file_list)).encode("utf-8"))
        client_response = self.request.recv(1024).decode()
        if client_response == '2203':
            self.request.sendall(file_list)

    def cd(self, *args):
        cmd_dict = args[0]
        path = cmd_dict['path']
        if path == '..':
            current_relative_dir = self.__get_relative_path(self.current_dir)
            dirs = current_relative_dir.split("/")
            if len(dirs) <= 2:
                self.request.send(b'2207')
            else:
                self.current_dir = re.sub("/%s" % dirs[-1], "", self.current_dir)
                self.request.send(self.__get_relative_path(self.current_dir).encode("utf-8"))
        else:
            self.current_dir = "%s/%s" % (self.current_dir, path)
            self.request.send(self.__get_relative_path(self.current_dir).encode("utf-8"))

    def mkdir(self, *args):
        cmd_dict = args[0]
        file_list = os.popen("ls %s" % self.current_dir).read().strip().split("\n")
        print(len(file_list))
        current_relative_dir = self.__get_relative_path(self.current_dir).strip()
        dirs = current_relative_dir.split("/")
        print("dirs ", len(dirs))
        if len(dirs) > 2 and dirs[2] == self.account_data['account_name']:
            if cmd_dict['dir'] in file_list:
                self.request.send(b'2208')
            else:
                os.mkdir("%s/%s" % (self.current_dir, cmd_dict['dir']))
                self.request.send(b'2000')
        else:
            self.request.send(b'2206')

    def handle(self):
        while True:
            try:
                print("开始接收客户端数据")
                self.data = self.request.recv(1024)
                print("{} wrote ".format(self.client_address[0]))
                print(self.data)
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic['action']
                if hasattr(self, action):
                    func = getattr(self, action)
                    func(cmd_dic)
            except ConnectionResetError as e:
                print("err", e)
                self.account_data = None
                self.home_dir = None
                self.current_dir = None
                break
            except json.decoder.JSONDecodeError as e:
                print("param err", e)
                self.account_data = None
                self.home_dir = None
                self.current_dir = None
                break
