# by ysan

lrc = open("lrc.txt", encoding="utf-8").read()

file = open("lrc.txt", encoding="utf-8")

print(file.tell())
print(file.readline())
print(file.tell())
print(file.readline())
print(file.tell())
print(file.readline().strip()) # strip 相当于 trim
print(file.readline().strip())
print(file.readline().strip())
print(file.tell())
file.seek(28)
print(file.readline())

file.close()

wFile = open("lrc2.txt", 'w', encoding="utf-8")
wFile.write("故事的小白鸽\n")
wFile.write("从出生那年就开始飘着\n")

wFile.close()

aFile = open("lrc2.txt", 'a', encoding="utf-8")
aFile.write("童年的荡秋千\n")
aFile.write("随记忆一直晃到现在\n")

aFile.close()

'''
    1.read(), readline() 和 readlines() 的区别   
    
        a. .read()每次读取整个文件，它通常将读取到底文件内容放到一个字符串变量中，也就是说 .read() 生成文件内容是一个字符串类型
        b. .readline()每只读取文件的一行，通常也是读取到的一行内容放到一个字符串变量中，返回str类型
        c. .readlines()每次按行读取整个文件内容，将读取到的内容放到一个列表中，返回list类型
    2.python中的 单引号和双引号
    
'''


