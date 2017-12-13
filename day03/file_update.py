# by ysan


with open("lrc.txt", encoding="utf-8") as f:    # 通过 with 可以自动关闭文件操作
    for line in f:
        print(line)


with open("lrc.txt", 'r', encoding="utf-8") as rf,\
     open("lrc3.txt", 'w', encoding="utf-8") as wf:
    for line in rf:
        if "故事的小黄花" in line:
            line = line.replace("故事的小黄花", "故事的小白鸽")
        wf.write(line)


