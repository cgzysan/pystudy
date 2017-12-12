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


