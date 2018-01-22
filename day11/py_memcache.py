#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/22 15:25
  * @author: by Ysan

'''

import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=True)
mc.set('foo', 'bar')

ret = mc.get('foo')
print(ret)
