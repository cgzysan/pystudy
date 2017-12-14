# by ysan

import sys

argv_find = sys.argv[1]
argv_replace = sys.argv[2]

print(argv_find)
print(argv_replace)

with open("lrc.txt", 'r', encoding="utf-8") as rf,\
     open("lrc4.txt", 'w', encoding="utf-8") as wf:
    for line in rf:
        if argv_find in line:
            line = line.replace(argv_find, argv_replace)
        wf.write(line)