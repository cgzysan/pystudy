#!/usr/bin/env python3
'''
  * @time: Created on 28/01/2018 1:41 PM
  * @author: by Ysan
'''
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_CONN = "mysql+pymysql://root:cgzysan@localhost:3306/jumpdb?charset=utf8"

'''
# Database
DATABASES = {
    'default': {
        'ENGINE': 'mysqldb',
        'NAME': 'Jumpserver',
        'HOST': '',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': ''
    }
}
'''
