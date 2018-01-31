#!/usr/bin/env python3
'''
  * @time: Created on 28/01/2018 1:45 PM
  * @author: by Ysan
'''

from sqlalchemy import Table, Column, Enum, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType

Base = declarative_base()


class Host(Base):
    __tablename__ = 'host'
    id = Column()


class HostGroup(Base):
    __tablename__ = 'host_group'


class RemoteUser(Base):
    __tablename__ = 'remote_user'

