#!/usr/bin/env python3
'''
  * @time: Created on 2018/04/02 14:16
  * @author: by Ysan
'''

import xlwt
import xlrd

# workbook = xlwt.Workbook(encoding="utf-8")
# worksheet = workbook.add_sheet("sheet1")
# worksheet.write(2, 0, label="This is test")
# worksheet.write(0, 0, label="这是原点")
# workbook.save("Excel_test.xls")

excel_path = "C:\\Users\\Administrator\\Desktop\\new xiaoman()\\格林数据(源)\\格林数据\\视频源.xls"

data = xlrd.open_workbook(excel_path)
sheet = data.sheet_by_index(1)
values = sheet.row_values(0)
print(values)
print(len(values))
print(values[4])
ddd = ['2', '34', '56', '42', '45']
print(ddd)
ddd[3] = 'yy'
print(ddd)
bbb = ""
aaa = "给我一首歌的时间"
print(aaa[2:4])
if aaa.index("一首歌") is not -1:
    print("一首歌" in aaa)
    print(aaa.index("一首歌"))


