# import multiprocessing as mp
from multiprocessing import Process
from time import sleep,ctime

a = 1


#进程函数
def fun():
    print("执行子进程")
    sleep(2)
    global a
    print("a = ", a)
    a = 10000
    print("子进程执行完毕")

#创建进程对象
p = Process(target = fun)

#启动进程
p.start()

for i in range(3):
    sleep(1)
    print(ctime())
#回收进程,防止僵尸进程的产生
# p.join()

print("parent a:", a)
while 1:
    pass
