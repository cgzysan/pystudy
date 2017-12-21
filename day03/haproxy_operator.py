# by ysan
#!/usr/bin/env python

import sys, os

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
                str = line.split()
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


'''
    展示 server 列表内容    
    backend_input >>> backend 的名称
    backend_all_info >>> 所有的backend信息
'''
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
    while True:
        if query_input in backend_show_dict:
            backend_input = backend_show_dict[query_input]
            print(backend_input, " :")
            server_show(backend_input, backend_all_info)
            break

        elif query_input in backend_show_dict.values():
            print(query_input, " :")
            server_show(query_input, backend_all_info)
            break

        else:   # 校验异常输入
            query_input = input("输入错误，请重新输入：")


# 添加功能
def insert(insert_input):
    while True:
        if insert_input in backend_show_dict:   # 添加原有backend下的server
            insert_dict = {}
            insert_dict['name'] = input("请输入需要增加的server名称：").strip()
            insert_dict['IP'] = input("请输入需要增加的IP地址：").strip()
            insert_dict['weight'] = input("请输入需要增加的weight值：").strip()
            insert_dict['maxconn'] = input("请输入需要增加的maxconn值：").strip()
            backend_name_key = backend_list[int(insert_input)]

            for dict in backend_all_info[backend_name_key]:  # 实现IP已存在，更新weight信息和maxconn信息
                if insert_dict['IP'] in dict.values():
                    dict['weight'] = insert_dict['weight']
                    dict['maxconn'] = insert_dict['maxconn']
                    break

                else:   # IP不存在，就将server增加到backend下
                    backend_all_info[backend_name_key].append(insert_dict)

            backup(file, backend_name_key, backend_all_info)
            print('''name：%{name} IP：{IP} weight：{weight} maxconn：{maxconn}已添加成功'''.format(**insert_dict))  # 提示添加成功
            break

        else:   # 添加新backend下的server
            insert_dict = {}
            insert_dict['name'] = input("请输入%s下新增server名称：" % insert_input)
            insert_dict['IP'] = input("请输入%s下新增IP地址：" % insert_input)
            insert_dict['weight'] = input("请输入%s下新增weight值：" % insert_input)
            insert_dict['maxconn'] = input("请输入%s下新增maxcoon值：" % insert_input)
            backend_name_key = insert_input
            backend_all_info[backend_name_key] = insert_dict    # 将新增backend和对应server存到字典中

            file_new = "$s_new" % file
            with open(file, 'r') as f_read, open(file_new, 'a+') as f_append:
                for line in f_read:
                    f_append.write(line)
                f_append.write("\nbackend %s\n" % backend_name_key)   # 追加backend信息
                server_line_write = "\t\tserver {name} {IP} weight {weight} maxconn {maxconn}\n"    # 追加server信息
                f_append.write(server_line_write.format(**insert_dict))

            os.system('mv %s %s_backup' % (file, file))     # 将file文件名改为file_backup
            os.system('mv %s %s' % (file_new, file))        # 将file_new文件名改为file，实现备份
            print("\nbackend %s" % backend_name_key)
            print('''name：{name} IP：{IP} weight：{weight} maxconn：{maxconn}已添加成功'''.format(**insert_dict))   # 提示添加成功
            break


# 修改功能
def update(update_input):
    update_dict = {}
    if update_input in backend_show_dict:   # 判断输入是否存在
        backend_name = backend_show_dict[update_input]    # 通过编号获取backend
        backend_name_confirm = input("是否需要修改该backend名称：%s；确认请按'y'，按任意键继续：" % backend_name)

        if backend_name_confirm == 'y':
            backend_new_name = input("请输入修改后的backend名：")    # 修改后新的backend名
            backend_all_info[backend_new_name] = backend_all_info.pop(backend_name)
            server_info_confirm = input("是否需要继续修改%s下的server：确认请按'y'，按任意键继续：" % backend_new_name)

            if server_info_confirm == 'y':
                server_update_show = server_show(backend_new_name, backend_all_info)
                server_update_num = numif(input("请输入需要修改的server编号："))
                update_dict['name'] = input("请输入修改后的name：")
                update_dict['IP'] = input("请输入修改后的IP：")
                update_dict['weight'] = input("请输入修改后的weight：")
                update_dict['maxconn'] = input("请输入修改后的maxconn：")
                server_update_show[int(server_update_num)] = update_dict
                server_update_dict_backup = {}
                server_update_dict_backup[backend_new_name] = server_update_show.values()
                backup(file, backend_name, server_update_dict_backup, backend_new_name)

            else:   # 不修改server，只修改了backend名称
                backup(file, backend_name, backend_all_info, backend_new_name)
        else:   # 未修改backend名情况时修改server信息
            server_update_show = server_show(backend_name, backend_all_info)
            server_update_num = numif(input("请输入需要修改的server编号："))
            update_dict['name'] = input("请输入修改后的name：")
            update_dict['IP'] = input("请输入修改后的IP：")
            update_dict['weight'] = input("请输入修改后的weight：")
            update_dict['maxconn'] = input("请输入修改后的maxconn：")
            server_update_show[int(server_update_num)] = update_dict
            server_update_dict_backup = {}
            server_update_dict_backup[backend_name] = server_update_show.values()
            backup(file, backend_name, server_update_dict_backup)   # 调用backup函数，操作文件

    else:
        update_input_return = input("需修改backend不存在，请重新输入：")
        update(update_input_return)


