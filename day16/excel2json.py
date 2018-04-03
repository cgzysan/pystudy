#!/usr/bin/env python3
'''
  * @time: Created on 2018/04/02 09:17
  * @author: by Ysan
'''

import xlrd
import xlwt
import json

excel_path = "C:\\Users\\Administrator\\Desktop\\new xiaoman()\\格林数据(源)\\格林数据\\视频源.xls"


def welcome():
    menu = """
    -----------选择操作----------
    1. \033[33;1m补全Excel表格\033[0m
    2. \033[33;1m转成Json文件\033[0m
    3. \033[33;1m退出\033[0m
    """
    menu_dict = {
        '1': 'completion_excel()',
        '2': 'excel2json()',
        '3': 'logout()',
    }
    interactive(menu, menu_dict)


def completion_excel():
    file_path = input("输入需要操作的Excel文件的绝对路径>>>")
    data = achieve_data(file_path)
    if data is not None:
        worksheets = data.sheet_names()
        print("包含的表单:")
        for index, sheet in enumerate(worksheets):
            print(index, sheet)
        choose = input("请输入表单对应的编号>>>")
        table = data.sheet_by_index(int(choose))

        # 创建Excel表
        workbook = xlwt.Workbook(encoding="utf-8")
        # 创建 sheet
        worksheet = workbook.add_sheet("sheet1")
        # 先写表头
        titles = table.row_values(0)
        for k, v in enumerate(titles):
            worksheet.write(0, k, v)
        for i in range(1, table.nrows):
            row = table.row_values(i)
            # 补全年级的表
            if row[4] == "":
                course = row[6]
                if "年级" in course:
                    n = course.index("年级")
                    row[4] = course[n-1:n+3]
                else:
                    row[4] = "初中"

            for x, y in enumerate(row):
                worksheet.write(i, x, y)
        workbook.save("Excel_test.xls")


def excel2json():
    file_path = input("输入需要转成Json的Excel文件的路径>>>")
    data = achieve_data(file_path)
    if data is not None:
        # 抓取所有sheet页的名称
        worksheets = data.sheet_names()
        print("包含的表单:")
        for index, sheet in enumerate(worksheets):
            print(index, sheet)
        choose = input("请输入表单对应的编号>>>")
        table = data.sheet_by_index(int(choose))
        # 获取到数据的表头
        titles = table.row_values(0)
        result = {}
        result["middle_school"] = []
        # 循环excel文件表的有效行数
        for i in range(1, table.nrows):
            row = table.row_values(i)
            tmp = {}
            for index, title in enumerate(titles):
                if title == "id":
                    tmp[title] = int(row[index])
                else:
                    tmp[title] = row[index]
            result["middle_school"].append(tmp)
        with open("middle_school.txt", 'w', encoding='utf-8') as f:
            json.dump(result, f)


def achieve_data(file_path):
    try:
        data = xlrd.open_workbook(file_path)
        return data
    except Exception as e:
        print("excel表格读取失败：%s" % file_path)
        return None


def logout():
    exit(" 谢谢使用 ".center(50, "#"))


def interactive(menu, menu_dict):
    '''
    user interactive func
    :param menu:
    :param menu_dict:
    :return:
    '''
    exit_flag = False
    while exit_flag != 'b':
        print(menu)
        user_option = input(">>>").strip()
        if user_option in menu_dict:
            exit_flag = eval(menu_dict[user_option])
        else:
            print("\033[31;1mOption does not exist!\033[0m")


if __name__ == '__main__':
    welcome()
