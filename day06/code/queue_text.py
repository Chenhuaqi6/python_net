from multiprocessing import Queue
from time import sleep


#创建消息队列
q = Queue(3)

q.put(1)
sleep(0.05)
print(q.empty())
q.put(2)
q.put(3)
print(q.full())
# q.put(4,False) #非阻塞状态
# q.put(4,timeout = 3)  #设置超时 时间
while 1:
    print(q.get())
    if q.qsize() is 0:
        break
q.close()