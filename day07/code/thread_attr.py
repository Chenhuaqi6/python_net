from threading import Thread,currentThread
from time import sleep

def fun():
    print("线程属性设置")
    sleep(3)
    print("%s线程执行完毕"%currentThread().getName())

t = Thread(target=fun,name = "Tarena")

t.setDaemon(True)

t.start()

t.setName("chenhuaqi")  #会覆盖原来的名字
print("Thread name:",t.name)
print("Get Thread name",t.name)

print("is_alive",t.is_alive()) #线程状态
# t.join()

print("Daemon:",t.isDaemon())
print("==================main thread================")