#!/usr/bin/env python3
'''
  * @time: Created on 2018/02/03 09:21
  * @author: by Ysan
'''
from conf import settings
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def print_err(msg, quit=False):
    output = "\033[31;1mError: %s\033[0m" % msg
    if quit:
        exit(output)
    else:
        print(output)


def yaml_parser(yml_filename):
    '''
    load yaml file and return
    :param yml_filename: yaml file name
    :return:
    '''
    try:
        with open(yml_filename, 'r') as yaml_file:
            data = yaml.load(yaml_file)
            return data
    except Exception as e:
        print_err(e)
