#二级子进程处理僵尸

import os 
from time import sleep

def f1():
    sleep(3)
    print("事件1...")

def f2():
    sleep(4)
    print("事件2....")

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    p = os.fork()
    if p == 0: #二级子进程
        f2() #执行事件
    else:
        os._exit(0)

else:
    os.wait() #等待一级子进程退出
    f1() #执行事件