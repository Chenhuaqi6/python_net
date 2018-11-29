import os 
from time import sleep
print("========================")
a = 1   #虽然在fork之上 赋值语句直接实在内存空间上创建的 子进程也继承了
p = os.fork()

if p < 0:
    print("创建进程失败")
elif p == 0:
    print("这是子进程")
    print("a=",a)
    a = 10000

else:
    print("这是父进程")
    print("父进程:a = ",a)
