# by ysan

operator = ("insert", "delete", "update", "search")
heard = "backend"


# 判断是否是数字，不然提示重新输入
def numif(num_input):
    while not num_input.isdigit():
        num_input = input('\033[31m 输入%s不是数字，请重新输入！\033[0m' % num_input)
    number = num_input
    return number


#
def search(search_key):
    with open("haproxy.txt", 'r', encoding="utf-8") as rf:
        for index, line in enumerate(rf):
            if line.startswith(heard) and search_key in line:
                # print(rf.readline().strip())
                return rf.readline().strip()
        return 0


def insert(insert_str):
    with open("haproxy.txt", 'r+', encoding="utf-8") as af:
        for line in af:
            af.writelines(line)
            if line.startswith("backend"):
                af.writelines("hello world")



a = insert("www.oldboy.org")
# b = search("www.oldboy.org")
# print(b)


# for index, ope in enumerate(operator):
#     print(index, ope)
#
# chioce = input("选择操作>>>")
#     if chioce == "insert":
#         # 增

