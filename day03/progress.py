# by ysan

import sys, time

for i in range(100):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.3)

sys.stdout.write("download successful") # 在我们在 python 调用 print obj 打印的时候，事实上是调用了 sys.stdout.write(obj + \n)
print("print download successful")