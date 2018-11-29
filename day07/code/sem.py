from multiprocessing import Semaphore,Process
from time import sleep
import os

#创建信号量
sem = Semaphore(1)

def fun():
    print("%d 想执行事件"%os.getpid())
    sem.acquire()  #消耗一个信号量
    print("%d 拿到信号执行事件"%os.getpid())
    sleep(3)
    print("%d 事件执行完毕"%os.getpid())
    sem.release()
jobs = []

for i in range(5):
    p = Process(target = fun)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print(sem.get_value())