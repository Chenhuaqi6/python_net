from multiprocessing import Process,Queue
import time

#创建队列消息

q = Queue()

def fun1():
    for i in range(10):
        q.put((2,i))

def fun2():
    for i in range(10):
        a,b = q.get()
        print(a * b)

p1 = Process(target = fun1)
p2 = Process(target = fun2)

p1.start()
p2.start()
p1.join()
p2.join()

