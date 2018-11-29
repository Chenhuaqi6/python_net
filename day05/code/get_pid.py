import os 
from time import sleep
print("========================")

p = os.fork()

if p < 0:
    print("创建进程失败")
elif p == 0:
    sleep(1)
    print("这是子进程")
    print('从子进程得到父进程pid',os.getppid())
    print('子进程pid',os.getpid())
else:
    print("这是父进程")

    print("父进程得到子进程pid",p)
    print("父进程pid",os.getpid())


#父进程得到子进程的pid 就是 子进程返回值