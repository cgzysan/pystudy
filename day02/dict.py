# by ysan


server_line_write = '\t\tserver {name} {IP} {weight} maxconn {maxconn}\n'
add_dict = {'name': 'ysan', 'IP': '127.0.0.1', 'weight': 30, 'maxconn': 4000}

'''
    字典前加** ， 为了打开参数列表
    列表钱加* 
    参考资料 >>> Unpacking Argument Lists  https://docs.python.org/2.7/tutorial/controlflow.html#unpacking-argument-lists
'''

print(range(3, 8))
args = [3, 8]
print(range(*args))

for i in range(5):
    print(i)


print(server_line_write.format(**add_dict))

print(add_dict, type(add_dict))
print(str(add_dict), type(str(add_dict)))

print("----------------------------字典的遍历 >> in 探索 ------------------------------------")

search_dict = {'0': 'www.oldboy.org', '1': 'www.12345.com.cn', '2': 'www.baidu.com', '3': 'wwww.google.com'}
print(search_dict)

search = input('输入查询的 key 值或者 value 值:')
if search in search_dict:
    print("nice")

# print(search_dict[search])