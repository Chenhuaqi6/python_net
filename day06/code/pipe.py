from multiprocessing import Process,Pipe
import os,time

#创建管道

fd1,fd2 = Pipe()

def fun(name):
    time.sleep(3)
    fd1.send("hi "+ name)

jobs = []

for i in ["tom","alex","levi","abby"]:
    p = Process(target = fun,args = (i,))
    jobs.append(p)
    p.start()

for i in range(4):
    #从管道读取内容
    data = fd2.recv()
    print(data)


for i in jobs:
    i.join()




#创建管道
#单向管道  fd1 >>recv   fd2 >>> send
# fd1,fd2 = Pipe(False)

# def fun(name):
#     time.sleep(3)
#     fd2.send("hi "+ name)

# jobs = []

# for i in ["tom","alex","levi","abby"]:
#     p = Process(target = fun,args = (i,))
#     jobs.append(p)
#     p.start()

# for i in range(4):
#     #从管道读取内容
#     data = fd1.recv()
#     print(data)


# for i in jobs:
#     i.join()



