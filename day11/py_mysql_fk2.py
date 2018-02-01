#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/31 17:18
  * @author: by Ysan
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:cgzysan@localhost:3306/studb", encoding='utf-8', echo=False)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    fullname = Column(String(64))
    password = Column(String(128))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(64), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="addresses", order_by=id)

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


def create_table():
    Base.metadata.create_all(engine)    # 创建表结构


def insert_table():
    Session_cls = sessionmaker(bind=engine)
    Session = Session_cls()

    user_obj = User(name="AA", fullname="AA_II", password="123")
    # 添加关联对象
    user_obj.addresses = [Address(email_address="r1@163.com"),
                          Address(email_address="r2@163.com")]
    Session.add(user_obj)
    Session.commit()


def query_table():
    Session_cls = sessionmaker(bind=engine)
    Session = Session_cls()

    aa_user = Session.query(User).filter_by(name="AA").first()
    print(aa_user, aa_user.addresses)


query_table()
