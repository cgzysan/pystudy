# by ysan

print ("Hello World")

name = input("name:")
age = int(input("age:"))
salary = input("salary:")

# info1 = '''
# --------- Info of ''' + name + '''----------
# name:''' + name + '''
# age:''' + age + '''
# salary:''' + salary + '''
# '''

# print(info1)

info2 = '''
--------- Info of %s----------
name:%s
age:%d
salary:%s
''' % (name, name, age, salary)

# print(info2)

info3 = '''
--------- Info of {_name}----------
name:{_name}
age:{_age}
salary:{_salary}
''' . format(_name = name,
             _age = age,
             _salary = salary)

print(info3)