# by ysan


server_line_write = '\t\tserver {name} {IP} {weight} maxconn {maxconn}\n'
add_dict = {'name': 'ysan', 'IP': '127.0.0.1', 'weight': 30, 'maxconn': 4000}

'''
    字典(dict)的方法
    删除指定给定键所对应的值，返回这个值并从字典中把它移除。注意字典pop()方法与列表pop()方法作用完全不同。
    
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

menu = {
    "Mobile phone": [
        ("Iphone7", 6188),
        ("Iphone7 plus", 7888),
        ("Xiaomi5", 2888)
    ],
    "Car": [
        ("Audi Q5", 490000),
        ("Ferrari 488", 4888888)
    ],
    "Drink": [
        ("Milk", 59),
        ("Coffee", 30),
        ("Tea", 311)
    ]
}

for item in enumerate(menu["Mobile phone"]):
    print(item)
    print(item[0], item[1], item[1][0], item[1][1])


print("----------------------------字典的遍历 >> in 探索 ------------------------------------")

search_dict = {'0': 'www.oldboy.org', '1': 'www.12345.com.cn', '2': 'www.baidu.com', '3': 'wwww.google.com'}
print(search_dict)

for key in search_dict:
    print(key)

search = input('输入查询的 key 值或者 value 值:')
if search in search_dict:
    print("nice")

# print(search_dict[search])