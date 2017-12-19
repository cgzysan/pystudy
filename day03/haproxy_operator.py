# by ysan

'''
    读取文件保存在字典和列表中：
    backend_all_info >>> 所有的 backend 信息 dict
    { backend : [ {server_info},{}...{} ]>>>server_list }
    backend_list >>> 所有的 backend 值 list
    backend_show_dict >>> 带编码的 backend dict
'''


# 判断是否是数字，不然提示重新输入
def numif(num_input):
    while not num_input.isdigit():
        num_input = input('\033[31m 输入%s不是数字，请重新输入！\033[0m' % num_input)
    number = num_input
    return number


# 查询显示并将文本生成程序需要的 dict 和 list
def show_list(file):
    backend_all_info = {}
    backend_info = {}
    backend_list = []
    server_list = []

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()

            if line.startswith('backend'):
                backend_name = line.split()[1]
                backend_list.append(backend_name)
                server_list = []     # 清空server_list里的记录，遇到新backend可以输入新的server_list

            elif line.startswith('server'):
                str = line.split();
                backend_info['name'] = str[1]
                backend_info['IP'] = str[2]
                backend_info['weight'] = str[4]
                backend_info['maxconn'] = str[6]
                server_list.append(backend_info.copy())  # 将backend中的信息加到server_list中,此处需要用copy, 使数据不会随着父类改变而被改变
                backend_all_info[backend_name] = server_list

    return backend_list, backend_all_info


# 展示 backend 列表内容，同时返回编号与列表内容对应的 dict
def backend_show(backend_list):
    backend_show_dict = {}
    print("-".center(70, "-"))
    print("Welcome to HAproxy configure platform".center(70, "-"))
    print("backend list information as follows".ljust(70, "-"))

    for k, v in enumerate(backend_list):
        print(k, v)
        backend_show_dict[str(k)] = v

    return backend_show_dict    # 返回 backend 和对应的编号


# 展示 server 列表内容
def server_show(backend_input, backend_all_info):
    server_show_dict = {}
    server_list = backend_all_info[backend_input]
    for k, v in enumerate(server_list, 1):      # enumerate(list, start=0) 代表下标从0开始，但仅仅就是下标改变，元素不变
        print(k, "name:", v['name'], "\tIP:", v['IP'], "\tweight:", v['weight'], "\tmaxconn:", v['maxconn'])
        server_show_dict[k] = v

    return server_show_dict  # 返回编号对应的 server 字典


# 展示操作列表和编号，并返回编号
def action_list():
    print("-".center(70, "-"))
    print("操作清单如下：")
    print('''
    1.查询backend和server信息
    2.添加backend和server信息
    3.修改backend和server信息
    4.删除backend和server信息
    5.退出
    ''')
    print("-".center(70, "-"))
    action_number = numif(input("请输入操作码：（请输入数字）"))
    return action_number


# 查询功能
def query(query_input):
    if query_input in backend_show_dict:
        backend_input = backend_show_dict[query_input]
        print(backend_input, " :")
        server_show(backend_input, backend_all_info)

    elif query_input in backend_show_dict.values():
        print(query_input, " :")
        server_show(query_input, backend_all_info)


# 添加功能
def insert(insert_input):
    if insert_input in backend_list:
        insert_dict = {}
        insert_dict['name'] = input("请输入需要增加的server名称：").strip()
        insert_dict['IP'] = input("请输入需要增加的IP地址：").strip()
        insert_dict['weight'] = input("请输入需要增加的weight值：").strip()
        insert_dict['maxconn'] = input("请输入需要增加的maxconn值：").strip()
        backend_name_key = backend_list[int(insert_input) - 1]

        for dict in backend_all_info[backend_name_key]:  # 实现IP已存在，更新weight信息和maxconn信息
            if insert_dict['IP'] in dict.values():
                dict['weight'] = insert_dict['weight']
                dict['maxconn'] = insert_dict['maxconn']

            else:   # IP不存在，就将server增加到backend下
                backend_all_info[backend_name_key].append(insert_dict)



# 定义文档备份与回写功能
def backup():
    file_new = "%s_new" % file

    with open(file, 'r') as f_read , open(file_new, 'w+') as f_write:
        for line in f_read:



# 退出功能
def backend_exit():
    flag_exit = True
    b_input = input("操作完毕退出请按'b'：")
    while flag_exit:
        if b_input == 'b':
            flag_exit = False
            return flag_exit

        else:
            return backend_exit()   # 使用尾递归优化，加上return帮助直接退出，而不需要递归一层层退出 >>> 待学习


# 主函数
file = 'haproxy'
backend_list, backend_all_info = show_list(file)
backend_show_dict = backend_show(backend_list)
action_num = action_list()

if action_num == '1':
    query(input("请输入需要查询的backend编号，或者名称"))
    backend_exit()

if action_num == '2':
    insert("请输入需要添加的现有backend编号或新backend名称：")

