#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/23 09:46
  * @author: by Ysan

    ORM
    http://www.cnblogs.com/alex3714/articles/5978329.html
    优点：隐藏了数据访问细节，“封闭”的通用数据库交互，ORM的核心。他使得我们的通用数据库交互变得简单易行，并且完全不用考虑该死的SQL语句。
    缺点：代价是牺牲性能

    SQLAlchemy是Python编程语言下的一款ORM框架，该框架建立在数据库API之上，使用关系对象映射进行数据库操作，
    简言之便是：将对象转换成SQL，然后使用数据API执行SQL并获取执行结果。简化了SQL的操作
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()   # 生成一个SqlORM基类

engine = create_engine("mysql+pymysql://root:cgzysan@localhost:3306/studb", encoding='utf-8', echo=False)


class Host(Base):
    __tablename__ = 'hosts' # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    ip_addr = Column(String(128), unique=True, nullable=False)
    port = Column(Integer, default=21)

    def __repr__(self):
        return "<Host(hostname='%s',  ip_addr='%s', port='%s')>" % (
            self.hostname, self.ip_addr, self.port)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(32), nullable=False)
    host_id = Column(Integer, ForeignKey('hosts.id'))

    host = relationship("Host", backref="addresses")    # 允许你在user表里通过backref字段反向查出所有它在addresses表里的关联项

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


def session_insert():
    SessionCls = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    session = SessionCls()  # 生成session实例
    h1 = Host(hostname='Dn', ip_addr='192.168.2.213', port=15100)
    h2 = Host(hostname='En', ip_addr='192.168.2.212', port=16200)
    h3 = Host(hostname='Fn', ip_addr='192.168.2.215', port=17399)
    session.add(h1)
    session.add_all([h2, h3])
    h3.hostname = 'yyy'
    # session.rollback()  # 回滚当前的操作，会使当前的操作取消
    session.commit()


def session_delete():
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()
    res = session.query(Host).filter(Host.hostname.in_(['An', 'ysan'])).all()
    for r in res:
        session.delete(r)
    session.commit()


def session_update():
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()
    session.query(Host).filter(Host.id > 4).update({"port": 11111})
    session.commit()


def session_query():
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()
    res = session.query(Host).filter(Host.hostname.in_(['ubuntu', 'windows'])).all()
    for r in res:
        print("查询数据库", r.ip_addr)


Base.metadata.create_all(engine)    # 创建所有表结构

if __name__ == '__main__':
    #session_insert()
    #session_query()
    #session_delete()
    #session_update()
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()
    objs = session.query(Host).all()
    for obj in objs:
        print(obj)
        for i in obj.addresses:  # 通过user对象反查关联的addresses记录
            print(i)
        else:
            print('------------------------------------------------')
