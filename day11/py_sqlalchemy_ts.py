#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/23 15:04
  * @author: by Ysan

    设计一个能描述“图书”与“作者”的关系的表结构
    需求：
    1. 一本书可以有好几个作者一起出版
    2. 一个作者可以写好几本书
    通过中间表方便实现
'''

from sqlalchemy import Table, Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("mysql+pymysql://root:cgzysan@localhost:3306/studb?charset=utf8", encoding='utf-8', echo=False)

book_m2m_author = Table(
    'book_m2m_author', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('author_id', Integer, ForeignKey('authors.id')),
)


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author', secondary=book_m2m_author, backref='books')

    def __repr__(self):
        return self.name


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name


def initialize():
    b1 = Book(name='跟An学C++')
    b2 = Book(name='跟An学java')
    b3 = Book(name='跟An学python')
    b4 = Book(name='跟Dn学Linux')
    b5 = Book(name='跟Dn学C#')
    b6 = Book(name='跟Kn学go')

    a1 = Author(name='An')
    a2 = Author(name='Dn')
    a3 = Author(name='Kn')

    b1.authors = [a1, a2]
    b2.authors = [a1, a3]
    b3.authors = [a2, a3]
    b4.authors = [a1, a2, a3]
    b5.authors = [a1, a2]
    b6.authors = [a2, a3]

    session.add_all([b1, b2, b3, b4, b5, b6, a1, a2, a3])

    session.commit()


def query():
    print('--------通过书表查关联的作者---------')

    book_obj = session.query(Book).filter_by(name="跟Dn学Linux").first()
    print(book_obj.name, book_obj.authors)

    print('--------通过作者表查关联的书---------')
    author_obj = session.query(Author).filter_by(name="Dn").first()
    print(author_obj.name, author_obj.books)
    session.commit()


sessionCls = sessionmaker(bind=engine)
session = sessionCls()
Base.metadata.create_all(engine)    # 创建所有表结构

if __name__ == '__main__':
    # initialize()
    query()
