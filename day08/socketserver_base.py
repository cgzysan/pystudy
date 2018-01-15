#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/15 16:27
  * @author: by Ysan

  socketserver 基础用法
'''

import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    '''
    The request handler class for our server

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the client
    '''

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("err", e)
                break


if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999

    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()  # 一直处理请求
