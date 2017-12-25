#!/usr/bin/env python3
# by ysan

import json

acc_dict = {
    'id': 1234,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2017-01-02',
    'expire_date': '2022-01-01',
    'pay_day': 22,
    'status': 0,  # 0 = normal, 1 = locked, 2 = disable
}

print(json.dumps(acc_dict))
