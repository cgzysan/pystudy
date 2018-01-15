#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/15 19:22
  * @author: by Ysan
'''

import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core import main

if __name__ == '__main__':
    main.run()
