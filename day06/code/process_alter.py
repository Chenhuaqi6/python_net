from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(4):
        sleep(2)
        print(ctime())

p = Process(target = tm,name = "tedu")

p.daemon = True #主进程结束子进制不再执行 通常不和join同时使用 僵尸进程系统自动处理

p.start()
#打印进程对象属性
print("name:",p.name)
print("pid:",p.pid)
print("alive:",p.is_alive())

# p.join()