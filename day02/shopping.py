#!/usr/bin/env python3
# by ysan

product_list = [
    ('iphone', 5400),
    ('mac pro', 22000),
    ('bicycle', 5400),
    ('book', 60),
    ('kindle', 1000)
]

shopping_cart = []

salary = input("请输入工资：")
if salary.isdigit():
    salary = int(salary)
    for index, p_item in enumerate(product_list):
        print(index, p_item)
    while True:
        user_choice = input("选择商品：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                if (salary > product_list[user_choice][1]):
                    salary -= product_list[user_choice][1]
                    print("product \033[41;1m%s\033[0m add successful , u balance \033[31;1m%s\033[0m" % (product_list[user_choice][0], salary))
                    shopping_cart.append(product_list[user_choice])
                else:
                    print("u balance is not enough")
        elif user_choice == 'q':
            print('shopping cart'.center(50, '-'))
            for pro in shopping_cart:
                print(pro)
            print("u balance is %s" % salary)
            exit()
else:
    print("illegal parameter")
    exit()