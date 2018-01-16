#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/16 13:37
  * @author: by Ysan
'''


def file_db_handle(conn_params):
    db_path = "%s/%s" % (conn_params['path'], conn_params['name'])
    return db_path


def mysql_db_handle(conn_params):
    pass


def db_handler(conn_params):
    if conn_params['engine'] == 'file_storage':
        return file_db_handle(conn_params)
    if conn_params['engine'] == 'mysql':
        return mysql_db_handle(conn_params)
