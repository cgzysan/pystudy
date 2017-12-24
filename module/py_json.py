#!/usr/bin/env python3
# by ysan

import json

info = {
    'name': 'ysan',
    'age': 26,
    'salary': 7000,
}

list_info = [11, 22, 33, 44, 55,]

# print(info, type(info))
# print(list_info, type(list_info))
print(info, type(info))

json_info = json.dumps(info)
print(json_info, type(json_info))

with open('json.txt', 'w') as f_write:
    f_write.write(json_info)

with open('json.txt', 'r') as f_read:
    file = f_read.read()
    file_json = json.loads(file)
    print(file, type(file))
    print(file_json, type(file_json))
