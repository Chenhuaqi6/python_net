import os 
from time import sleep

pid = os.fork()

if pid <0:
    print("Create process failed")

elif pid == 0:
    sleep(3)
    print("child process %d exit"%os.getpid())
    os._exit(2)
else:
    # pid,status = os.waitpid(-1,os.WNOHANG) #阻塞
    pid,status = os.wait() #阻塞

    print("pid",pid)
    print("status:",status) #status 返回 256的 exit(x) 的x 倍
    # print("status:",os.WEXITSTATUS(status)) #从父进程得到子进程的退出装态
    while 1:
        pass