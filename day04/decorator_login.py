#!/usr/bin/env python3
# by ysan

user,password = 'ysan', '123456'

def login(func):
    def wrapper():
        user = input("username:").strip()
        pwd = input("password:").strip()

        if user == user and pwd == password:
            print("login successful")
            res = func()
            return res
        else:
            print("invalid  input")

    return wrapper


@login
def test1():
    print("this is test 1")
    return "from home"


print(test1())

print("------------------extra decorator------------------")

def auth(auth_type):
    print("auth type ", auth_type)
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            user = input("username:").strip()
            pwd = input("password:").strip()

            if auth_type == "local":
                if user == user and pwd == password:
                    print("login successful")
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("invalid  input")
            elif auth_type == "net":
                print("don't apply net auth")
            else:
                print("invalid parameter")
                exit()

        return wrapper
    return out_wrapper


@auth(auth_type='local')  # test2 = out_wrapper(test2)
def test2():
    print("this is test 2")


test2()