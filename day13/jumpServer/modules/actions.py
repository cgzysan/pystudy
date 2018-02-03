#!/usr/bin/env python3
'''
  * @time: Created on 2018/02/02 17:08
  * @author: by Ysan
'''
from conf import settings
from conf import action_registers
from modules import utils


def help_msg():
    '''
    print help messages
    :return:
    '''
    print("\033[31;1mAvailable commands:\033[0m")
    for key in action_registers.actions:
        print("\t", key)


def excute_from_command_line(args):
    if len(args) < 2:
        help_msg()
        exit()
    if args[1] not in action_registers.actions:
        utils.print_err("Command [%s] does not exist!" % args[1], quit=True)
    action_registers.actions[args[1]](args[1:])
