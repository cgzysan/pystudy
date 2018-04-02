#!/usr/bin/env python3
'''
  * @time: Created on 2018/03/31 13:56
  * @author: by Ysan
'''


def print_msg():
    msg = "end of march"

    def printer():
        print(msg)
    # printer()
    return printer

a = print_msg()
a()
