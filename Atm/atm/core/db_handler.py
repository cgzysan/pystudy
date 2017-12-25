#!/usr/bin/env python3
# by ysan


def file_db_handle(conn_params):
    '''
    parse the db file path
    :param conn_params: the db connection params set in settings
    :return:
    '''
    db_path = '%s/%s' % (conn_params['path'], conn_params['name'])
    return db_path


def mysql_db_handle(conn_params):
    pass


def db_handler(conn_params):
    '''
    connect to db
    :param conn_params: ths db connection params set in settings
    :return:
    '''

    if conn_params['engine'] == 'file_storage':
        return file_db_handle(conn_params)

    if conn_params['engine'] == 'mysql':
        return mysql_db_handle(conn_params)
