from multiprocessing import Process
from time import sleep

# #带参数的进程函数(元组)
# def worker(sec,name):
#     for i in range(3):
#         sleep(sec)
#         print("I'm %s"%name)
#         print("I'm working...")

# p = Process(target = worker,args = (2,"Abby"))

# p.start()

# p.join()



#带参数的进程函数(字典)
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

p = Process(target = worker,kwargs={"sec":2,"name":"陈华齐"})

p.start()

p.join()