#!/usr/bin/env python3
'''
  * @time: Created on 2018/02/03 10:29
  * @author: by Ysan
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from conf import settings

engine = create_engine("mysql+pymysql://root:cgzysan@localhost:3306/jumpdb", encoding='utf-8', echo=False)

SessionCls = sessionmaker(bind=engine)
session = SessionCls()
