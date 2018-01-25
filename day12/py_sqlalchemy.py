#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/25 10:09
  * @author: by Ysan

    工作数据导入数据库中
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("mysql+pymysql://root:cgzysan@localhost:3306/studb", encoding='utf-8', echo=False)
base_dir = "E:/beevideos/动漫"
file_path = "%s/%s" % (base_dir, "dongman")


class Cartoon(Base):
    __tablename__ = "cartoons"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    duration = Column(String())
    episodeTotal = Column(Integer)
    id = Column(Integer, unique=True, nullable=False)
    introduction = Column(String())
    link_data = Column(String())
    name = Column(String())
    pay = Column(Integer)
    pic = Column(String())
    region = Column(String())
    tag = Column(String())

    def __repr__(self):
        return "%s >> %s" % (self.id, self.name)


def session_insert():
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()


Base.metadata.create_all(engine)    # 创建所有表结构