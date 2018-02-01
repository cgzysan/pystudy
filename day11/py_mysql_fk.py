#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/31 09:18
  * @author: by Ysan

    外键关联：
    ForeignKey      其含义为，其所在的列的值域应当被限制在另一个表的指定列的取值范围之类。
    relationship
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("mysql+pymysql://root:cgzysan@localhost:3306/studb", encoding="utf-8", echo=False)
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    # ForeignKey表示 Customer.billing_address_id 列的值应该等于 address.id列中的值
    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(2))
    state = Column(String(64))


def create_table():
    Base.metadata.create_all(engine)


def insert_table():
    c = input("input data>>>").strip()
    print(c, len(c))
    sessionCls = sessionmaker(bind=engine)
    session = sessionCls()
    address_obj = Address(street="A", city=c, state="Y")
    session.add(address_obj)
    session.commit()

insert_table()
