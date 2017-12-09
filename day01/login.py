# by ysan
import getpass

# register

username = input("register username:")
password = input("register password:")
# password = getpass.getpass("password:")

infos = {username : password}

count = 0

while count < 3:
    loginname = input("login username:")
    loginpwd = input("login password:")
    if loginname in infos.keys():
        pwd = infos.get(loginname)
        if loginpwd == pwd:
            print("Welcome, Login Successful")
            break
        else:
            print("Incorrect password")
    else:
        print("This name hasn't register")
        infos[loginname] = loginpwd
    count +=1