# 删除功能
def delete(delete_input):
    if delete_input in backend_show_dict:
        backend_delete = backend_show_dict[delete_input]
        delete_confirm = input("是否需要删除该backend：%s，确认请按'y'，按任意键继续：" % backend_delete)
        if delete_confirm == 'y':
            del backend_all_info[backend_delete]  # 在backend与server总字典中删除backend
            backup(file, backend_delete, backend_all_info)  # 调用backup函数，操作文件

        else:   # 删除server
            server_delete_show = server_show(backend_delete, backend_all_info)
            server_delete_num = int(numif(input("请输入需要删除的server编号：")))
            while True:
                if server_delete_num in server_delete_show:
                    server_delete_show.pop(server_delete_num)
                    server_delete_dict_backup = {}
                    server_delete_dict_backup[backend_delete] = server_delete_show.values()
                    backup(file, backend_delete, server_delete_dict_backup)
                    break
                else:
                    server_delete_num = input("输入编号不存在，请重新输入：")  # 提示输入错误


'''
    定义文档备份与回写功能
    file >>> 源文件
    backend_name_action >>> backend 的名称    定位到增删改查的地方
    backend_all_dict >>> backend 的所有信息，--> backend_all_info / 需要修改的信息
'''
def backup(file, backend_name_action, backend_all_dict, *backend_update_name):
    file_new = "%s_new" % file
    add_flag = False    # 为跳过原backend下server信息的写入
    backend_name = "backend %s" % backend_name_action
    backend_update_name = "".join(tuple(backend_update_name))
    with open(file, 'r') as f_read, open(file_new, 'w+') as f_write:
        for line in f_read:
            if line.strip() == backend_name:    # 如果读取的内容是 backend 内容
                if backend_name_action not in backend_all_dict and backend_update_name not in backend_all_dict:
                    add_flag = True
                    pass

                elif backend_update_name in backend_all_info:
                    update_server = "backend %s\n" % backend_update_name
                    f_write.write(update_server)
                    for add_dict in backend_all_info[backend_update_name]:
                        server_line_write = '\t\tserver {name} {IP} weight {weight} maxconn {maxconn}\n'
                        f_write.write(server_line_write.format(**add_dict))  # 格式化输出
                    add_flag = True

                else:
                    f_write.write(line)
                    for add_dict in backend_all_dict[backend_name_action]:
                        server_line_write = '\t\tserver {name} {IP} {weight} maxconn {maxconn}\n'
                        f_write.write(server_line_write.format(**add_dict))
                    add_flag = True

            elif line.strip().startswith("server") and add_flag:
                pass

            else:
                f_write.write(line)
                add_flag = False

    os.system('mv %s %s_backup' % (file, file))
    os.system('mv %s %s' % (file_new, file))


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
flag_main = True
backend_list, backend_all_info = show_list(file)
backend_show_dict = backend_show(backend_list)
action_num = action_list()

while flag_main:
    if action_num == '1':
        query(input("请输入需要查询的backend编号，或者名称"))
        flag_main = backend_exit()
        break

    if action_num == '2':
        insert(input("请输入需要添加的现有backend编号或新backend名称："))
        flag_main = backend_exit()
        break

    if action_num == '3':
        update(input("请输入需要修改的backend编号或名称："))
        flag_main = backend_exit()
        break

    if action_num == '4':
        delete(input("请输入需要删除的backend编号或名称："))
        flag_main = backend_exit()
        break

    if action_num == '5':
        sys.exit()

    elif action_num not in range(5):
        print("\033[31;1m输入错误请重新输入！\033[0m")
        flag_main = False