#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/08 15:51
  * @author: by Ysan
'''

import pickle


class Db(object):
    '''定义数据库'''
    def __init__(self, conn_params):
        '''
        连接库
        :param conn_params: 连接参数
        '''
        self.conn_params = conn_params
        self.db_path = None

    def db_handler(self):
        '''
        :return:
        '''
        if self.conn_params['engine'] == 'file_storage':
            self.db_path = '%s/%s' % (self.conn_params['path'], self.conn_params['name'])
        elif self.conn_params['engine'] == 'mysql':
            self.db_path = None
        return self.db_path

    @staticmethod
    def load_pickle_data(file):
        '''
        读取文件数据到内存
        :param file: 文件路径
        :return:    文件数据
        '''
        with open(file, 'rb') as f:
            data = pickle.load(f)
            return data

    @staticmethod
    def dump_pickle_data(file, data):
        '''
        将内存中的数据写入文件中
        :param file:    文件路径
        :param data:    需要写入的数据
        :return:
        '''
        with open(file, 'wb') as f:
            pickle.dump(data, f)
