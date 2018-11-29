from threading import Lock,Thread
from time import sleep
a = b = 0
lock = Lock()



def fun():
    while True:

        # lock.acquire() #枷锁
        with lock:
            if a!=b:
                print("a = %d,b = %d"%(a,b))
t = Thread(target = fun)
t.start()

while 1:
    lock.acquire() #加锁 代码段结束后解锁
    a += 1
    b += 1
    lock.release()

t.join()