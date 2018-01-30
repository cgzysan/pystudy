#!/usr/bin/env python3
'''
  * @time: Created on 21/01/2018 9:59 PM
  * @author: by Ysan

    安装mysql
    https://www.cnblogs.com/fnlingnzb-learner/p/6009153.html
    官方文档
    https://dev.mysql.com/doc/refman/5.7/en/data-directory-initialization-mysqld.html
    sp:初始化时：
    使用-initialize生成随机密码
    使用-initialize-insecure生成空密码

    python 对mysql的操作
    http://www.runoob.com/python3/python3-mysql.html

    sql 语句
    http://www.runoob.com/sql/sql-tutorial.html

    PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。
    PyMySQL 遵循 Python 数据库 API v2.0 规范，并包含了 pure-Python MySQL 客户端库。

    mysql 外键关联
    外键约束：mysql通过外键约束来保证表与表之间的数据的完整性和准确性
'''

import pymysql


def insert_mysql():
    '''
    mysql插入数据
    :return:
    '''
    conn = pymysql.connect(host='localhost', user='root', passwd='cgzysan', db='studb')

    cur = conn.cursor()

    # 插入数据
    n = input("name:").strip()
    s = input("sex:").strip()
    a = input("age:").strip()
    a = int(a)
    t = input("tel:").strip()
    reCount = cur.execute('insert into students(name, sex, age, tel) VALUES(%s, %s, %s, %s)', (n, s, a, t))
    conn.commit()

    cur.close()
    conn.close()
    print(reCount)


def delete_mysql():
    '''
    删除数据
    :return:
    '''
    conn = pymysql.connect(host='localhost', user='root', passwd='cgzysan', db='studb')
    cur = conn.cursor()
    # 删除表（people）中所有的数据
    reCount = cur.execute('delete from people')
    conn.commit()

    cur.close()
    conn.close()
    print(reCount)


def update_mysql():
    '''
    更新数据
    :return:
    '''
    conn = pymysql.connect(host='localhost', user='root', passwd='cgzysan', db='studb')
    cur = conn.cursor()
    reCount = cur.execute("update students set name = 'HAHA' WHERE sex = 'f'")
    conn.commit()

    cur.close()
    conn.close()
    print(reCount)


def query_mysql():
    '''
    查找数据
    :return:
    '''
    conn = pymysql.connect(host='localhost', user='root', passwd='cgzysan', db='studb')
    cur = conn.cursor()
    reCount = cur.execute('select * from students')

    # ------------------- fetchall() 获取所有数据 -------------------
    # mRet = cur.fetchall()
    #
    # cur.close()
    # conn.close()
    #
    # print(reCount)
    # print(mRet)

    # ------------------- 逐个取数据 -------------------
    print(cur.fetchone())
    print(cur.fetchone())

    cur.scroll(-1, mode='relative')
    print(cur.fetchone())
    print(cur.fetchone())

    cur.scroll(0, mode='absolute')
    print(cur.fetchone())
    print(cur.fetchone())

    cur.scroll(0, mode='absolute')
    print('-------------------- 循环输出 --------------------')
    for i in range(reCount):
        print(cur.fetchone())

    cur.close()
    conn.close()
    print(reCount)


if __name__ == '__main__':
    query_mysql()
