#!/usr/bin/env python3
'''
  * @time: Created on 2018/02/05 12:54
  * @author: by Ysan
'''

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("GET")
        u = self.get_argument('user')
        e = self.get_argument('email')
        print(u)
        print(e)
        self.write("GET")

    def post(self, *args, **kwargs):
        print("POST")
        p = self.get_argument('password', None)
        print(p)
        self.write("POST")


application = tornado.web.Application([
    (r"/index", MainHandler),
])
if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
