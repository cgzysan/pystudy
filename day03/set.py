# by ysan

# set (集合) 自动去重

list = [1,2,3,4,5,3,2,1]

print(list)

set = set(list)

print(set)

set.add(3)
set.add(5)

print(set)